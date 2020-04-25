# import the request module from urllib library.
from urllib import request
# This one has handy tools for scraping a web page.
from bs4 import BeautifulSoup
# If you want to dump data to json file.
import json
# If you want to save to CSV.
import csv

# URL (address) of the desired page.
# sample_url = 'https://AlanSimpson.me/python/sample.html'

''' below url causes an error.The “error” isn’t with your coding. Rather, it’s an HTTP error.
Many big sites reject attempts to access their content programmatically, in part to protect
their rights to their own content, and in part to have some control over the incoming traffic.'''
# sample_url = 'https://www.google.com/search?q=python%20web%20scraping%20tutorial'

# Sample page for practice.
sample_url = 'https://alansimpson.me/python/scrape_sample.html'
# Request the page and put it in a variables named the page.
req_page = request.urlopen(sample_url)

# Make a BeautifulSoup object from the html page. You’ll also have to tell BeautifulSoup
# how you want the page parsed. (html5lib)
soup = BeautifulSoup(req_page, 'html5lib')

# Isolate the main content block.
content = soup.article
# print(content)
# Create an empty list for dictionary items.
links_list = []
# Loop through all the links in the article.
# print(content.find_all('a'))
for link in content.find_all('a'):
    # Try to get the href, image url, and text.
    try:
        url = link.get('href')
        img = link.img.get('src')
        text = link.span.text
        links_list.append({'url' : url, 'img': img, 'text': text})
    # If the row is missing anything...
    except AttributeError:
        #... skip it, don't blow up.
        pass

print(len(links_list))
print(links_list)

# Save links in a JSON file.
with open('links.json', 'w', encoding='utf-8') as links_file:
   json.dump(links_list, links_file, ensure_ascii=False) 
   
# Save it to a CSV.
with open('links.csv', 'w', newline='') as csv_out:
    csv_writer = csv.writer(csv_out)
    # Create the header row
    csv_writer.writerow(['url','img','text'])
    for row in links_list:
        csv_writer.writerow([str(row['url']),str(row['img']),str(row['text'])])


# Put the response code in a variable named status.
status = req_page.code
# What is the data type of the page?
print(type(req_page))
# What is the status code?
print(status)
# help(BeautifulSoup)