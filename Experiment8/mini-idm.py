# ============================================================
# Mini Internet Download Manager
# ============================================================
# Required pip installs:
#   pip install requests
#
# Standard library modules used (no install needed):
#   tkinter, threading, os, time, re
# ============================================================

import os
import re
import time
import threading
import tkinter as tk
from tkinter import ttk, messagebox

import requests

# ─────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────
CHUNK_SIZE      = 1024          # bytes per chunk
WINDOW_WIDTH    = 660
WINDOW_HEIGHT   = 420
BG_DARK         = "#0f1117"
BG_CARD         = "#1a1d27"
BG_INPUT        = "#12151f"
ACCENT          = "#4f8ef7"
ACCENT_HOVER    = "#6aa3ff"
TEXT_PRIMARY    = "#e8eaf0"
TEXT_SECONDARY  = "#7a7f99"
TEXT_SUCCESS    = "#3ecf8e"
TEXT_ERROR      = "#f76f72"
TEXT_WARNING    = "#f7c94f"
BORDER          = "#2a2d3e"
FONT_TITLE      = ("Consolas", 18, "bold")
FONT_LABEL      = ("Segoe UI", 10)
FONT_LABEL_BOLD = ("Segoe UI", 10, "bold")
FONT_MONO       = ("Consolas", 9)
FONT_STATUS     = ("Segoe UI", 9)
FONT_BTN        = ("Segoe UI", 10, "bold")
FONT_URL        = ("Consolas", 10)


# ─────────────────────────────────────────────
# HELPER – extract filename from URL
# ─────────────────────────────────────────────
def extract_filename(url: str) -> str:
    """
    Try to pull a clean filename from the URL path.
    Falls back to 'downloaded_file' if nothing useful is found.
    """
    path = url.split("?")[0]          # strip query string
    name = path.rstrip("/").split("/")[-1]
    name = re.sub(r'[<>:"/\\|?*]', "_", name)  # sanitise bad chars
    return name if name else "downloaded_file"


# ─────────────────────────────────────────────
# CORE DOWNLOAD LOGIC  (runs in a background thread)
# ─────────────────────────────────────────────
def download_file(url: str, callbacks: dict, stop_event: threading.Event,
                  pause_event: threading.Event):
    """
    Download *url* in streaming chunks and invoke GUI callbacks.

    callbacks keys:
        on_progress(pct, speed_kb, downloaded, total)
        on_complete(filename, elapsed)
        on_error(message)
    """
    try:
        # ── HEAD request to get content-length ──────────────────
        try:
            head = requests.head(url, timeout=10, allow_redirects=True)
            total_size = int(head.headers.get("content-length", 0))
        except Exception:
            total_size = 0          # unknown size – progress shows 0 %

        filename = extract_filename(url)
        save_path = os.path.join(os.getcwd(), filename)

        # ── Streaming GET ────────────────────────────────────────
        response = requests.get(url, stream=True, timeout=15)
        response.raise_for_status()

        # Use content-length from GET response if HEAD missed it
        if total_size == 0:
            total_size = int(response.headers.get("content-length", 0))

        downloaded   = 0
        start_time   = time.time()
        last_time    = start_time
        last_bytes   = 0

        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):

                # ── CANCEL check ────────────────────────────────
                if stop_event.is_set():
                    f.close()
                    try:
                        os.remove(save_path)
                    except OSError:
                        pass
                    callbacks["on_error"]("Download cancelled.")
                    return

                # ── PAUSE check (spin until resumed) ────────────
                while pause_event.is_set():
                    if stop_event.is_set():
                        f.close()
                        try:
                            os.remove(save_path)
                        except OSError:
                            pass
                        callbacks["on_error"]("Download cancelled.")
                        return
                    time.sleep(0.1)

                if not chunk:
                    continue

                f.write(chunk)
                downloaded += len(chunk)

                # ── Speed calculation (rolling 0.5 s window) ────
                now = time.time()
                elapsed_window = now - last_time
                if elapsed_window >= 0.5:
                    speed_kb = (downloaded - last_bytes) / elapsed_window / 1024
                    last_time  = now
                    last_bytes = downloaded
                else:
                    total_elapsed = now - start_time
                    speed_kb = (downloaded / total_elapsed / 1024) if total_elapsed > 0 else 0

                # ── Progress ────────────────────────────────────
                pct = (downloaded / total_size * 100) if total_size else 0
                callbacks["on_progress"](pct, speed_kb, downloaded, total_size)

        elapsed = time.time() - start_time
        callbacks["on_complete"](filename, elapsed)

    except requests.exceptions.MissingSchema:
        callbacks["on_error"]("Invalid URL — please include http:// or https://")
    except requests.exceptions.ConnectionError:
        callbacks["on_error"]("Connection error — check your internet or the URL.")
    except requests.exceptions.Timeout:
        callbacks["on_error"]("Request timed out — server took too long to respond.")
    except requests.exceptions.HTTPError as e:
        callbacks["on_error"](f"HTTP error: {e}")
    except Exception as e:
        callbacks["on_error"](f"Unexpected error: {e}")


