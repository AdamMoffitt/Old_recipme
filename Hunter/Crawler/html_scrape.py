import urllib2
import cookielib
import re
from pymongo import MongoClient


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Recipe:
	def __init__(self, *args):
		if len(args) > 0:
			self.title = args[0]
			self.author = args[1]
			self.description = args[2]
			#the following are all lists
			self.ingredients = args[3]
			self.directions = args[4]
			self.notes = args[5]
			self.image = args[6]
			self.populated = True
			self.url = args[7]
		else:
			self.title = ''
			self.author = ''
			self.description = ''
			#the following are all lists
			self.ingredients = ''
			self.directions = ''
			self.notes = ''
			self.image = ''
			self.populated = False

	def print_to_file(self):
		if self.populated:
			outFile = open('list_of_recipes.txt', 'a')
			print >> outFile, 'Title:', self.title
			print >> outFile, 'By:', self.author+'\n'
			print >> outFile, '"'+self.description+'"'+'\n'
			count = 1
			print >> outFile, 'Ingredients:'
			for i in self.ingredients:
				print >> outFile, str(count)+'.', i
				count += 1
			print >> outFile, '\nDirections:'
			count = 1
			for d in self.directions:
				print >> outFile, str(count)+'.', d,'\n'
				count += 1
			#print >> outFile, '\n', self.notes
			outFile.close()

	def write_to_db(self, db):
		# ingr = set(self.ingredients)
		# directions = set(self.directions)
		doc = {
			'Title': self.title,
			'Author': self.author,
			'Description': self.description,
			'Ingredients': [x for x in self.ingredients ],
			'Directions': [x for x in self.directions ]
		}
		db.first_try.insert_one(doc)



def scrape_site(url_input):
	link = url_input
	hdr = {'User-Agent' : 'Mozilla/5.0', 'Accept': 'text/html,applicatin/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
	req = urllib2.Request(link, headers=hdr)
	url = urllib2.urlopen(req)
	html = url.read()

	# outFile = open('recipe_page.txt', 'w')
	# print >> outFile, html
	# outFile.close()

	return html


def make_recipe(html, url):
	try:
		recipe_title = re.search('(?<=<title>).*?(?=</title>)', html)
		# print recipe_title.group()
		recipe_author = re.findall('Recipe\sby.*?"author">([\s|\S]*?)</span>', html)
		# print recipe_author[0]
		recipe_description = re.search('(?<=&#34;)[\s|\S]*?(?=&#34;)', html)
		# print recipe_description.group()
		recipe_ingredients = re.findall('itemprop="ingredients">([\s|\S]*?)</span>', html)
		# print recipe_ingredients
		recipe_directions = re.findall('"recipe-directions__list--item">([\s|\S]*?)</span>', html)
		# print recipe_directions
		#recipe_notes_block = re.search('(?<=<section class="recipe-footnotes">)[\s|\S]*?(?=</section>)')
		#add the notes part here later notes here later

		args = [recipe_title.group(), recipe_author[0], recipe_description.group(), recipe_ingredients, recipe_directions]
		for arg in args:
			if type(arg) is not list:
				arg = arg.replace('\n', '')
			else:
				for second_arg in arg:
					second_arg = second_arg.replace('\n', '')
		return Recipe(recipe_title.group(), recipe_author[0], recipe_description.group(), 
					recipe_ingredients, recipe_directions, 'notes', '', url)
	except urllib2.HTTPError:
		print 'This wedding is horse shit!'
		return Recipe()

def get_recipe_num(link):
	if link[:6] == 'http://': link = link.lstrip('http://allrecipes.com')
	return re.search('(?<=recipe/).*?(?=/)', link).group()


def find_links(q, v, html):
	links = re.findall('(?<=href=")/recipe/[\w|\W]*?(?=")', html)
	for link in links:
		rec = get_recipe_num(link)
		if rec not in v:
			v.add(rec)
			q.enqueue('http://allrecipes.com'+link)






if __name__ == '__main__':
	#clears this
	# open('temp_name.txt', 'w').close()
	#v_file = open('visited.txt', 'r')

	client = MongoClient('mongodb://localhost/27017')
	db = client.recipes
	collection = 'first_try'

	starting_url = 'http://allrecipes.com/recipe/241607/vietnamese-grilled-lemongrass-chicken/'
	url_queue = Queue()
	url_queue.enqueue(starting_url)
	bad_links = []

	visited = set()
	# for recipe_id in v_file:
	# 	visited.add(recipe_id)
	if get_recipe_num(starting_url) not in visited: 
		visited.add(get_recipe_num(starting_url))
	else:
		print "You've already used this one"
	# v_file.close()

	# max_times = 10	
	curr = 1
	while not url_queue.isEmpty():
		url = url_queue.dequeue()
		print str(curr)+':', url
		try:
			site_html = scrape_site(url)
		except urllib2.HTTPError:
			bad_links.append(url)
			print '^ bad'
		# outFile = open('visited.txt', 'a')
		# print >> outFile, get_recipe_num(url)
		# outFile.close()

		find_links(url_queue, visited, site_html)
		recipe = make_recipe(site_html, url)
		recipe.write_to_db(db)
		curr += 1
		# if curr > max_times: break









