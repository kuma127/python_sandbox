# challenge
def is_prime(n: int) -> bool:
    prime_list = list(range(2, n + 1))
    is_processing = True
    index = 0
    while is_processing:
        p = prime_list[index]
        count = 0
        for i in range(0, len(prime_list)):
            if p * (p + i) in prime_list:
                prime_list.remove(p * (p + i))
                count += 1
        if count == 0:
            is_processing = False
        index += 1
    return n in prime_list

def main():
    try:
        num = int(input('検索対象を入力してください：'))
        print(is_prime(num))
    except ValueError:
        print('数値を入力してください')

if __name__ == "__main__":
    main()
