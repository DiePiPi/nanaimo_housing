# scraping Kijiji
# first use curl from bash to download nanaimo kijiji cookie
# You must delete whole file and keep only the cookie section
# login~$ curl -c - 'http://www.kijiji.ca/b-nanaimo/l1700263' > kijiji.cookie

from lxml import html
import requests, cookielib
from fetcher import *

cookie_jar = cookielib.MozillaCookieJar('kijiji.cookie')
cookie_jar.load()

root_url = 'http://www.kijiji.ca'

# main page for Nanaimo rentals
rental_url = GetRentalPage(root_url,cookie_jar)

# Get all links to other pages for nanaimo rentals
# Plus, get the ad links available on the first page
pages_url, ad_url = GetKijijiAdpage(root_url, rental_url, cookie_jar)

for page in pages_url:
	ad_page = requests.get( page )
	ad_tree = html.fromstring(ad_page.content)
	ad_url = ad_url + GetRentalLinks( root_url, ad_tree )



for rental in ad_url:
	ad_date, price, address, ad_id = GetAdDetails( rental )
	print [ad_date,price,address,ad_id]

	


	
