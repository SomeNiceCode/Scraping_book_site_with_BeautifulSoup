import requests
import lxml
from bs4 import BeautifulSoup
from time import sleep

# Base URL used to construct absolute links from relative paths
base_url = "https://books.toscrape.com/catalogue/"

# HTTP headers to mimic a real browser request
headers = {"User-Agent": "Chrome/120.0.0.0 Safari/537.36", "Accept-Language": "en-US,en;q=0.9",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Connection": "keep-alive"}

"""  
    def download_img(url)
    Downloads an image from a given URL and saves it to a local directory.
    Note: Uses absolute pathing for the Windows Desktop.
"""

def download_img(url):

    response = requests.get(url, stream = True)
    r = open("C:\\Users\\momen\\Desktop\\our_img\\" + url.split("/")[-1], "wb")
    for value in response.iter_content(1024*1024):
        r.write(value)
    r.close()



"""
    def get_url(url)
    Iterates through the first two pages of the book catalogue 
    and yields the absolute URL for each individual book page.
"""

def get_url():

    for count in range(1, 3):

        books_url = f"https://books.toscrape.com/catalogue/page-{count}.html"

        response = requests.get(books_url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

        for item in data:
            get_url = item.find("h3").find("a").get("href")
            final_url = base_url + get_url
            yield final_url


"""
    def array()
    Main generator: Visits each book page, extracts details, 
    triggers image download, and yields book information.
"""

def array():
    for item_url in get_url():
        response = requests.get(item_url, headers=headers)
        sleep(2)
        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find("article", class_="product_page")

        description = data.find("div", id="product_description").find_next_sibling("p").text.strip()
        name = data.find("div", class_="col-sm-6 product_main").find("h1").text.strip()
        price = data.find("p", class_="price_color").text.replace("Â", "").strip()

        img_url = data.find("div", class_="item active").find("img").get("src")
        img_final_url = (base_url + img_url).replace("/catalogue/../..", "")
        final_book_url = item_url

        download_img(img_final_url)

        yield name, description, price, img_final_url, final_book_url


