import re


def char_count(a_string: str)-> dict:
    a_dict = {}
    for char in a_string:
        if char in a_dict:
            a_dict[char] += 1
        else:
            a_dict[char] = 1
    return a_dict


## challenge
def duplicate_delete(sentence: str)-> str:
    word_list = re.split('[ .]', sentence)
    a_dict = {}
    out_list = []
    for index, a_string in enumerate(word_list):
        if a_string not in a_dict:
            out_list.append(a_string)
            a_dict[a_string] = index

    return ' '.join(out_list).strip() + '.'


def main():
    a_string = 'I am a self-taught programmer looking for a job as a programmer.'
    out = duplicate_delete(a_string)
    print(out)


if __name__ == "__main__":
    main()
