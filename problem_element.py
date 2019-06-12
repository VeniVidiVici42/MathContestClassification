import constants
from bs4 import BeautifulSoup

class ProblemElement:
	def __init__(self, problem_element):
		self.problem = problem_element

	def get_text(self):
		soup = BeautifulSoup(self.problem.get_attribute('innerHTML'), 'html.parser')
		for img in soup.findAll('img'):
			img.replace_with(img['alt'])
		return soup.text
	
	

