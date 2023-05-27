# import csv

# def save_to_csv(filename, product_urls, product_names, product_prices, ratings, review_counts):
#     with open(filename, 'w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Product URL', 'Product Name', 'Product Price', 'Rating', 'Review Count'])

#         for i in range(len(product_urls)):
#             writer.writerow([product_urls[i], product_names[i], product_prices[i], ratings[i], review_counts[i]])

#     print('Data saved to', filename)
import csv

def save_to_csv(filename, urls, names, prices, ratings, review_counts):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Product URL', 'Product Name', 'Product Price', 'Rating', 'Review Count'])

        for i in range(len(urls)):
            writer.writerow([urls[i], names[i], prices[i], ratings[i], review_counts[i]])

    print('Data saved to', filename)
