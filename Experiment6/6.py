max_min = lambda lst: (
    (lambda l: (
        (lambda mx, mn: (mx, mn))(
            (lambda l: [mx := l[0]] or [mx := x if x > mx else mx for x in l] and mx)(l),
            (lambda l: [mn := l[0]] or [mn := x if x < mn else mn for x in l] and mn)(l)
        )
    ))(lst)
)
ls=[10, 6, 8, 90, 12, 56]
print(max_min(ls))