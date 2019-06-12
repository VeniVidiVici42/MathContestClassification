import constants
import utils

from problem_file_loader import ProblemFileLoader

class Problem:
	def __init__(self):
		pass
	
	@staticmethod
	def remove_diagrams(problem):
		return utils.split_substrings('[asy]', '[/asy]', problem)[0]
	
	@staticmethod
	def split_latex(problem, latex=''):
		problem, latex = utils.split_substrings('\[', '\]', problem, latex)
		problem, latex = utils.split_substrings('$$', '$$', problem, latex)
		problem, latex = utils.split_substrings('$', '$', problem, latex)
		return problem, latex
	
	@staticmethod
	def split_commands(basic_latex, commands=''):
		beg = basic_latex.find('\\')
		
		#if no such sequences in the problem
		if beg == -1:
			return basic_latex, commands
		
		for end in range(beg + 1, len(basic_latex)):
			if basic_latex[end] in constants.punctuation or basic_latex[end] == ' ':
				break
		
		new_basic_latex = basic_latex[:beg] + ' ' + basic_latex[end:]
		new_command = basic_latex[beg:end]
		
		return Problem.split_commands(new_basic_latex, commands + ' ' + new_command)
	
	#splits problem into words, basic latex, and latex commands
	@staticmethod
	def split_problem(problem):
		problem = Problem.remove_diagrams(problem)
		words, latex = Problem.split_latex(problem)
		words = utils.clean_sentence(words)
		basic_latex, commands = Problem.split_commands(latex)
		return words, basic_latex, commands
	
'''	
a = ProblemFileLoader('../Problems/problems2.txt')
b = a.get_problem_array()[:2]
print(b)
for c in b:
	print(c)
	print(Problem.split_problem(c))
'''
