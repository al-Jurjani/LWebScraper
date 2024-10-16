# bismillah
# started project 09-04-1446/13-10-2024
# ended project 12-04-1446/16-10-2024
from bs4 import BeautifulSoup as bs4
import requests
import time
from pathlib import Path

# # Example of making an HTTP request and parsing the HTML content
# url = 'https://example.com'
# response = requests.get(url)

# # Initialize BeautifulSoup with the HTML content and a parser (e.g., 'lxml' or 'html.parser')
# soup = BeautifulSoup(response.content, 'lxml')  # or 'html.parser'

# # Now you can use `soup` to find elements
# print(soup.prettify())

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='
pyjobs = requests.get(url).text
soup = bs4(pyjobs, 'lxml')

print("Print unfamiliar skills.")
unfskill = input('>')
print(f"Filtering out {unfskill}")

def findJobs():
    path = Path('posts/file.txt')
    if path.exists():
        print('Deleting Outdated File!')
        path.unlink()
        time.sleep(10) # just checking if file is actually deleting. it is.

    jobs = soup.findAll('li', class_ = 'clearfix job-bx wht-shd-bx')
    for count, job in enumerate(jobs):
        company = job.find('h3', class_ = 'joblist-comp-name').text.strip()
        skill = job.find('span', class_ = "srp-skills").text.strip()
        if unfskill not in skill:
            info = job.header.h2.a['href']
            posted = job.find('span', class_ = 'sim-posted').text.strip()
            fileWriting(company, skill, info, posted)
            print(f'post #{count} saved!')

def fileWriting(c: str, s: str, i, p: str):
        with open(f'posts/file.txt', 'a') as f:
            f.write(c)
            f.write(s)
            f.write(i)
            f.write(p + "\n")

if __name__ == '__main__':
    while True:
        findJobs()
        print("\n Waiting 10 seconds!")
        time.sleep(10) # 10 seconds