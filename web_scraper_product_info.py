import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#works for newegg.com website
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

uClient = uReq(my_url)  #requests all the data from my_url
page_html = uClient.read()  #pastes all the raw html in a variable
uClient.close()   #since it is opened client close it 


page_soup = soup(page_html, "html.parser")

 
containers = page_soup.findAll("div", {"class":"item-container"}) 


filename = "products.csv"   
f=open(filename, "w")
headers = "brand, product_name, shipping, price\n"

f.write(headers)

for container in containers:
	

	title_container = container.findAll("a", {"class":"item-title"}) 
	product_name = title_container[0].text   #title

	try:
		brand = container.div.div.a.img["title"]   
	except:
		brand = product_name.split(' ')[0]


	shipping_container = container.findAll('li', {"class":"price-ship"})  
	shipping = shipping_container[0].text.strip()  #remove whitespace char

	if shipping == '':
		shipping = 'Info not available'

	price_container = container.findAll("li", {"class":"price-current"})
	price_list = price_container[0].text.split()

	if price_list[0] == '|':
		price = price_list[1]
	else:
		price = price_list[0]


	print("brand:" + brand)
	print("product name:" + product_name)
	print("shipping:" + shipping)
	print("price:"+ price)

	f.write(brand + "," + product_name.replace(",","|") + ", "+ shipping + "," + price + "\n")

f.close()
