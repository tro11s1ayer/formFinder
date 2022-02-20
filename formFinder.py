import requests
import sys

from urllib import parse as parse
from bs4 import BeautifulSoup as bs

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"

def find_form(target):
    try:
        rg = requests.get("https://"+target, verify=False, timeout=10, headers={'User-Agent': user_agent})
        print('=======================================================================')
        print(rg.url+'\n'+str(rg))
        print('=======================================================================')
        print(rg.headers)

        page = bs(rg.content.decode(), 'html.parser')
        forms = page.findAll('form')
        for form in forms:
            print(form)
            print('=======================================================================')
            print(str(form.get('name'))+'\n'+str(form.get('method')))
            print('=======================================================================')

    except requests.Timeout as t:
        print('=============================================================================')
        print(t)
        pass
    except requests.ConnectionError as e:
        print('=============================================================================')
        print(e)
        pass
    except requests.TooManyRedirects as r:
        print('=============================================================================')
        print(r)
        pass
    except requests.exceptions.MissingSchema as m:
        print('=============================================================================')
        print(m)
        pass

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            find_form(line.strip())