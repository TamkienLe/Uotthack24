import requests
from bs4 import BeautifulSoup
import warnings
from urllib3.exceptions import InsecureRequestWarning



# URL of the page you want to scrape
url = "https://thegoodshoppingguide.com/subject/ethical-fashion-retailers/"

# Fetch the content from the URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


elements_with_class = soup.find_all(class_="mr-1 pl-3 text-xs lg:text-xl xl:text-2xl font-normal mx-1 md:ml-3 ls:ml-3 md:mr-1 ls:mr-1 py-2.5 md:py-3 xl:py-4")
scores_with_class = soup.find_all('div', class_="rating__index")

# Loop through the found elements and print their text content
for i in range(len(elements_with_class)):
    print(elements_with_class[i].text + ": " + scores_with_class[i].text.strip())
