"""Uses the requests library to print hello world from the web."""

# You want to label your code with a version never 
__version__ = '0.1.0'

import requests
import re

URL = 'https://en.wikipedia.org/wiki/"Hello,_world!"_program'

def do_hello():
    result = requests.get(URL)
    print(re.findall('<title>(.*?)</title>', result.text)[0])

if __name__ == '__main__':
    do_hello()