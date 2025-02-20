import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

home_url = "https://fermosaplants.com/"
page_url = "https://fermosaplants.com/collections/sansevieria?page={}"


def scrape_page(page_number):
    """
    - scrapes a single page and returns a list of product details.
    - extracts raw html and deduces information about product from it.
    - returns dictionary list with details of products in a single page.
    """
    try:
        target_url = page_url.format(page_number)
        response = requests.get(target_url)
        raw_html = response.text
        soup = BeautifulSoup(raw_html, 'html5lib')
        page_data = []
        for product in soup.find_all("div", class_="product-item-v5"):
            
            title = product.find("h4", class_="title-product")
            product_link = urljoin(home_url, title.find("a")["href"])
            product_title = title.text.strip()
            
            price_tag = product.find("p", class_="price-product")
            product_price = price_tag.text.strip() if price_tag else "N/A"
            
            combo = "combo" in product_title.lower()
            plant_names = extract_product_description(product_link) if combo else ""
            
            extracted_data = {
                "Name": product_title,
                "URL": product_link,
                "Price": product_price,
                "Plants": plant_names,
            }

            page_data.append(extracted_data)
        print(f"Finished scraping page {page_number}.")
        return page_data
    except requests.exceptions.ConnectionError:
        print("Error in connecting to the URL.")


def extract_plant_names(text):
    """
    - extracts plant names from the given text data.
    - sample text to extract plant names: "Scientific Name- Sansevieria  About Combo Offer (A) - Pups of-1. Mini Boncel, 2..."
    - returns a string with plant names in any combo given as 1..,2..,3...
    """
    text = text.split("1.")[-1]
    text = text.split('\n')[0]
    text = text.split('.')
    data = [name.strip().split(',')[0] for name in text]
    data = ', '.join(data)
    return data


def extract_product_description(product_url):
    """
    - scrapes individual product page to extract product description.
    - returns string with plant names.
    """
    source = requests.get(product_url).text
    soup = BeautifulSoup(source, 'html5lib')
    plant_names = []
    for plant in soup.find_all("div", class_="desc product-desc"):  
        extracted_names = extract_plant_names(plant.text.strip())
        plant_names.extend(extracted_names)
    return extracted_names


def process_pages():
    """
    - scrapes multiple pages and returns combined data.
    - returns list with data.
    """
    data = []
    for curr_page in range(1, 8):
        page_data = scrape_page(curr_page)
        data.extend(page_data)
    return data


def to_csv(csv_path, data):
    """dumps data into csv file"""
    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False)
    print(f"Finished writing to {csv_path}")


def to_excel(excel_path, data):
    """dumps data into excel sheet"""
    df = pd.DataFrame(data)
    df.to_excel(excel_path, index=False)
    print(f"Finished writing to {excel_path}")


if __name__ == "__main__":
    scraped_data = process_pages()
    csv_path = "data.csv"
    excel_path = "data.xlsx"
    to_csv(csv_path, scraped_data)
    to_excel(excel_path, scraped_data)