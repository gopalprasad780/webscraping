from bs4 import BeautifulSoup
import requests


url = "https://www.newegg.com/global/in/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+card&N=-1&isNodeId=1"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#For storing all item in div tag having class 'item-container'
containers = soup.findAll("div",{"class":"item-container"})
filename = 'product.csv'
f = open(filename, 'w')

headers = 'brand, product_name, price \n'
f.write(headers)
for container in containers:
    try:
        #extracting brand title from container
        brand =container.div.div.a.img['title']
        # for product name 
        title_container = container.findAll('a',{'class':'item-title'})
        product_name = title_container[0].text

        #product price container
        product_price_container = container.findAll('li',{'class':'price-current'})
        li = product_price_container[0].text

        #filter out price
        for j in range(3):
            for i in ['\n',' ', '–', '\xa0', '\r','\x20','\x0a','\x09','\x0c','\x0d']:
                li=li.strip(i)

        price = li

        print('Product brand :-  ',brand)
        print('product name  :-  ',product_name)
        print('Price         :-  ',price)
        
        f.write(brand.replace(',',' ')+","+ product_name.replace(',','|')+","+ price.replace(',',' ')+"\n")
        
        
    except:
        
        pass
        

f.close()

