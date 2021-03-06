import requests
from bs4 import BeautifulSoup

# Here we create a .txt file with ' open() ' function and write into it. 
# This algorithm will decode a web page and get all file as text for some specific classes in page HTML or CSS.
# And then write into the .txt file.

link = "https://www.theguardian.com/international"
r = requests.get(link).text
soup = BeautifulSoup(r, features="html.parser")
fielname = input("Enter a filename : ")
with open(fielname, 'w') as d:
    for story in soup.find_all(class_="u-faux-block-link__overlay js-headline-text"):
        if story.a:
           d.write(story.get_text().replace("\n", " ").strip())
        else:
            d.write(story.contents[0].strip())
