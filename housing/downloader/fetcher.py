# fetcher.py
"""
This is a file that defines functions fetching urls
"""

from lxml import html
import requests 
import re

def GetRentalPage( root_url, cookie_jar ):
	# Look for href that in <a> that has attribute data-id = 36
	# This will return a link to the main nanaimo rental page
	page = requests.get(root_url, cookies = cookie_jar)
	tree = html.fromstring(page.content)
	for line in tree.xpath('//li/a[@data-id=36]'):
		rental_url = root_url + line.get('href')
	return rental_url

def GetRentalLinks( root_url, page_n ):
	"""
	Takes a AD.content as argument
	"""
	rental_links = []
	for line in page_n.xpath('//div[@class="title"]/a'):
		rental_links.append( root_url + line.get('href') )
		
	return rental_links
	
def GetKijijiAdpage( root_url, rental_url, cookie_jar ):
	# Get all the links in the footer for the page numbers
	ad_page = requests.get(rental_url, cookies = cookie_jar)
	ad_tree = html.fromstring( ad_page.content )
	ad_link_list = []
	for line in ad_tree.xpath('//div[@class="pagination"]/a'):
		ad_link_list.append( root_url + line.get('href') )
	
	# get all 'regular ad links from the rental_url page
	page1_links = GetRentalLinks( root_url, ad_tree )
	
	# remove last rss line
	# we use set to make sure we do not get duplicates
	all_page_links = list( set(ad_link_list[0:-1]) )
	return all_page_links, page1_links
	
def GetAdDetails( link ):
	ad_page = requests.get( link )
	ad_tree = html.fromstring( ad_page.content )
	ad_date = ad_tree.xpath('//th[contains(text(),"Date Listed")]/following-sibling::*')[0].text_content()
	price = ad_tree.xpath('//span[@itemprop="price"]/strong')[0].text_content()
	address = ad_tree.xpath('//th[contains(text(),"Address")]/following-sibling::td[not(self::a)]/text()')[0]
	ad_id_tmp = ad_tree.xpath('//div[@id="Breadcrumb"]/strong')[0].text_content()
	ad_id = re.split("Ad ID ", ad_id_tmp)[-1]
	return ad_date, price, address, ad_id
