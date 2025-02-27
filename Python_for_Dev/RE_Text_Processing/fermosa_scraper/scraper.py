'''
Introduction - 
    Fermosa Plants is an online marketplace to purchase various species of plants. 
    Plants are sold individually or as a combo.

Objective - 
    Scraping information from fermosa website including Names, URL, Price, if combo or not and Plant Names if combo.

Components - 
    Class ProductData : to store the product information
    Class PlantScrapper : to implements the scrapper functions
        - make_request() : to make HTTP request
        - extract_plant_names() : extracts individual plant names
        - extract_product_description() : extracts product description to parse plant names
        - scrape_page() : scrapes page and returns product data
        - scrape_all_pages() : scrapes all pages and return combined data
    Class DataExporter : to export data into excel file
        - prepare_df() : converts product data to dataframe
        - to_excel() : dumps data to excel sheet
'''

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd


class ProductData:
    def __init__(self, name, url, price, is_combo, is_variegated, plants):
        self.name = name
        self.url = url
        self.price = price
        self.is_combo = is_combo
        self.is_variegated = is_variegated
        self.plants = plants


class PlantScraper:
    def __init__(self, home_url, page_url, max_pages = 7):
        self.home_url = home_url
        self.page_url = page_url
        self.max_pages = max_pages
    

    def make_request(self, url):
        try:
            response = requests.get(url, timeout=10)
            return response.text
        
        except requests.RequestException as e:
            print(f"Failed to fetch URL: ", str(e))


    def extract_plant_names(self, text):
        try:
            if "1." not in text: return []
    
            #splitting at '1.', splitting again either at line end or at '.' conditionally
            text = text.split("1.")[-1]
            text = text.split('\n')[0].split('.') if '\n' not in text.split('.')[0] else text.split('.')

            #creating strings from alphabetic characters and adding them to a list
            parts = [(''.join([char if char.isalpha() else ' ' for char in part])).strip() for part in text]
            return parts
        
        except Exception as e:
            print("Error extracting plant names from text: ", str(e))


    def extract_plant_list(self, product_url):
        try:
            source = self.make_request(product_url)
            soup = BeautifulSoup(source, 'html.parser')
            plant_names = []
            for plant in soup.find_all("div", class_="desc product-desc"):
                names = self.extract_plant_names(plant.text.strip())
                plant_names.extend(names)
            return plant_names
        
        except Exception as e:
            print("Error extracting product description: ", str(e))


    def scrape_page(self, page_number):
        try:
            target_url = self.page_url.format(page_number)
            raw_html = self.make_request(target_url)
            soup = BeautifulSoup(raw_html, 'html5lib')
            page_data = []

            for product in soup.find_all("div", class_="product-item-v5"):
                try:
                    #extract title and link
                    product_name = product.find("h4", class_="title-product")
                    product_link = urljoin(self.home_url, product_name.find("a")["href"])
                    product_title_txt = product_name.text.strip()
                    
                    #extract price
                    price_tag = product.find("p", class_="price-product")
                    product_price = price_tag.text.strip() if price_tag else ""
                    
                    #determine if product is a combo
                    is_combo = "combo" in product_title_txt.lower()
                    
                    #determine if product variegated or not
                    is_variegated = "Not Eligible" if is_combo else "Yes" if "variegated" in product_title_txt.lower() else "No"

                    #extract plant names if it's a combo
                    plant_names = self.extract_plant_list(product_link) if is_combo else []
                    
                    #create ProductData object
                    product_data = ProductData(
                        name=product_title_txt,
                        url=product_link,
                        price=product_price,
                        is_combo="Yes" if is_combo else "No",
                        is_variegated=is_variegated,
                        plants=plant_names
                    )
                    page_data.append(product_data)
                    
                except Exception as e:
                    print("Error processing product in page: ", str(e))
                    continue

            print(f"Finished scraping page {page_number}")
            return page_data
            
        except Exception as e:
            print("Error scraping page: ", str(e))
            return []


    def scrape_all_pages(self):
        all_data = []
        for curr_page in range(1, self.max_pages + 1):
            try:
                page_data = self.scrape_page(curr_page)
                all_data.extend(page_data)

            except Exception as e:
                print(f"Error processing page: {curr_page}", str(e))
                continue

        return all_data


class DataExporter:
    def prepare_df(data):
        df_data = []

        for product in data:
            row = {
                'Name': product.name,
                'URL': product.url,
                'Price': product.price,
                'Combo': product.is_combo,
                'Variegated':product.is_variegated
            }

            for i, plant in enumerate(product.plants, 1):
                row[f'Plant_{i}'] = plant
            df_data.append(row)

        df = pd.DataFrame(df_data)
        return df


    def to_excel(data, excel_path):
        try:
            df = DataExporter.prepare_df(data)
            df.to_excel(excel_path, index=False)
            print(f"Successfully exported data to {excel_path}")

        except Exception as e:
            print(f"Error exporting to Excel: {str(e)}")
            raise


if __name__ == "__main__":
    home_url = "https://fermosaplants.com/"
    page_url = "https://fermosaplants.com/collections/sansevieria?page={}"

    scraper = PlantScraper(home_url, page_url)
    scraped_data = scraper.scrape_all_pages()
    excel_path = "data.xlsx"
    DataExporter.to_excel(scraped_data, excel_path)