def calc_op(op, x):
    res = 0
    for i in range(0, len(op)):
        res += op[i] * pow(x, i)
    return (res)

def my_div(num, den):
    if (den == 0):
        print("Error Divsion by Zero")
        exit(84)
    return (num / den)

def main_loop(tab, step):
    x = 0
    while (x <= 1 + step):
        res = 1
        for i in range(0, len(tab), 2):
            num = calc_op(tab[i], x)
            den = calc_op(tab[i + 1], x)
            res *= my_div(num, den)
        print("{0:.3g} -> {1:.5f}".format(x, res))
        x += step
    return (res)
