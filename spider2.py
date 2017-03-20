#coding=utf-8

import urllib2
import re
from bs4 import BeautifulSoup

#
# this is not useful, just practise
#
name = "北京百度网讯科技有限公司"
url = "http://www.beianbeian.com/s?keytype=2&q="
geturl = url + name
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# headers = { 'User-Agent' : user_agent }
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
content_all = response.read()
# print content_all
json_result = []
pattern_table = "<table id=\"show_table\" class=\"seo\" cellpadding=\"5\" " \
                "cellspacing=\"0\" border=\"1\" bordercolor=\"#BBD7E6\"(.*?)</table>"
pattern_tr = "(<tr>|<tr style=\"background-color: #EEEEEE;\">)(.*?)</tr>"
pattern_td = "(<td><s style=\"color:#CCCCCC;\">|<td style=\"word-break:break-all;" \
             "word-wrap:break-word;\">|<td nowrap=\"nowrap\">|<td>)(.*?)</td>"
list_tr = []


bsoup = BeautifulSoup(content_all, 'html.parser')
table = bsoup.find('table')
for tr in table.findAll('tr'):
    list_td = []
    count = 0
    for td in tr.findAll('td'):
        temp = re.sub(r"\n\[.*?\]",'',td.getText().strip())
        if ( temp.encode('utf-8') == "详细信息" or temp.encode('utf-8') == "主办单位名称"):
            continue
        list_td.append(temp)
        count += 1
    if count < 7 :
        continue
    list_tr.append(list_td)

for a in list_tr:
    print a[0]

