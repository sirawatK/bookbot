def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def counts_word(contents):
	list_word = contents.split()
	return len(list_word)
