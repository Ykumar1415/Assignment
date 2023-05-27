# import requests
# from bs4 import BeautifulSoup

# def scrape_data(num_pages):
#     base_url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{}'

#     product_urls = []
#     product_names = []
#     product_prices = []
#     ratings = []
#     review_counts = []

#     for page in range(1, num_pages + 1):
#         url = base_url.format(page)
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')

#         product_blocks = soup.find_all('div', {'data-component-type': 's-search-result'})
#         for block in product_blocks:
#             product_url = block.find('a', {'class': 'a-link-normal s-no-outline'}).get('href')
#             product_urls.append('https://www.amazon.in' + product_url)

#             product_name = block.find('span', {'class': 'a-size-medium a-color-base a-text-normal'}).text.strip()
#             product_names.append(product_name)

#             product_price = block.find('span', {'class': 'a-offscreen'})
#             if product_price:
#                 product_prices.append(product_price.text)
#             else:
#                 product_prices.append('Not available')

#             rating = block.find('span', {'class': 'a-icon-alt'})
#             if rating:
#                 ratings.append(rating.text.split()[0])
#             else:
#                 ratings.append('Not available')

#             review_count = block.find('span', {'class': 'a-size-base'})
#             if review_count:
#                 review_counts.append(review_count.text)
#             else:
#                 review_counts.append('Not available')

#     return product_urls, product_names, product_prices, ratings, review_counts
import requests
from bs4 import BeautifulSoup

def scrape_data(num_pages):
    base_url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{}'

    urls = []
    names = []
    prices = []
    ratings = []
    review_counts = []

    for page in range(1, num_pages + 1):
        url = base_url.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        product_blocks = soup.find_all('div', {'data-component-type': 's-search-result'})
        for block in product_blocks:
            product_url = block.find('a', {'class': 'a-link-normal s-no-outline'}).get('href')
            urls.append('https://www.amazon.in' + product_url)

            product_name = block.find('span', {'class': 'a-size-medium a-color-base a-text-normal'}).text.strip()
            names.append(product_name)

            product_price = block.find('span', {'class': 'a-offscreen'})
            if product_price:
                prices.append(product_price.text)
            else:
                prices.append('Not available')

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

    return urls, names, prices, ratings, review_counts
