import urllib.request
import re

for i in range(10):
    url_qsbk = 'http://www.qiushibaike.com/text/page/{}/'.format(i) 
    url_agent = 'Chrome/4.0 (compatible; MSIE 5.5; Windows NT)'
    rep = urllib.request.Request(url_qsbk, headers={'User-Agent':url_agent})
    page = urllib.request.urlopen(rep)
    p = page.read().decode('utf-8')
    
    r1 = r'''<div class=\"author clearfix\".*?h2>\n*?(.*?)\n*?</h2>
             <div class="content".*?span>\n+(.*?)\n+</span>'''
    r = re.findall(r1, p, re.S)
    print(r)








