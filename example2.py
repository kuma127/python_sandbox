import requests
import strcounter
from timeit import timeit

def count_chars(text: str):
    alphabet_count = 0
    digit_count = 0
    other_count = 0

    for char in text:
        if char.isalpha() and char.isascii():
            alphabet_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            other_count += 1
    
    return alphabet_count, digit_count, other_count


if __name__ == "__main__":
    url = "https://gihyo.jp/article/2023/06/monthly-python-2306"
    res = requests.get(url)
    res.encoding = "utf-8"
    text = res.text

    loop = 1000
    # 本スクリプト内のPython関数の実行結果を表示
    p_res = timeit(lambda: count_chars(text), number=loop)
    # 1回あたりの平均実行時間をマイクロ秒で計算
    p_time = p_res / loop * 1_000_000
    print(f"Python Avg: {p_time:.2f} μs/call")

    # PythonバインディングによるRustの実行結果を表示
    r_res = timeit(lambda: strcounter.count_chars(text), number=loop)
    # 1回あたりの平均実行時間をマイクロ秒で計算
    r_time = r_res / loop * 1_000_000
    print(f"Rust Avg: {r_time:.2f} μs/call")
