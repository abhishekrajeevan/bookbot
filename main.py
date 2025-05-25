import sys
from stats import get_book_text, get_num_words, get_num_characters, get_output

def main():
    args = sys.argv[1:]
    print(args)
    if not args:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    content = get_book_text(args[0])
    print(content)
    num_words = get_num_words(content)
    print(f'Found {num_words} total words')
    num_characters = get_num_characters(content)
    #print(num_characters)
    output = get_output(num_characters)
    for i in output:
        if i['char'].isalpha():
            print(f'{i['char']}: {i['num']}')

if __name__ == '__main__':
    main()