def get_book_text(filepath):
	with open(filepath, 'r') as f:
		file_contents = f.read()
	return file_contents

def get_num_words(text):
	word_list = text.split()
	return len(word_list)

def get_num_characters(text):
	char_count = {}
	for char in text.lower():
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1
	return char_count

def get_output(char_dict):
	char_list = []
	for key,val in char_dict.items():
		char_list.append({"char": key, "num": val})
	char_list.sort(reverse=True, key=lambda x: x["num"])
	return char_list
	

				
