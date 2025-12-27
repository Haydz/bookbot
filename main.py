from stats import count_words, count_chars, sort_dict, report
import sys



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def report(filepath, num_words, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(num_words)
    print("--------- Character Count -------")
    for i in sorted_dict:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")



def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    #print("test")
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = count_words(text)
    num_chars = count_chars(text)
    sorted_dict = sort_dict(num_chars)
    report(filepath, num_words, sorted_dict)
main()
