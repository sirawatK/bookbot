def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def counts_word(contents):
	list_word = contents.split()
	return len(list_word)

def char_each_num(contents):
	contents = contents.lower()
	dict_num = {}
	for charecter in contents:
		dict_num[charecter] = dict_num.get(charecter, 0) + 1
	return dict_num

