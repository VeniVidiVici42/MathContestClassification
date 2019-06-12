import constants

class ProblemFileLoader:

	def __init__(self, path):
		problem_array = []
		
		with open(path) as f:
			lines = f.readlines()
		
		#Combine each problem between the problem dividers into one line
		problem = ''
		for line in lines:
			if line[:3] != '---':#line != constants.problem_file_spacing:
				problem += line.replace('\n', ' ')
			else:
				problem_array.append(problem)
				problem = ''
		
		self.problem_array = problem_array
	
	def get_problem_array(self):
		return self.problem_array
	
	
	
	
		
		

			