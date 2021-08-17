import requests
from bs4 import BeautifulSoup

domain ='https://en.wikipedia.org'
History_of_Mexico_url = f'{domain}/wiki/History_of_Mexico'

def get_citations_needed_count(url):
    response = requests.get(url)
    html_text_content = response.text
    soup = BeautifulSoup(html_text_content, 'html.parser')
    result = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    return len(result)

# print(get_citations_needed_count(History_of_Mexico_url))


def get_citations_needed_report(url):
    response = requests.get(url)
    html_text_content = response.text
    soup = BeautifulSoup(html_text_content, 'html.parser')
    result = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    string = ''
    for passage in result:
        string+= f'Citation needed for "{passage.parent.text}"'
    return string  
    
print(get_citations_needed_report(History_of_Mexico_url))    


