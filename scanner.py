import html
import json
import re

import requests
from bs4 import BeautifulSoup


def scan(eggSummaryPage, textToSearch):
    '''
    Args: website_link = string; link of website to be crawled
            link_class = string; class name for job link on website
    Returns: jobs_link = list; list of jobs 
    '''

    # get content of website and parse it
    website_request = requests.get(eggSummaryPage, timeout=5)
    soup = BeautifulSoup(website_request.content, 'html.parser')

    results = []

    for li in soup.findAll('li'):
        for text in textToSearch:
            matches = li.find(string=re.compile(text))
            if (matches is not None):
                results.append(matches)

    return results


def main():
    results = scan('https://netcup-eier.deployn.de/',
                   ['sdf'])
    print(results)


if __name__ == '__main__':
    main()
