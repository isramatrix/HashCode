from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class AmazonSpider:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def launch_spider(self):
        pass


text_to_search = 'lg k40'

browser = webdriver.Chrome()
browser.get('https://www.amazon.es/')

search_bar = browser.find_element_by_id('twotabsearchtextbox')
search_bar.send_keys(text_to_search)
search_bar.submit()

# Ya hemos llegado a la página con el listado de productos
list_of_products = browser.find_element_by_css_selector(".sg-col-inner .s-search-results")

list_of_products = list_of_products.find_elements_by_xpath('child::div')

i = 0
for p in list_of_products:
    try:
        p.find_element_by_class_name('s-shopping-adviser')
        p.find_element_by_class_name('s-border-top-overlap')
    except:
        i += 1

print(i)