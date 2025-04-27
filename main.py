from stats import get_book_text, counts_word

def main():
	contents = get_book_text("books/frankenstein.txt")
	words = counts_word(contents)
	print(f"{words} words found in the document")

main()
