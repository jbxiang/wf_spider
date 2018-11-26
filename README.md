
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
![](https://github.com/jbxiang/pictures_wf/raw/wf_results_page.JPG)  
可以看到这个页面包含我们想要获取的所有信息：作者、题目、关键字。  
第一步，我们想知道翻页的机制，首先点击第二页，先看网页的url有没有变化，发现由```http://s.wanfangdata.com.cn/Paper.aspx?q=%E4%BA%92%E8%81%94%E7%BD%91&f=top&p=```变为```http://s.wanfangdata.com.cn/Paper.aspx?q=%E4%BA%92%E8%81%94%E7%BD%91&f=top&p=2```，也就是说万方的url的翻页机制的关键是p='num',这个num就是对应的页码。  
了解了翻页机制后，我们就可以查看网页源代码，看看我们需要的信息在哪里：  
![](https://github.com/jbxiang/pictures_wf/blob/master/wf_url_info.JPG)
最后开始进行爬取

关键代码
--------  
BS
爬取
速度限制
数量限制
正则表达式



反爬
--------
使用`代理`和`限制爬取频率`这两种办法    
proxy = random.choice(proxy_list)// Python  
time.sleep(3)

效果
--------
