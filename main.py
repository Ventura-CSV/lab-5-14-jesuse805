def fibo(N):

    x0, x1 = 0, 1
    count = 0
    while count < N:
        yield x0
        x0, x1 = x1, x0 + x1
        count += 1

def main():
    N = 16
    gen = fibo(N)
    # for v in gen:
    #     print(v, end=' ')
    print(list(gen))


if __name__ == '__main__':
    main()
