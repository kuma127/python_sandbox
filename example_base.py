def count_chars(text: str):
    alphabet_count: int = 0
    digit_count: int = 0
    other_count: int = 0

    for char in text:
        if char.isalpha() and char.isascii():
            alphabet_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            other_count += 1
    
    return alphabet_count, digit_count, other_count


if __name__ == "__main__":
    text = "Python Monthly Topics: 2023年7月"
    alphabet_count, digit_count, other_count = count_chars(text)
    print(f"アルファベットの数: {alphabet_count}")
    print(f"数字の数: {digit_count}")
    print(f"それ以外の数: {other_count}")
