import constants
from bs4 import BeautifulSoup

class Problem:
	def __init__(self, problem):
		self.problem = problem

	def get_text(self):
		soup = BeautifulSoup(self.problem.get_attribute('innerHTML'), 'html.parser')
		for img in soup.findAll('img'):
			img.replace_with(img['alt'])
		return soup.text

