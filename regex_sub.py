import re

def replace_with_pattern(pattern, text, replacement):
    return re.sub(pattern, replacement, text)


if __name__ == "__main__":
    pattern = r"\d+"
    text = "Hello01Python23Rust45with678maturin"  # 置換対象文字列
    replacement = "-"

    print(replace_with_pattern(pattern, text, replacement))
