import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import urllib.request as urlrequest
import csv ,codecs
import xlsxwriter
import re

url_original= '这里是你要爬取的网页链接'
paper_title_string ='文章标题'
time_data_num ='出版年份'
paper_keywd_string ='关键词'
paper_num = 0

with open ('wf_papertest3.csv','w',encoding='utf-8') as outputfile:
	writer = csv.writer(outputfile)
	outputfile.write("paper_num#paper_title_string#time_data_num#paper_keywd_string\n")
	for i in range(41,300):
		kv = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
		url = url_original+ str(i)
		resp = urlrequest.Request(url,headers =kv)
		paper_content = urlrequest.urlopen(resp).read()
		paper_html = paper_content.decode('utf-8')
		paper_soup = BeautifulSoup(paper_html,'html.parser')
		paper_title_list = []
		allpaper_list = paper_soup.find_all(class_='record-item')
		re_words = re.compile(u'[\u4e00-\u9fa5]+')
		for paper in allpaper_list:
			paper_data = paper.find(class_='record-title')
			paper_title = paper_data.find('a',class_='title')
			paper_title_str = str(paper_title)
			paper_title_string = re.findall(re_words,paper_title_str)
			paper_keywd = paper.find(class_='record-keyword')
			paper_keywd_str = str(paper_keywd)
			paper_keywd_string = re.findall(re_words,paper_keywd_str)
			time_data_info = paper.find(class_='fulltext')['href']
			time_data = str(time_data_info)
			time_data_num = re.findall('\d+',time_data)
			paper_num = paper_num +1
			outputfile.write('{}#{}#{}#{}\n'.format(paper_num,paper_title_string,time_data_num,paper_keywd_string))

csv = pd.read_csv('wf_papertest3.csv',sep='#',encoding='utf-8')
csv.to_excel('wf_papertest3.xlsx' , sheet_name='data')
