import constants

class Collection:
	def __init__(self, collection):
		self.collection = collection

	def get_url(self):
		return self.collection.get_attribute(constants.url_attribute)