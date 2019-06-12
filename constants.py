scroll_to_bottom_command = "window.scrollTo(0, document.body.scrollHeight);"
get_html_command = "return document.body.innerHTML"
page_load_time = 0.5 #seconds
collection_class_name = 'cmty-full-cell-link'
url_attribute = 'href'
problem_class_name = 'cmty-view-post-item-text'

aops_contests_url = "https://artofproblemsolving.com/community/c13_contests"
aops_regional_contests_url = "https://artofproblemsolving.com/community/c16_national_and_regional_contests"
contest_discussion_url = "https://artofproblemsolving.com/community/c40244_contest_collections_discussion"

max_problems_per_file = 1000
problem_file_spacing = '\n--------------------------------\n'

punctuation = '.,!:;?()[]{}-*\'\\/><+&_'
stop_words = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", 
              "you", "your", "yours", "yourself", "yourselves", "he", "him", 
			  "his", "himself", "she", "her", "hers", "herself", "it", "its", 
			  "itself", "they", "them", "their", "theirs", "themselves", "what", 
			  "which", "who", "whom", "this", "that", "these", "those", "am", 
			  "is", "are", "was", "were", "be", "been", "being", "have", "has", 
			  "had", "having", "do", "does", "did", "doing", "a", "an", "the", 
			  "and", "but", "if", "or", "because", "as", "until", "while", "of", 
			  "at", "by", "for", "with", "about", "against", "between", "into", 
			  "through", "during", "before", "after", "above", "below", "to", 
			  "from", "up", "down", "in", "out", "on", "off", "over", "under", 
			  "again", "further", "then", "once", "here", "there", "when", "where", 
			  "why", "how", "all", "any", "both", "each", "few", "more", "most", 
			  "other", "some", "such", "no", "nor", "not", "only", "own", "same", 
			  "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", 
			  "should", "now"}
			  
min_prob_length = 10