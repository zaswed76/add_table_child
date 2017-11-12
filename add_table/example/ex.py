


gr = {
    "1": [0, 20],
    "2": [21, 30],
    "3": [31, 40]
}

def calc_rang(time):
    for m, interval in gr.items():
        if time in range(interval[0], interval[1] + 1):
            return m
    else: return ""

print(calc_rang(21))
