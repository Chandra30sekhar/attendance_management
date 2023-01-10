def calculate(no_attended, total):
    p = (no_attended / total) * 100
    return "{:.2f}".format(p)


# print(calculate(10, 43))