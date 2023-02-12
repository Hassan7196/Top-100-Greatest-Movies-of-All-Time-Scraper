import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")

headings = soup.find_all(name="h3", class_="title")
movies = []

for heading in headings:
    movies.append(heading.getText())

movies.reverse()
print(movies)

with open("movies.txt", mode="w",encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie} \n")







