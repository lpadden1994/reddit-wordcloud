from bs4 import BeautifulSoup
import requests

# request to get data from url
url = 'https://www.reddit.com'

# used for user agent, request fails otherwise
headers = {
	'User-Agent': 'My User Agent'
}

req = requests.get(url, headers=headers)

# data from the request
data = req.text

soup = BeautifulSoup(data, "html.parser")

titles_raw = soup.find_all('p', class_='title')
titles = []

# parse the html tags and get clean text titles
for title in titles_raw:
	titles.append(title.text)

# write the titles to a file for use later
with open('redditdata.txt', 'w') as f:
	for title in titles:
		f.write("{}\n".format(title))

