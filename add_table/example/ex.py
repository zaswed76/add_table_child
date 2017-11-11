


gr = {
    "2": 35,
    "1": 25,
    "3": 45
}

def calc_rang(time):
    print(gr.items())
    for k, v in gr.items():
        if time <= v:
            return k
    else: return ""

print(calc_rang(20))
