def plus(a: int, b: int):
    return a + b


if __name__ == '__main__':
    a = int(input('a - '))
    b = int(input('b - '))
    print(f"{a}+{b}={plus(a, b)}")
