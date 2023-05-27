import csv

def save_to_csv(filename, data):
    urls, names, prices, ratings, review_counts, desc, asins, prod_desc, manufacturers = data

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Product URL', 'Product Name', 'Product Price', 'Rating', 'Review Count',
                         'Description', 'ASIN', 'Product Description', 'Manufacturer'])

        for i in range(len(urls)):
            writer.writerow([urls[i], names[i], prices[i], ratings[i], review_counts[i],
                             desc[i], asins[i], prod_desc[i], manufacturers[i]])

    print('Data saved to', filename)
