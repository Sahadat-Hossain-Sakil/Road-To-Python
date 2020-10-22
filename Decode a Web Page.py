import requests
from bs4 import BeautifulSoup

# We can use any weblink for decode, but we must specify the class.
# Here we find all headlines of a newspaper Ex. = ("The Guardian")

link = "https://www.theguardian.com/international" 
r = requests.get(link).text
soup = BeautifulSoup(r, features="html.parser")
print("\n ---HEADLINES ARE BELOW--- \n")
for story_line in soup.find_all(class_="u-faux-block-link__overlay js-headline-text"):
    print(story_line.get_text().replace("\n", " ").strip())