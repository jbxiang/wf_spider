
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
首先打开万方知识库，随便搜索一个关键词，如`互联网`，进入搜索结果界面:
![](https://github.com/jbxiang/pictures_wf/blob/master/wf_results_page.JPG)  
可以看到这个页面包含我们想要获取的所有信息：作者、题目、关键字。    第一步，我们想知道翻页的机制，首先点击第二页，先看网页的url有没有变化，发现由```http://s.wanfangdata.com.cn/Paper.aspx?q=%E4%BA%92%E8%81%94%E7%BD%91&f=top&p=```变为```http://s.wanfangdata.com.cn/Paper.aspx?q=%E4%BA%92%E8%81%94%E7%BD%91&f=top&p=2```，也就是说万方的url的翻页机制的关键是p='num',这个num就是对应的页码。  
了解了翻页机制后，我们就可以查看网页源代码，看看我们需要的信息在哪里：  
![](https://github.com/jbxiang/pictures_wf/blob/master/wf_url_info.JPG)

在知道了以上信息后就可以编写爬取的代码了。

关键代码
--------  
## 发送请求  
```Python
        head = random.choice(user_agents) //随机选择user_agents
				kv = {'User-Agent':head}
				url = url_original+ str(i)
				resp = urlrequest.Request(url,headers =kv)
				urlrequest.install_opener(opener)
				paper_content = urlrequest.urlopen(resp).read()
```
## BS
然后使用BeautifulSoup对网页进行解析：  
```Python
        paper_html = paper_content.decode('utf-8')
				paper_soup = BeautifulSoup(paper_html,'html.parser')
				paper_title_list = []
```
## 爬取
```Python
		for paper in allpaper_list:
					paper_data = paper.find(class_='record-title')
					paper_title = paper_data.find('a',class_='title')
					paper_title_str = str(paper_title)
					paper_title_string = re.findall(re_words,paper_title_str)
```
使用中间一段爬取title的过程为例，发现源代码中的标题放在```<record-title>```下的```<title>```标签下，于是采取find方法提取内容。  

反爬
--------
使用`代理`和`限制爬取频率`这两种办法    
```Python proxy = random.choice(proxy_list) ```构建一个代理池，每次爬取时随即使用一个ip，防止被反爬。
```Python time.sleep(3) ```每一次爬取时可以限制速率，每爬取一次暂停3秒钟，如果想获得更好的伪装，可以使用随机数暂停时间。

效果
--------
![](https://github.com/jbxiang/pictures_wf/blob/master/results.JPG)
