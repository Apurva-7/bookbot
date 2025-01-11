def main():
    book_path = "books/frankenstein.txt"    
    text = get_book_text(book_path)

    print(f"--- Begin report of {book_path} ---")
    book_word_count = count_words(text)
    print(f"{book_word_count} words found in the document")
    
    char_count = count_char_appearance(text)
    print_char_count_report(char_count)
    print("--- End report ---")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(book):
    words = book.split()
    return len(words)

def count_char_appearance(text) :
    char_dict = {}

    for ch in text:
        ch = ch.lower()
        if ch not in char_dict :
            char_dict[ch] = 1
        else :
            char_dict[ch] += 1
    
    return char_dict

def print_char_count_report(dict) :
    count_ch_list = dict_list_func(dict)
    for ch in count_ch_list :
        print(f"The {ch["ch"]} character was found {ch["count"]} times.")

def dict_list_func(dict) :
    dict_list = []

    for el in dict :
        if el.isalpha() == True :
            ch_dict = {"ch" : el, "count" : dict[el]}
            dict_list.append(ch_dict)
    
    dict_list.sort(reverse=True, key = sort_key_cr)
    return dict_list

def sort_key_cr(dict):
    return dict["count"]


main()
