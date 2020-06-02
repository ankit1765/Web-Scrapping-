import requests
from bs4 import BeautifulSoup

page =requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
print(page.status_code) ### Code 200 prints if the request is successful
                        ### Codes starting with 4 or 5 is a failure

# > print(page.content)    ### Code to print the contents of the page.

soup = BeautifulSoup(page.content, 'html.parser')

# > print(soup.prettify())   ### Print the content properly

outertext_tags = soup.find_all('p', class_='outer-text')  ### All the p tags with outer-text class label.

print(outertext_tags) ### Print p tags with outer-text class label.

id_first_tags = soup.find_all(id="first") ### All the tags with first ID label.

print(id_first_tags) ### Print tags with first ID label.

# > list(soup.children)  ### Creates a list of children of main file.

# > html = list(soup.children)[2]  ### This puts all HTML style (found in index 2) code into "html"

# > list(html.children) ### This puts all tags under <html> in a list

# > body = list(html.children)[3] ### This puts all code in body (found in index 3) into "body"

# > list(body.children) ### This puts all tags under <body> in a list

# > p = list(body.children)[1]  ### Isolating the p tag

# > print(p.get_text()) ### Print the content in the p tag and using .get_text

# > soup.find_all('p') ### Creates list of all the p tags

# > print(soup.find_all('p')[0].get_text()) ### prints the first thing in the list of p's

# > soup.find ('p') ### this finds first instance of p

###Using CSS Selectors

soup.select("div p") # The returns all p tags inside of div







