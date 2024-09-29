import re
import replacer
from timeit import timeit

def replace_with_pattern(pattern, text, replacement):
    return re.sub(pattern, replacement, text)

if __name__ == "__main__":
    pattern = r"\d+"
    text = "Hello01Python23Rust45with678maturin"  # 置換対象文字列
    replacement = "-"

    loop = 1000
    # 本スクリプト内のPython関数の実行結果を表示
    p_res = timeit(lambda: replace_with_pattern(pattern, text, replacement), number=loop)
    # 1回あたりの平均実行時間をマイクロ秒で計算
    p_time = p_res / loop * 1_000_000
    print(f"Python Avg: {p_time:.2f} μs/call")

    # PythonバインディングによるRustの実行結果を表示
    r_res = timeit(lambda: replacer.replace_with_pattern(pattern, text, replacement), number=loop)
    # 1回あたりの平均実行時間をマイクロ秒で計算
    r_time = r_res / loop * 1_000_000
    print(f"Rust Avg: {r_time:.2f} μs/call")
