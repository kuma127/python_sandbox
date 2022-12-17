class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, data) -> None:
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self) -> int:
        return len(self.items)

    def is_empty(self):
        return not self.items


class MaxStack():
    def __init__(self) -> None:
        self.main = []
        self.max = []

    def push(self, n) -> None:
        if len(self.main) == 0:
            self.max.append(n)
        elif n >= self.max[-1]:
            self.max.append(n)
        self.main.append(n)

    def pop(self) -> list:
        self.max.pop()
        return self.main.pop()

    def get_max(self) -> int:
        return self.max[-1]


def reverse_string(a_string) -> str:
    stack = []
    string = ""
    for c in a_string:
        stack.append(c)
    for _ in a_string:
        string += stack.pop()
    return string


def check_parentheses(a_string):
    stack = []
    for c in a_string:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


def check_brackets(a_string):
    parentheses_stack = []
    curly_brackets = []
    for c in a_string:
        if c == "(":
            parentheses_stack.append(c)
        elif c == ")":
            if len(parentheses_stack) == 0:
                return False
            parentheses_stack.pop()
        elif c == "{":
            curly_brackets.append(c)
        elif c == "}":
            if len(curly_brackets) == 0:
                return False
            curly_brackets.pop()
    return len(parentheses_stack) == 0 and len(curly_brackets) == 0


def main():
    # test = "{print(lentest))}"
    # print(check_brackets(test))
    test_list = [1, 5, 43, 23, 35, 36]
    max_stack = MaxStack()
    for c in test_list:
        max_stack.push(c)
    print(max_stack.get_max())


if __name__ == "__main__":
    main()
