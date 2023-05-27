import scraping as sp
import csv_utils as cu

num_pages = 20

product_urls, product_names, product_prices, ratings, review_counts = sp.scrape_product_listing(num_pages)

descriptions, asins, product_descs, manufacturers = sp.scrape_product_details(product_urls)

data = (product_urls, product_names, product_prices, ratings, review_counts,
        descriptions, asins, product_descs, manufacturers)

filename = 'amazon_products_extended.csv'
cu.save_to_csv(filename, data)
