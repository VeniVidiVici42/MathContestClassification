from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pickle

aops_contests_url = "https://artofproblemsolving.com/community/c13_contests"
aops_regional_contests_url = "https://artofproblemsolving.com/community/c16_national_and_regional_contests"
contest_discussion_url = "https://artofproblemsolving.com/community/c40244_contest_collections_discussion"
chrome_browser = webdriver.Chrome(ChromeDriverManager().install())

def get_html():
	return browser.execute_script("return document.body.innerHTML")

visited_url = {}
visited_url[contest_discussion_url] = True
url_stack = [aops_regional_contests_url, contest_discussion_url]
problems = []
idx = 18

def infiniscroll(browser):
	for i in range(5):
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(0.5)

while len(url_stack) > 0:
	url = url_stack.pop()
	if url in visited_url:
		continue
	print(url)
	visited_url[url] = True
	chrome_browser.get(url)
	infiniscroll(chrome_browser)
	new_collections = chrome_browser.find_elements_by_class_name('cmty-full-cell-link')
	new_urls = [collection.get_attribute('href') for collection in new_collections]
	#print(new_urls)
	if len(new_urls) > 1:
		# more collections
		url_stack = url_stack + new_urls
	else:
		# this is a contest
		contest_problems = chrome_browser.find_elements_by_class_name('cmty-view-post-item-text')
		for contest_problem in contest_problems:
			soup = BeautifulSoup(contest_problem.get_attribute('innerHTML'), 'html.parser')
			for img in soup.findAll('img'):
				img.replace_with(img['alt'])
			problems.append(soup.text)
			#print(soup.text)
			#print()
			#print()
			if len(problems) % 10 == 0:
				f = open('problems{0}pickle'.format(idx), 'wb')
				g = open('problems{0}.txt'.format(idx), 'w', encoding='utf-8')
				g.write('\n---------------\n'.join(problems))
				g.close()
				pickle.dump(problems, f)
				f.close()
				problems = []
				idx = idx + 1

f = open('problems{0}pickle'.format(idx), 'wb')
g = open('problems{0}.txt'.format(idx), 'w', encoding='utf-8')
g.write('\n---------------\n'.join(problems))
g.close()
pickle.dump(problems, f)
f.close()