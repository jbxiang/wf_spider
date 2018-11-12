# wf_spider
使用python爬取万方数据库的论文
====
需要的库
------
* pandas 
* numpy
* bs4
* urllib.request
* csv,codecs
* xlsxwriter
* re
* random
* os
* time

分析网页
-------
首先打开万方知识库，随便搜索一个关键词，如`'互联网'`，进入搜索结果界面。  
第一步，我们想知道翻页的机制，首先点击第二页，先看网页的url有没有变化，发现由。。。变为。。。，也就是说万方的url的基本构成为：
然后，我们查看网页源代码，看看我们需要的信息在哪里  
最后开始进行爬取

关键代码
--------
反爬
--------
使用`代理`和`限制爬取频率`这两种办法    
proxy = random.choice(proxy_list)  
time.sleep(3)
效果
--------
