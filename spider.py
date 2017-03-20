#coding=utf-8


import urllib2
import re
from bs4 import BeautifulSoup


class DataGetModel:

    def get_html_source(self, name, keytype=2):       # get html resource from the specified site
        # example: name = "北京百度网讯科技有限公司"
        url1 = "http://www.beianbeian.com/s?keytype="
        url2 = "&q="
        geturl = url1 + str(keytype) + url2 + name
        request = urllib2.Request(geturl)
        response = urllib2.urlopen(request)
        html = response.read()
        return html

    def get_table_value(self, html):      # get table value from html source code
        bsoup = BeautifulSoup(html, 'html.parser')
        table = bsoup.find('table')
        list_tr = []
        for tr in table.findAll('tr'):
            list_td = []
            count = 0
            for td in tr.findAll('td'):
                temp = re.sub(r"\n\[.*?\]",'',td.getText().strip())
                if temp.encode('utf-8') == "详细信息" or temp.encode('utf-8') == "主办单位名称":
                    continue
                list_td.append(temp)
                count += 1
            if count < 7:
                continue
            list_tr.append(list_td)
        return list_tr

    def get_data(self, list_tr):      # make the specified format
        data_list = []
        for tmp in list_tr:
            column_list = \
                {
                    'No':tmp[0],
                    'Company':tmp[1],
                    'Type':tmp[2],
                    'ICP-No':tmp[3],
                    'Name':tmp[4],
                    'url':tmp[5],
                    'Time':tmp[6]
                }
            data_list.append(column_list)
        return data_list
#
# test = DataGetModel()
#
# table = test.get_table_value(test.get_html_source("北京百度网讯科技有限公司"))
# result = test.get_data(table)
# for a in result:
#     print a['ICP-No']





