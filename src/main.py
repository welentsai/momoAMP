# coding=UTF-8

import requests
import json
import codecs
from bs4 import BeautifulSoup, Tag

from momoItm import MomoItm
from momoItmTag import ItmTag

# Momo 一般商品 HTML Template
html_doc = """
<!DOCTYPE html>
<html ⚡ lang="en">
<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1">

	<link rel="canonical" href="/article.html">

	<title>Momo AMP</title>

	<style amp-boilerplate>body{-webkit-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}@-webkit-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-moz-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-ms-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-o-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}</style><noscript><style amp-boilerplate>body{-webkit-animation:none;-moz-animation:none;-ms-animation:none;animation:none}</style></noscript>
	<style amp-custom>
		body {
			background-color: #eee;
			margin: 0 auto;
			display: block;
		}
		ul {
			list-style: none;
			margin:0px;
			padding:0px;
			display: block;
			margin-block-start: 1em;
			margin-block-end: 1em;
			margin-inline-start: 0px;
			margin-inline-end: 0px;
			padding-inline-start: 0px;
		}
		
		li {	
			display: list-item;
			text-align: -webkit-match-parent;
		}
		
		a {
			text-decoration: none;
			cursor: pointer;
		}

		.prdListArea {
			background-color: transparent;
			margin: 0px auto;
			border: 0px;
			max-width: 640px;
		}
		
		p {
			display: block;
			margin-block-start: 1em;
			margin-block-end: 1em;
			margin-inline-start: 0px;
			margin-inline-end: 0px;
		}
		
		.prdListArea ul li {
			float: left;
			width: 50%;
			margin: 0px 0px 10px;
			position: relative;
			padding: 0px;
			list-style: none;
		}

		.prdListArea ul li:nth-child(odd) a {margin: 0px 5px 0px 0px;}

		.prdListArea ul li:nth-child(even) a {margin:0px 0px 0px 5px}

		.prdListArea ul li a {
			background-color: #FFFFFF;
			text-align: center;
			padding: 0px 0px 10px;
			display: block;
			border: 1px solid #ccc;
			box-sizing: border-box;
		}

		.prdListArea ul li .trackbtn {
			margin: 0px 5px 0px 0px;
			padding: 0px;
			position: absolute;
			bottom: 10px;
			right: 5px;
			z-index: 1;
			border: none;
			background-color: #FFFFFF;
			text-align: center;
			display: block;
			box-sizing: border-box;
		}

		.prdListArea ul li .prdImgWrap {
			width: 100%;
			height: 100%;
			position: relative;
			display: inline-block;
		}

		.prdListArea ul li a .prdEvent {
			height: 20px;
			font: 13px/20px Helvetica;
			color: #dd2726;
			text-align: left;
			margin: 5px 0px 0px;
			padding: 0px 5px;
			overflow: hidden;
		}

		.prdListArea ul li a .prdName {
			height: 40px;
			font: 15px/20px Helvetica;
			color: #484848;
			text-align: left;
			margin: 0px;
			padding: 0px 5px;
			overflow: hidden;
			margin-top: 5px;
		}

		.prdListArea ul li a .priceArea {
			margin: 0px;
			padding: 0px;
			text-align: left;
		}

		.prdListArea ul li a .priceArea .priceSymbol {
			font: 13px/24px Century Gothic;
			color: #D62872;
			margin: 0px 5px;
			text-align: left;
		}

		ul li a .priceArea .discountArea {
			height: 20px;
			padding: 0px 5px;
			display: block;
			position: relative;
			text-align: left;
		}

		ul li a .priceArea .discountArea b {
			background-color: #FF4C76;
			font: 9px/9px Helvetica;
			color: #FFFFFF;
			margin: 2px;
			padding: 2px 4px;
			border-radius: 3px;
			text-align: left;
		}

		ul li a .priceArea .discountArea .fastIcon {
			background-color: #BE0211;
		}
		ul li a .priceArea .priceSymbol .price {
			font-size: 22px;
			font-weight: normal;
		}

		ul li a .priceArea .priceSymbol .priceText {
			font: 10px/20px Helvetica;
			color: #A6A6A6;
			margin: 0px 0px 0px 3px;
		}

		.prdListArea ul li a .priceArea .discountArea.forsoldout::after {
			width: 100%;
			/* max-width: 200px; */
			color: rgb(255, 255, 255);
			content: "售完補貨中";
			text-align: center;
			position: absolute;
			bottom: 117px;
			left: 0px;
			font: 15px/26px Helvetica;
			margin: 0px;
			padding: 0px;
		}
		.prdListArea ul li a .priceArea .discountArea.forsoldout::after {
			background: rgba(0%,0%,0%,0.7);
		}

	</style>
	<script async src="https://cdn.ampproject.org/v0.js"></script>

</head>
<body>
		<article class="prdListArea">
			<ul>
			</ul>
		</article>
</body>
</html>
"""

def showRespInfo(jsonData):
	print(json.dumps(jsonData, indent=4, sort_keys=True))

def getGoodsDesc(type):
	if type == '0':
		return "一般商品"
	elif type == '1':
		return "中古車"
	elif type == '2':
		return "書類"
	else:
		return "Unknown Goods Type"

def toFile(soup):
	file = codecs.open("result.html", "w", "utf-8")
	file.write(soup)
	file.close()

def makeAmpPage(goodsList, link):
	soup = BeautifulSoup(html_doc, 'html.parser')
	ul_tag = soup.find('ul')
	html_tag = soup.find('html')
	html_tag['⚡'] = None
	script_tag = soup.find("script")
	script_tag['async'] = None
	link_tag = soup.find("link", rel="canonical")
	link_tag['href'] = link
	for goods in goodsList:
		li_tagSoup = BeautifulSoup(goods, 'html.parser')
		li_tag = li_tagSoup.find('li')
		ul_tag.append(li_tag)
	# print(soup)
	toFile(str(soup))

def makeGoodsList(goodsDict):
	goodsList = []
	for good in goodsDict:
		tag = ItmTag(good)
		link = tag.getCategoryUrl()
		goodsList.append(tag.getTag())
	makeAmpPage(goodsList, link)

def doMomoPost(host, cateCode, curPage):
	url = "http://www.momoshop.com.tw/api/moecapp/getCategoryGoodsV2"
	headers = {
		"user-agent": "my-app/0.0.1",
		"Accept": "*/*"
	}
	payload = {
	  "host": host,
	  "data": {
	    "cateCode": cateCode,
	    "curPage": curPage
  	}
	}

	r = requests.post(url, headers=headers, json=payload)
	jsonData = json.loads(r.text)
	goodsDict = jsonData['rtnGoodsData']['goodsInfoList']
	# showRespInfo(jsonData)
	makeGoodsList(goodsDict)
	

def main():
	# print("Hello World!")
	doMomoPost("AMP", "1901100205", "1")	
  
if __name__== "__main__":
	main()