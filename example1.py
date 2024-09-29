import strcounter

if __name__ == "__main__":
    text = "Python Monthly Topics: 2023年7月"
    alphabet_count, digit_count, other_count = strcounter.count_chars(text)
    print(f"アルファベットの数: {alphabet_count}")
    print(f"数字の数: {digit_count}")
    print(f"それ以外の数: {other_count}")
