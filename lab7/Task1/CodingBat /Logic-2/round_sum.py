def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


def round10(num):
    rd = num % 10
    if (rd >= 5):
        return num + 10 - rd
    return num - rd
