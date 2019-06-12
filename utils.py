import constants
import pickle

def dump_problems(problems, file_number):
	print('dumping')
	with open('problems{0}.txt'.format(file_number), 'w', encoding='utf-8') as text_file:
		text_file.write(constants.problem_file_spacing.join(problems))

	with open('problems{0}.txt'.format(file_number), 'wb') as pickle_file:
		pickle.dump(problems, pickle_file)

#removes all substrings between a start_char and finish_char in a string
#	and concatenates them with spaces into their own string.  
def split_substrings(start_char, finish_char, string, substrings=''):
	beg = string.find(start_char)
	
	#if no such substrings in string
	if beg == -1:
		return string, substrings
	
	if start_char == finish_char:
		end = string[beg + len(start_char):].find(finish_char) + beg + len(start_char)
	else:
		end = string.find(finish_char)
	
	#if no such substrings in string
	if end == -1:
		return string, substrings
	
	new_string = string[:beg] + ' ' + string[end + len(finish_char):]
	removed_substring = string[beg + len(start_char):end]
	
	#returns tuple of original string with substrings removed, and the concatenated substrings
	return split_substrings(start_char, finish_char, new_string, substrings + ' ' + removed_substring)

#removes punctuation and makes all characters lower case
def clean_sentence(sentence):
	s = sentence
	for char in constants.punctuation:
		s.replace(char, ' ')
	return s.lower()