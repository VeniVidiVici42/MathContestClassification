import constants

class ProblemFileCleaner:

	def __init__(self, path):
		problem_array = []
		
		with open(path) as f:
			lines = f.readlines()
		
		#Combine each problem between the problem dividers into one line
		problem = ''
		for line in lines:
			if line[:3] != '---':
				problem += line.replace('\n', ' ')
			else:
				problem_array.append(problem)
				problem = ''
		
		self.problem_array = problem_array
	
	def get_problem_array(self):
		return self.problem_array
	
	#removes all sequences between a start_char and finish_char in the problem
	#	and puts them in their own string
	def isolate_sequences(self, start_char, finish_char, problem, sequences=''):
		beg = problem.find(start_char)
		
		#if no such sequences in the problem
		if beg == -1:
			return problem, sequences
		
		if start_char == finish_char:
			end = problem[beg + len(start_char):].find(finish_char) + beg + len(start_char)
		else:
			end = problem.find(finish_char)
		
		new_problem = problem[:beg] + ' ' + problem[end + len(finish_char):]
		new_sequence = problem[beg + len(start_char):end]
		
		return self.isolate_sequences(start_char, finish_char, new_problem, sequences + ' ' + new_sequence)
	
	def remove_diagrams(self, problem):
		return self.isolate_sequences('[asy]', '[/asy]', problem)[0]
	
	def isolate_latex(self, problem, latex=''):
		problem, latex = self.isolate_sequences('\[', '\]', problem, latex)
		problem, latex = self.isolate_sequences('$$', '$$', problem, latex)
		problem, latex = self.isolate_sequences('$', '$', problem, latex)
		return problem, latex
	
	def clean_sentence(self, sentence):
		s = sentence
		for char in constants.punctuation:
			s.replace(char, ' ')
		return s.lower()
		
	def isolate_commands(self, basic_latex, commands=''):
		beg = basic_latex.find('\\')
		
		#if no such sequences in the problem
		if beg == -1:
			return basic_latex, commands
		
		for end in range(beg + 1, len(basic_latex)):
			if basic_latex[end] in constants.punctuation or basic_latex[end] == ' ':
				break
		
		new_basic_latex = basic_latex[:beg] + ' ' + basic_latex[end:]
		new_command = basic_latex[beg:end]
		#print(new_basic_latex)
		
		return self.isolate_commands(new_basic_latex, commands + ' ' + new_command)
	
	def parse_problem(self, problem):
		problem = self.remove_diagrams(problem)
		words, latex = self.isolate_latex(problem)
		words = self.clean_sentence(words)
		basic_latex, commands = self.isolate_commands(latex)
		return words, basic_latex, commands
		
		

			