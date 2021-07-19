import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get(
    'https://news.ycombinator.com/')

# grap html elements
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def creatge_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            print(points)
        print(hn.append({'title': title, 'href': href}))
    return hn


print(creatge_custom_hn(links, subtext))
