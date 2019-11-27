

def fibonacci(n,a=1,b=0):

    if n == 0:
        return a

    return fibonacci(n-1,a+b,a)


if __name__=="__main__":

    n = int(input())

    print(fibonacci(n))
