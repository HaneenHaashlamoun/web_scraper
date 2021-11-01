import requests
from bs4 import BeautifulSoup

domain = 'https://en.wikipedia.org/wiki/History_of_Mexico'


def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find_all("span", text="citation needed")
    return (len(result))


def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.find_all('sup', class_='Inline-Template')
    p_citation = []
    for p in result:
        p_citation.append(p.parent.text.strip())
    return '\n'.join(p_citation)
    

print(get_citations_needed_report(domain))
print(get_citations_needed_count(domain))
