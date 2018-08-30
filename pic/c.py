import re
import urllib.request

url_qsbk = 'https://www.qiushibaike.com/text/page/2/'
url_agent = 'Chrome/4.0 (compatible; MSIE 5.5; Windows NT'
rep = urllib.request.Request(url_qsbk, headers = {'User_Agent':url_agent})
page = urllib.request.urlopen(rep)
p = page.read().decode('utf-8')


r1 = r'<div class=.*?h2>\n*?(.*?)</h2>'
r = re.findall(r1, p, re.S)
print(r)





