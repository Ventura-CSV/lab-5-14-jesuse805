def fibo(N):

    a, b = 0, 1
    while N > 0:
        yield a
        a, b = b, a + b
        N -= 1

def main():
    N = 16
    gen = fibo(N)
    # for v in gen:
    #     print(v, end=' ')
    print(list(gen))


if __name__ == '__main__':
    main()
