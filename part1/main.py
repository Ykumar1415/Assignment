import scraping
import save_to_csv

num_pages = 20

urls, names, prices, ratings, review_counts = scraping.scrape_data(num_pages)

filename = 'amazon_products.csv'
save_to_csv.save_to_csv(filename, urls, names, prices, ratings, review_counts)

print('Number of products scraped:', len(urls))
