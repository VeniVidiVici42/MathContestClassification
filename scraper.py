from chrome_browser import ChromeBrowser
import constants
import utils

chrome_browser = ChromeBrowser()

is_url_visited = {}
is_url_visited[constants.contest_discussion_url] = True
url_stack = [constants.aops_regional_contests_url, constants.contest_discussion_url]
problems = []
file_number = 1

while len(url_stack) > 0:
	# Retrieve a URL and update visited map accordingly
	url = url_stack.pop()
	if url in is_url_visited:
		continue
	print(url)
	is_url_visited[url] = True

	chrome_browser.open_url(url)

	# Elements are dynamically loaded on scroll, so scroll through the entire page to make sure we get everything
	chrome_browser.infiniscroll()

	# If URL points to a collection of contests (and/or other collections), get them all
	new_collections = chrome_browser.get_collections()
	new_urls = chrome_browser.get_collection_urls()

	if len(new_urls) > 1:
		# More collections to visit later
		url_stack = url_stack + new_urls
	else:
		# This is a contest page; collect the problems instead
		contest_problems = chrome_browser.get_problems()
		for contest_problem in contest_problems:
			problems.append(contest_problem.get_text())

			# Weird things can happen if we store too many problems at once (memory issues?). Dump them occasionally.
			if len(problems) % constants.max_problems_per_file == 0:
				utils.dump_problems(problems, file_number)
				problems = []
				file_number = file_number + 1

#one last dump is necessary
utils.dump_problems(problems, file_number)