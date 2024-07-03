def fibo(N):

    x0, x1 = 0, 1
    while N > 0:
        yield x0
        x0, x1 = x1, x0 + x1
        N -= 1

def main():
    N = 16
    gen = fibo(N)
    # for v in gen:
    #     print(v, end=' ')
    print(list(gen))


if __name__ == '__main__':
    main()
