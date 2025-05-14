def get_word_count(text_string):
        words = text_string.split()
        return len(words)

def get_letter_counts(text_string):
	letter_dict = {}
	for char in text_string:
		letter = char.lower()
		if letter in letter_dict:
			letter_dict[letter] += 1
		else:
			letter_dict[letter] = 1
	return letter_dict

def sort_on(dict):
	return dict["num"]

def sort_letter_list(char_dict):
	letter_list = []
	for key in char_dict:
		letter_list.append({"char":key,"num":char_dict[key]})
	letter_list.sort(reverse=True, key=sort_on)
	return letter_list

#x = get_letter_counts("This is a test")
#print(sort_letter_list(x))

