
#### Origin : https://www.topcoder.com/thrive/articles/web-crawler-in-python


import requests
import lxml
from bs4 import BeautifulSoup
from xlwt import *

url = "https://www.manchester.ac.uk/study/international/study-abroad-programmes/study-abroad/course-units/subject-list/"
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
f = requests.get(url, headers = headers)
soup = BeautifulSoup(f.content, 'lxml')

data = soup.select("table tbody tr")


workbook = Workbook(encoding = 'utf-8')
table = workbook.add_sheet('data')
table.write(0, 0, 'Number')
table.write(0, 1, 'Courses')
table.write(0, 2, 'Fall assessment available?')
table.write(0, 3, 'Faculty')
line = 1

tags = [] 
for  x in data :
  tags.extend((i.prettify() for i in x.find_all('td') ) )


####### Write the crawled data to Excel
k = 0
while k <= ( len(tags)//3 ):
    
  table.write(line, 0, line)
  table.write(line, 1, tags[k])
  table.write(line, 2, tags[k+1])
  table.write(line, 3, tags[k+2])
  line += 1
  k = k + 3


workbook.save('courses.xls')


