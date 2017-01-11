# IPython log file

import cython
help(cython)
import urllib.request as req
get_ipython().system('pip install bs4')
from bs4 import BeautifulSoup
get_ipython().magic('logstart')
url = ''
def makeSoup(url):
    with req.urlopen(url)
def makeSoup(url):
    with req.urlopen(url) as html:
        soup = BeautifulSoup(html)
        
url = 'https://pypi.python.org/pypi/Markdown'
makeSoup(url)
def makeSoup(url):
    with req.urlopen(url) as html:
        soup = BeautifulSoup(html, 'lxml')
        
makeSoup(url)
get_ipython().system('pip install lxml')
makeSoup(url)
exit()
