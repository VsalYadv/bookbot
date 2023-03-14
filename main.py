def main ():
    file_path = "books/frankenstein.txt"
    text = read_book(file_path)
    no_of_words = words_counter(text)
    char_count = character_counter(text)
    char_list = only_char_strng(char_count)

    print(f"--- Begin report of {file_path} ---")
    print(f"{no_of_words} words found in the document")
    print()

    for item in char_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def read_book(path):
    with open(path) as f:
        text1 = f.read()
    return text1

def to_sort(ch):
    return ch["num"]
     
def words_counter(text2):
    split_text = text2.split()
    return len(split_text)

def only_char_strng(char_count_dict1):
    only_char = []
    for ch in char_count_dict1:
        only_char.append({"char" : ch, "num" :char_count_dict1[ch]})
    only_char.sort(reverse = True , key =to_sort) 
    return only_char


def character_counter(text3):
    char_count_dict = {}
    for ch in text3:
        small_case = ch.lower()
        if small_case in char_count_dict:
            char_count_dict[small_case] +=1
        else:
            char_count_dict[small_case] =1 
    return char_count_dict

main()