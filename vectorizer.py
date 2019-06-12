import numpy as np
import constants

#from problem_file_loader import ProblemFileLoader
#from problem import Problem

class Vectorizer:
	def __init__(self, split_problem_array):
		data = []
		for words, latex in split_problem_array:
			if len(words) + len(latex) > constants.min_prob_length:
				data.append((words.split(' '), latex.replace(' ', '')))
		
		word_set = set()
		latex_set = set()
		for words, latex in data:
			for word in words:
				word_set.add(word)
			for char in latex:
				latex_set.add(char)
				
		word_list = list(word_set)
		latex_list = list(latex_set)
		
		num_words = len(word_list)
		num_latex = len(latex_list)
	
		word2idx = {}
		latex2idx = {}
		
		for i in range(len(word_list)):
			word2idx[word_list[i]] = i
		for i in range(len(latex_list)):
			latex2idx[latex_list[i]] = i
		
		self.data = data
		self.num_words = num_words
		self.num_latex = num_latex
		self.word2idx = word2idx
		self.latex2idx = latex2idx
		
	def bag_of_words(self, words):
		v = [0]*self.num_words
		for word in words:
			v[self.word2idx[word]] += 1
		return v
	
	def bag_of_chars(self, latex):
		v = [0]*self.num_latex
		for char in latex:
			v[self.latex2idx[char]] += 1
		return v
	
	def vectorize(self):
		vectorized_data = []
		for words, latex in self.data:
			v = self.bag_of_words(words)
			v.extend(self.bag_of_chars(latex))
			vectorized_data.append(v)
		return np.array(vectorized_data)

'''		
a = ProblemFileLoader('../Problems/problems2.txt').get_problem_array()
b = []
for prob in a:
	b.append(Problem.split_problem(prob))
c = Vectorizer(b)
print(c.num_words)
print(c.num_latex)
d = c.vectorize()
print(d.shape)
'''
			
		