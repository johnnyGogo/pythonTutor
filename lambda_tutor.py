import fire

def lambda_tutor():
    # lambda arg1, arg2, ....: expression
    max = lambda m, n: m if m > n else n
    print(max(10, 3))


if __name__ == '__main__':
    fire.Fire()