# ─────────────────────────────────────────────
# GUI APPLICATION CLASS
# ─────────────────────────────────────────────
class DownloadManagerApp:
    """
    Tkinter GUI for the Mini Internet Download Manager.
    All GUI updates from the background thread go through
    root.after() to stay thread-safe.
    """

    def __init__(self, root: tk.Tk):
        self.root = root
        self._configure_root()
        self._build_ui()

        # Thread-control events
        self._stop_event  = threading.Event()
        self._pause_event = threading.Event()
        self._dl_thread: threading.Thread | None = None
        self._paused = False

    # ── Root window setup ─────────────────────────────────────
    def _configure_root(self):
        self.root.title("IDM Lite — Download Manager")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_DARK)
        # Centre on screen
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth()  - WINDOW_WIDTH)  // 2
        y = (self.root.winfo_screenheight() - WINDOW_HEIGHT) // 2
        self.root.geometry(f"+{x}+{y}")

    # ── Build all widgets ─────────────────────────────────────
    def _build_ui(self):
        # ── ttk style ──────────────────────────────────────────
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Horizontal.TProgressbar",
                         troughcolor=BG_INPUT,
                         background=ACCENT,
                         bordercolor=BORDER,
                         lightcolor=ACCENT,
                         darkcolor=ACCENT,
                         thickness=14)

        # ── Outer padding frame ────────────────────────────────
        outer = tk.Frame(self.root, bg=BG_DARK)
        outer.pack(expand=True, fill="both", padx=30, pady=20)

        # ── Title bar ──────────────────────────────────────────
        title_row = tk.Frame(outer, bg=BG_DARK)
        title_row.pack(fill="x", pady=(0, 18))

        tk.Label(title_row, text="⬇", font=("Segoe UI Emoji", 22),
                 bg=BG_DARK, fg=ACCENT).pack(side="left", padx=(0, 10))
        title_block = tk.Frame(title_row, bg=BG_DARK)
        title_block.pack(side="left")
        tk.Label(title_block, text="IDM Lite", font=FONT_TITLE,
                 bg=BG_DARK, fg=TEXT_PRIMARY).pack(anchor="w")
        tk.Label(title_block, text="Mini Internet Download Manager",
                 font=FONT_STATUS, bg=BG_DARK, fg=TEXT_SECONDARY).pack(anchor="w")

        # ── Card ───────────────────────────────────────────────
        card = tk.Frame(outer, bg=BG_CARD, bd=0, highlightthickness=1,
                        highlightbackground=BORDER)
        card.pack(fill="x", pady=(0, 14))

        inner = tk.Frame(card, bg=BG_CARD)
        inner.pack(fill="x", padx=22, pady=18)

        # URL label + entry
        tk.Label(inner, text="Download URL", font=FONT_LABEL_BOLD,
                 bg=BG_CARD, fg=TEXT_SECONDARY).pack(anchor="w", pady=(0, 5))

        url_frame = tk.Frame(inner, bg=BG_INPUT, bd=0, highlightthickness=1,
                             highlightbackground=BORDER)
        url_frame.pack(fill="x")

        self.url_var = tk.StringVar()
        self.url_entry = tk.Entry(url_frame, textvariable=self.url_var,
                                  font=FONT_URL, bg=BG_INPUT, fg=TEXT_PRIMARY,
                                  insertbackground=ACCENT, relief="flat",
                                  bd=0)
        self.url_entry.pack(side="left", fill="x", expand=True, padx=10, pady=8)
        self.url_entry.insert(0, "https://")

        # Clear button inside entry
        self._clear_btn = tk.Label(url_frame, text="✕", font=("Segoe UI", 9),
                                   bg=BG_INPUT, fg=TEXT_SECONDARY, cursor="hand2")
        self._clear_btn.pack(side="right", padx=8)
        self._clear_btn.bind("<Button-1>", lambda _: self._clear_url())

        # ── Stats row ─────────────────────────────────────────
        stats_frame = tk.Frame(inner, bg=BG_CARD)
        stats_frame.pack(fill="x", pady=(16, 0))

        # Status
        left = tk.Frame(stats_frame, bg=BG_CARD)
        left.pack(side="left", expand=True, anchor="w")
        tk.Label(left, text="STATUS", font=("Segoe UI", 7, "bold"),
                 bg=BG_CARD, fg=TEXT_SECONDARY).pack(anchor="w")
        self.status_label = tk.Label(left, text="Idle", font=FONT_LABEL_BOLD,
                                     bg=BG_CARD, fg=TEXT_SECONDARY)
        self.status_label.pack(anchor="w")

        # Speed
        mid = tk.Frame(stats_frame, bg=BG_CARD)
        mid.pack(side="left", expand=True)
        tk.Label(mid, text="SPEED", font=("Segoe UI", 7, "bold"),
                 bg=BG_CARD, fg=TEXT_SECONDARY).pack(anchor="w")
        self.speed_label = tk.Label(mid, text="— KB/s", font=FONT_LABEL_BOLD,
                                    bg=BG_CARD, fg=TEXT_SECONDARY)
        self.speed_label.pack(anchor="w")

        # Size
        right = tk.Frame(stats_frame, bg=BG_CARD)
        right.pack(side="right", expand=True, anchor="e")
        tk.Label(right, text="SIZE", font=("Segoe UI", 7, "bold"),
                 bg=BG_CARD, fg=TEXT_SECONDARY).pack(anchor="e")
        self.size_label = tk.Label(right, text="—", font=FONT_LABEL_BOLD,
                                   bg=BG_CARD, fg=TEXT_SECONDARY)
        self.size_label.pack(anchor="e")

        # ── Progress bar + percentage ──────────────────────────
        prog_frame = tk.Frame(inner, bg=BG_CARD)
        prog_frame.pack(fill="x", pady=(14, 0))

        self.pct_label = tk.Label(prog_frame, text="0%",
                                  font=("Consolas", 10, "bold"),
                                  bg=BG_CARD, fg=ACCENT, width=5, anchor="e")
        self.pct_label.pack(side="right", padx=(8, 0))

        self.progress_var = tk.DoubleVar(value=0)
        self.progress_bar = ttk.Progressbar(prog_frame,
                                            variable=self.progress_var,
                                            maximum=100,
                                            style="Custom.Horizontal.TProgressbar")
        self.progress_bar.pack(fill="x", side="left", expand=True)

        # ── File label ────────────────────────────────────────
        self.file_label = tk.Label(inner, text="",
                                   font=FONT_MONO, bg=BG_CARD, fg=TEXT_SECONDARY,
                                   anchor="w")
        self.file_label.pack(fill="x", pady=(8, 0))

        # ── Button row ────────────────────────────────────────
        btn_row = tk.Frame(outer, bg=BG_DARK)
        btn_row.pack(fill="x")

        self.dl_btn = self._make_button(btn_row, "⬇  Download",
                                        ACCENT, self._start_download)
        self.dl_btn.pack(side="left", padx=(0, 8))

        self.pause_btn = self._make_button(btn_row, "⏸  Pause",
                                           "#3b3f55", self._toggle_pause,
                                           state="disabled")
        self.pause_btn.pack(side="left", padx=(0, 8))

        self.cancel_btn = self._make_button(btn_row, "✕  Cancel",
                                            "#3b3f55", self._cancel_download,
                                            state="disabled")
        self.cancel_btn.pack(side="left")

        # ── Footer ────────────────────────────────────────────
        tk.Label(outer, text="Files are saved to the current working directory",
                 font=("Segoe UI", 8), bg=BG_DARK, fg=TEXT_SECONDARY).pack(
                 side="bottom", pady=(12, 0))

    # ── Button factory ───────────────────────────────────────
    def _make_button(self, parent, text, color, command, state="normal"):
        btn = tk.Label(parent, text=text, font=FONT_BTN,
                       bg=color, fg=TEXT_PRIMARY,
                       padx=18, pady=9, cursor="hand2",
                       relief="flat")
        if state == "normal":
            btn.bind("<Button-1>", lambda _: command())
            btn.bind("<Enter>",    lambda _, b=btn, c=color: b.config(bg=self._lighten(c)))
            btn.bind("<Leave>",    lambda _, b=btn, c=color: b.config(bg=c))
        btn._cmd     = command
        btn._enabled = (state == "normal")
        btn._color   = color
        return btn

    @staticmethod
    def _lighten(hex_color: str) -> str:
        """Return a slightly lighter shade of a hex colour."""
        hex_color = hex_color.lstrip("#")
        r, g, b = (int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        return "#{:02x}{:02x}{:02x}".format(
            min(r + 30, 255), min(g + 30, 255), min(b + 30, 255))

    def _enable_btn(self, btn, color=None):
        btn._enabled = True
        btn._color   = color or btn._color
        btn.config(bg=btn._color, cursor="hand2")
        btn.bind("<Button-1>", lambda _: btn._cmd())
        btn.bind("<Enter>",    lambda _, b=btn: b.config(bg=self._lighten(b._color)))
        btn.bind("<Leave>",    lambda _, b=btn: b.config(bg=b._color))

    def _disable_btn(self, btn):
        btn._enabled = False
        btn.config(bg="#2a2d3e", cursor="arrow")
        btn.unbind("<Button-1>")
        btn.unbind("<Enter>")
        btn.unbind("<Leave>")

    # ── URL helpers ──────────────────────────────────────────
    def _clear_url(self):
        self.url_var.set("")
        self.url_entry.focus()

    # ── Download control ─────────────────────────────────────
    def _start_download(self):
        url = self.url_var.get().strip()
        if not url or url == "https://":
            messagebox.showwarning("No URL", "Please enter a download URL first.")
            return
        if not url.startswith(("http://", "https://")):
            messagebox.showerror("Invalid URL",
                                 "URL must start with http:// or https://")
            return

        # Reset state
        self._stop_event.clear()
        self._pause_event.clear()
        self._paused = False
        self._reset_progress()
        self._set_status("Downloading…", TEXT_WARNING)
        self.file_label.config(text=f"Saving: {extract_filename(url)}")

        # Toggle buttons
        self._disable_btn(self.dl_btn)
        self._enable_btn(self.pause_btn,  "#3b3f55")
        self._enable_btn(self.cancel_btn, "#3b3f55")
        self.pause_btn.config(text="⏸  Pause")

        # Build callbacks (called from worker thread → schedule on main thread)
        callbacks = {
            "on_progress": lambda p, s, d, t: self.root.after(
                0, self._on_progress, p, s, d, t),
            "on_complete": lambda fn, el: self.root.after(
                0, self._on_complete, fn, el),
            "on_error":    lambda msg: self.root.after(
                0, self._on_error, msg),
        }

        self._dl_thread = threading.Thread(
            target=download_file,
            args=(url, callbacks, self._stop_event, self._pause_event),
            daemon=True
        )
        self._dl_thread.start()

    def _toggle_pause(self):
        if not self._paused:
            self._pause_event.set()
            self._paused = True
            self.pause_btn.config(text="▶  Resume")
            self._set_status("Paused", TEXT_WARNING)
        else:
            self._pause_event.clear()
            self._paused = False
            self.pause_btn.config(text="⏸  Pause")
            self._set_status("Downloading…", TEXT_WARNING)

    def _cancel_download(self):
        self._stop_event.set()
        self._pause_event.clear()   # unblock paused thread so it can exit
        self._set_status("Cancelling…", TEXT_ERROR)

    # ── GUI callbacks (always on main thread) ────────────────
    def _on_progress(self, pct: float, speed_kb: float,
                     downloaded: int, total: int):
        self.progress_var.set(pct)
        self.pct_label.config(text=f"{pct:.1f}%")
        self.speed_label.config(text=f"{speed_kb:.1f} KB/s", fg=ACCENT)

        if total:
            dl_mb    = downloaded / (1024 * 1024)
            total_mb = total      / (1024 * 1024)
            self.size_label.config(
                text=f"{dl_mb:.2f} / {total_mb:.2f} MB", fg=TEXT_PRIMARY)
        else:
            dl_kb = downloaded / 1024
            self.size_label.config(text=f"{dl_kb:.1f} KB", fg=TEXT_PRIMARY)

    def _on_complete(self, filename: str, elapsed: float):
        self.progress_var.set(100)
        self.pct_label.config(text="100%")
        self._set_status("Completed ✓", TEXT_SUCCESS)
        self.speed_label.config(text=f"Done in {elapsed:.1f}s", fg=TEXT_SUCCESS)
        self.file_label.config(text=f"✓ Saved: {filename}", fg=TEXT_SUCCESS)
        self._restore_buttons()

    def _on_error(self, message: str):
        self._set_status("Error", TEXT_ERROR)
        self.file_label.config(text=f"✗ {message}", fg=TEXT_ERROR)
        self.speed_label.config(text="— KB/s", fg=TEXT_SECONDARY)
        messagebox.showerror("Download Error", message)
        self._restore_buttons()

    # ── UI helpers ───────────────────────────────────────────
    def _set_status(self, text: str, color: str):
        self.status_label.config(text=text, fg=color)

    def _reset_progress(self):
        self.progress_var.set(0)
        self.pct_label.config(text="0%")
        self.speed_label.config(text="— KB/s", fg=TEXT_SECONDARY)
        self.size_label.config(text="—",       fg=TEXT_SECONDARY)
        self.file_label.config(text="",        fg=TEXT_SECONDARY)

    def _restore_buttons(self):
        self._enable_btn(self.dl_btn, ACCENT)
        self.dl_btn.config(text="⬇  Download")
        self._disable_btn(self.pause_btn)
        self._disable_btn(self.cancel_btn)
        self.pause_btn.config(text="⏸  Pause")
        self._paused = False


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app  = DownloadManagerApp(root)
    root.mainloop()