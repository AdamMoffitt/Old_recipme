import urllib2
import cookielib
import re


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

	def print_recipe(self):
		if self.populated:
			outFile = open('temp_name.txt', 'a')
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
				print >> outFile, str(count)+'.', d
				count += 1
			print >> outFile, '\n', self.notes
			outFile.close()


def scrape_site(url_input):
	link = url_input
	hdr = {'User-Agent' : 'Mozilla/5.0', 'Accept': 'text/html,applicatin/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
	req = urllib2.Request(link, headers=hdr)
	url = urllib2.urlopen(req)
	html = url.read()

	outFile = open('recipe_page.txt', 'w')
	print >> outFile, html
	outFile.close()

	return html

def make_recipe(html, url):
	try:
		recipe_title = re.search('(?<=<title>).*?(?=</title>)', html)
		# print recipe_title.group()
		recipe_author = re.findall('Recipe\sby.*?"author">(.*?)</span>', html)
		# print recipe_author[0]
		recipe_description = re.search('(?<=&#34;).*?(?=&#34;)', html)
		# print recipe_description.group()
		recipe_ingredients = re.findall('itemprop="ingredients">(.*?)</span>', html)
		# print recipe_ingredients
		recipe_directions = re.findall('"recipe-directions__list--item">(.*?)</span>', html)
		# print recipe_directions
		# recipe_notes = re.search('(?<=>Cook\'s Note:</span></li>\n<li>).*?(?=</li>)')
		#add the notes part here later notes here later


		return Recipe(recipe_title.group(), recipe_author[0], recipe_description.group(), 
						recipe_ingredients, recipe_directions, 'notes', '', url)
	except urllib2.HTTPError:
		print 'This wedding is horse shit!'
		return Recipe()

def get_recipe_num(link):
	return re.search('(?<=recipe/).*?(?=/)', link).group()


def find_links(q, v, html):
	links = re.findall('(?<=href=")/recipe/[\w|\W]*?(?=")', html)
	for link in links:
		rec = get_recipe_num(link)
		if rec not in v:
			v.add(rec)
			q.enqueue('http://allrecipes.com/'+link)






if __name__ == '__main__':
	starting_url = 'http://allrecipes.com/recipe/242402/greek-lemon-chicken-and-potato-bake/'
	url_queue = Queue()
	visited = set()
	visited.add(get_recipe_num(starting_url))
	url_queue.enqueue(starting_url)
	bad_links = []

	
	while not url_queue.isEmpty():
		url = url_queue.dequeue()
		print url
		try:
			site_html = scrape_site(url)
		except urllib2.HTTPError:
			bad_links.append(url)
		find_links(url_queue, visited, site_html)
		recipe = make_recipe(site_html, url)
		recipe.print_recipe()



