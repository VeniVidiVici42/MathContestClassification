from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from collection_element import CollectionElement
from problem_element import ProblemElement
import constants
import time

class ChromeBrowser:
	def __init__(self):
		self.browser = webdriver.Chrome(ChromeDriverManager().install())

	def open_url(self, url):
		self.url = url
		self.browser.get(url)

	def infiniscroll(self, scrolls=20):
		for i in range(scrolls):
			self.browser.execute_script(constants.scroll_to_bottom_command)
			time.sleep(constants.page_load_time)

	def get_collections(self):
		return [CollectionElement(collection) for collection in self.browser.find_elements_by_class_name(constants.collection_class_name)]

	def get_collection_urls(self):
		collections = self.get_collections()
		return [collection.get_url() for collection in collections]

	def get_problems(self):
		return [ProblemElement(problem) for problem in self.browser.find_elements_by_class_name(constants.problem_class_name)]

	def get_html(self):
		return self.browser.execute_script(constants.get_html_command)