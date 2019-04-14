

import requests
import json

from momoItm import MomoItm
from momoItmTag import ItmTag

def showRespInfo(jsonData):
	print(json.dumps(jsonData, indent=4, sort_keys=True))

def showGoods(goodsDict):
	for good in goodsDict:
		tag = ItmTag(good)
		tag.getTag()
		# print(good['goodsType'] + " (" + getGoodsDesc(good['goodsType']) + ")")
		# print(good['imgUrl'])
		# print(good['imgWidth'] + " " + good['imgHeight'])
		# print(good['goodsUrl'])
		# print(good['categoryUrl'])
		# print(good['icon'])
		# print()

def getGoodsDesc(type):
	if type == '0':
		return "一般商品"
	elif type == '1':
		return "中古車"
	elif type == '2':
		return "書類"
	else:
		return "Unknown Goods Type"

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
	showGoods(goodsDict)
	

def main():
	# print("Hello World!")
	doMomoPost("AMP", "1901100205", "1")	
  
if __name__== "__main__":
	main()