import constants

class CollectionElement:
	def __init__(self, collection_element):
		self.collection= collection_element

	def get_url(self):
		return self.collection.get_attribute(constants.url_attribute)