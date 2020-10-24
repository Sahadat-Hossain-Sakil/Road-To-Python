import requests
from bs4 import BeautifulSoup

link = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(link)
soup = BeautifulSoup(r.content, 'html.parser')
print("\n ---FULL ARTICLE IS BELOW--- \n")
for story_line in soup.find_all(class_= "grid--item body body__container article__body grid-layout__content"):
    print(story_line.get_text().replace("\n", " ").strip())