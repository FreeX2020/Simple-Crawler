
#### Origin : https://www.topcoder.com/thrive/articles/web-crawler-in-python

import re
import requests
import lxml
from bs4 import BeautifulSoup
from soupsieve.css_parser import PAT_COMBINE, process_custom
from xlwt import *

url = "https://www.manchester.ac.uk/study/international/study-abroad-programmes/study-abroad/course-units/subject-list/"
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
f = requests.get(url, headers = headers)
soup = BeautifulSoup(f.content, 'lxml')

data = soup.select("table tbody tr")
# print(data)

workbook = Workbook(encoding = 'utf-8')
table = workbook.add_sheet('data')
table.write(0, 0, 'Number')
table.write(0, 1, 'link')
table.write(0, 2, 'Courses')
table.write(0, 3, 'Fall assessment available?')
table.write(0, 4, 'Faculty')
line = 1

tags = [] 
for  x in data : 
    tags.extend(( (i.get('href')) for i in x.find_all('a')))
    tags.extend(( (i.text)for i in x.find_all('td') ))
    

# print(tags)
  

  
  
  
  


####### Write the crawled data to Excel
k = 0
# while k <= ( len(tags)-3 ):
  
#   table.write(line, 0, line)
#   table.write(line, 1, tags[k])
#   table.write(line, 2, tags[k+1])
#   table.write(line, 3, tags[k+2])
#   table.write(line, 4, tags[k+3])
#   line += 1
#   k = k + 4
# workbook.save('courses.xls')


# workbook.save('courses.xls')
print('*******')

j = 0
while j <= len(tags)//4 :
      url  = tags[j]
      headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
      }
      f = requests.get(url, headers = headers)
      soup = BeautifulSoup(f.content, 'lxml')
      j = j + 4
      data = soup.select("div")
      
      tags2 = [] 
      for  x in data : 
        try:
          tags2.extend(( (i.text) for i in x.find_all('p') ))
        except ValueError:
          continue


      # print(tags2)
      k = 0
      while k <= ( len(tags2)-4 ):
        
        table.write(line, 0, line)
        table.write(line, 1, tags2[0])

        # table.write(line, 2, tags2[k+1])
        # table.write(line, 3, tags2[k+2])
        # table.write(line, 4, tags2[k+3])
        line += 1
        k = k + 4
        print( tags2[0])


print(line)     










# driver = webdriver.Firefox(executable_path = '/path/to/geckodriver')
# url2 = "https://www.geeksforgeeks.org/"
# driver.get(url2)

