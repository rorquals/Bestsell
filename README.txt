1. enviroment
Python 2.7 + Scrapy + BeautifulSoup4

2. how to run the code
>scrapy crawl apple

3. where is the result
bestsell.csv

4. problem solved
  a. blank space format problem
    using tab and using space sheet are difference.

  b. write item to excel encode problem
    the python 2.7 has encode problem. ASCII/utf-8 should be clearly encode decode.

  c. check format in yahoo web
    using InfoLite can easily get the information

  d. regular expression
    like compiler, using regular expression to describe the rule


5. file description
  a. items.py
	list all items' names

  b. pipelines.py
	write item into excel/csv files

  c. crawler.py
	spider body, keep trace items in the pages

6. some bug still exist...