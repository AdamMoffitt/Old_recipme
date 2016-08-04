from pymongo import MongoClient
import pprint

#####################################################################Just format each recipe in BSON then its super easy

def create_document(l):
	doc = {
		"Title": l[0].rstrip(),
		"Author": l[1].rstrip()

	}
	return doc


if __name__ == '__main__':
	client = MongoClient('mongodb://localhost/27017')
	db = client.recipes

	inFile = open('first_recipes.txt', 'r')

	first_line = True
	list_of_lines = []
	for line in inFile:
		# print line[:5]
		if first_line:
			list_of_lines.append(line)
			first_line = False
		else:
			if line[:5] != 'Title':
				list_of_lines.append(line)
			else:
				x = create_document(list_of_lines)
				db.first_try.insert_one(x)

				del list_of_lines[:]
				list_of_lines.append(line)

