from stats import *
import sys


def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	contents = get_book_text(sys.argv[1])
	words = counts_word(contents)
	dict_num = char_each_num(contents)
	dict_num = sort_dict(dict_num)
	print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}")
	print(f"----------- Word Count ----------\nFound {words} total words")
	print("--------- Character Count -------")
	for d in dict_num:
		print(f"{d}: {dict_num[d]}")
	print("============= END ===============")



main()
