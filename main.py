def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def counts_word(contents):
	list_word = contents.split()
	return len(list_word)

def main():
	contents = get_book_text("books/frankenstein.txt")
	words = counts_word(contents)
	print(f"{words} words found in the document")

main()
