import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data():
    try:
        df = pd.read_csv("meals.csv", header=None, on_bad_lines='skip')
        df.columns = ["date", "day", "meal", "calories", "protein", "carbs"]

        df["calories"] = pd.to_numeric(df["calories"])
        df["protein"] = pd.to_numeric(df["protein"])
        df["carbs"] = pd.to_numeric(df["carbs"])

        return df
    except FileNotFoundError:
        print("❌ No data found. Add meals first.")
        return None


def daily_calories(df):
    result = df.groupby("date")["calories"].sum()
    print("\n Daily Calories:\n", result)


def protein_analysis(df):
    avg_protein = np.mean(df["protein"])
    
    print(f"\n Average Protein Intake: {avg_protein:.2f}")

    if avg_protein < 50:
        print(" Low protein intake! Try eggs, paneer, chicken.")
    else:
        print(" Good protein intake!")


def carb_analysis(df):
    avg_carbs = np.mean(df["carbs"])
    print(f"\n Average Carbs: {avg_carbs:.2f}")

    if avg_carbs > 250:
        print(" High carb diet detected!")
    else:
        print(" Carb intake is balanced.")

def health_score(df):
    daily = df.groupby("date").sum()

    best_day = daily["protein"].idxmax()
    worst_day = daily["calories"].idxmax()

    print(f"\n Best Day (High Protein): {best_day}")
    print(f" Worst Day (High Calories): {worst_day}")


# def health_score_advanced(df):
#     daily = df.groupby("date").sum()
#     scores = []

#     for _, row in daily.iterrows():
#         score = 0

#         if row["protein"] >= 50:
#             score += 3
#         if 1800 <= row["calories"] <= 2500:
#             score += 3
#         if row["carbs"] <= 250:
#             score += 2

#         score += 2  # meals logged

#         scores.append(score)

#     avg_score = sum(scores) / len(scores)
#     print(f"\n Health Score: {avg_score:.2f} / 10")


def weekly_trend(df):
    df["date"] = pd.to_datetime(df["date"])
    weekly = df.groupby(df["date"].dt.isocalendar().week)["calories"].mean()

    print("\n Weekly Average Calories:\n", weekly)


def smart_insights(df):
    avg_protein = df["protein"].mean()
    avg_carbs = df["carbs"].mean()

    print("\n Smart Insights:")

    if avg_protein < 50:
        print(" Protein intake is LOW. Add eggs, paneer, or chicken.")
    else:
        print(" Protein intake is good.")

    if avg_carbs > 250:
        print(" High carb diet detected. Reduce rice/roti.")
    else:
        print(" Carb intake is balanced.")

def diet_recommendation(df):
    avg_cal = df["calories"].mean()
    avg_protein = df["protein"].mean()
    avg_carbs = df["carbs"].mean()

    print("\n Personalized Recommendations:")

    if avg_cal < 1800:
        print("^^Increase calorie intake. Add rice, paneer, or fruits.")
    elif avg_cal > 2500:
        print("⬇ Reduce calorie intake. Avoid fried food and sweets.")
    else:
        print(" Calorie intake is within healthy range.")

    if avg_protein < 50:
        print(" Increase protein: eggs, chicken, paneer, dal.")
    else:
        print(" Protein intake is sufficient.")

    if avg_carbs > 250:
        print(" Reduce carbs: limit rice/roti portions.")
    else:
        print(" Carb intake is balanced.")

    if avg_protein < 50 and avg_carbs > 250:
        print(" High-carb & low-protein diet detected — rebalance meals.")


def plot_calories(df):
    daily = df.groupby("date")["calories"].sum()
    daily.plot(kind="bar")
    plt.title("Daily Calories")
    plt.xlabel("Date")
    plt.ylabel("Calories")
    plt.tight_layout()
    plt.show()


def full_report():
    df = load_data()
    if df is None:
        return

    print("\n====== HEALTH REPORT ======")

    daily_calories(df)
    protein_analysis(df)
    carb_analysis(df)
    health_score(df)
    weekly_trend(df)
    smart_insights(df)
    diet_recommendation(df)

    plot_calories(df)