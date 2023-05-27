import requests
from bs4 import BeautifulSoup

def scrape_product_listing(num_pages):

    products_per_page = 10
    total_products = num_pages * products_per_page

    base_url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{}'

    product_urls = []
    product_names = []
    product_prices = []
    ratings = []
    review_counts = []

    for page in range(1, num_pages + 1):
        url = base_url.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        product_blocks = soup.find_all('div', {'data-component-type': 's-search-result'})
        for block in product_blocks:
            product_url = block.find('a', {'class': 'a-link-normal s-no-outline'}).get('href')
            product_urls.append('https://www.amazon.in' + product_url)

            product_name = block.find('span', {'class': 'a-size-medium a-color-base a-text-normal'}).text.strip()
            product_names.append(product_name)

            product_price = block.find('span', {'class': 'a-offscreen'})
            if product_price:
                product_prices.append(product_price.text)
            else:
                product_prices.append('Not available')

            rating = block.find('span', {'class': 'a-icon-alt'})
            if rating:
                ratings.append(rating.text.split()[0])
            else:
                ratings.append('Not available')

            review_count = block.find('span', {'class': 'a-size-base'})
            if review_count:
                review_counts.append(review_count.text)
            else:
                review_counts.append('Not available')

    return product_urls, product_names, product_prices, ratings, review_counts


def scrape_product_details(product_urls):
    descriptions = []
    asin_codes = []
    product_descriptions = []
    manufacturers = []

    for url in product_urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        description_element = soup.find('span', {'id': 'productTitle'})
        description = description_element.text.strip() if description_element else 'Not available'
        descriptions.append(description)

        asin_element = soup.find('th', string='ASIN')
        asin_code = asin_element.find_next('td').text.strip() if asin_element else 'Not available'
        asin_codes.append(asin_code)

        product_description_element = soup.find('div', {'id': 'productDescription'})
        product_description = product_description_element.text.strip() if product_description_element else 'Not available'
        product_descriptions.append(product_description)

        manufacturer_element = soup.find('a', {'id': 'bylineInfo'})
        manufacturer = manufacturer_element.text.strip() if manufacturer_element else 'Not available'
        manufacturers.append(manufacturer)

    return descriptions, asin_codes, product_descriptions, manufacturers
