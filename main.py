def fibo(N):

    a, b = 0, 1
    while N > 0:

def main():
    N = 10
    gen = fibo(N)
    # for v in gen:
    #     print(v, end=' ')
    print(list(gen))


if __name__ == '__main__':
    main()
