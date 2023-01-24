import re
import urllib.request
import urllib.parse

agent = {'User-Agent':
         "Mozilla/4.0 (\
compatible;\
MSIE 6.0;\
Windows NT 5.1;\
SV1;\
.NET CLR 1.1.4322;\
.NET CLR 2.0.50727;\
.NET CLR 3.0.04506.30\
)"}


link = f'https://github.com/darkprinx/break-the-ice-with-python'
request = urllib.request.Request(link, headers=agent)
raw_data = urllib.request.urlopen(request).read()
data = raw_data.decode("utf-8")
links_expr = r'<li>\n(?:.*href=\")(.*?)(?:\".*)\n<\/li>'
days_expr = r'title=\"(?:Day.)(.*?)\D'
links = re.findall(links_expr, data)
days = re.findall(days_expr, data)
li = dict(zip(days, links))
for date, link in li.items():
    print(date, link)



