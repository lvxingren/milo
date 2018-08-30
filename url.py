import urllib.request     #
url_qsbk = 'https://www.qiushubaike.com/'
url_python = 'http://www.python.org'

url_agent = 'Chrome/4.0 (compatible; MSIE 5.5; Windows NT)'
rep = urllib.request.Request(url_qsbk, headers={'User-Agent':url_agent})
page = urllib.request.urlopen(rep)
print(page.read().decode(utf-8))

