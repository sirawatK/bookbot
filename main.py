from stats import get_book_text, counts_word, char_each_num

def main():
	contents = get_book_text("books/frankenstein.txt")
	words = counts_word(contents)
	print(f"{words} words found in the document")
	dict_num = char_each_num(contents)
	print(dict_num)

main()
