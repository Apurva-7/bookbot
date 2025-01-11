def main():
    book_path = "books/frankenstein.txt"    
    text = get_book_text(book_path)
    print(text)

    frankenstein_word_count = count_words(text)
    print(f"Number of words in Frankenstein book : {frankenstein_word_count}")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(book):
    word_count = 0
    words = book.split()

    for word in words :
        word_count += 1
    return word_count


main()
