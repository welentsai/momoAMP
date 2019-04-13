

import requests
import json

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
	  "host": "AMP",
	  "data": {
	    "cateCode": "4000700009",
	    "curPage": "1"
  	}
	}

	r = requests.post(url, headers=headers, json=payload)
	jsonData = json.loads(r.text)
	goodsDict = jsonData['rtnGoodsData']['goodsInfoList']
	for good in goodsDict:
		print(good['goodsType'] + " (" + getGoodsDesc(good['goodsType']) + ")")
		print(good['imgUrl'])
		print(good['imgWidth'] + " " + good['imgHeight'])
		print(good['goodsUrl'])
		print(good['categoryUrl'])
		print(good['icon'])
		print()

def main():
	# print("Hello World!")
	doMomoPost("AMP", "4000700009", "1")	
  
if __name__== "__main__":
	main()