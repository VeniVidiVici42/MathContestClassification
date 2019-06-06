import constants
import pickle

def dump_problems(problems, file_number):
	print('dumping')
	with open('problems{0}.txt'.format(file_number), 'w', encoding='utf-8') as text_file:
		text_file.write(constants.problem_file_spacing.join(problems))

	with open('problems{0}.txt'.format(file_number), 'wb') as pickle_file:
		pickle.dump(problems, pickle_file)