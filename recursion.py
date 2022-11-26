def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# challenge
def recursion(n):
    if n > 10:
        return
    print(n)
    return recursion(n + 1)

def main():
    # result = factorial(5)
    # print(result)
    recursion(1)

if __name__ == "__main__":
    main()
