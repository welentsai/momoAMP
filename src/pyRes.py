
import json
import requests

def doGet(url):
    r = requests.get(url)
    print(r.status_code)
    print(r.cookies)
#     print(r.text)

def doGetWithParams(myParams):
    fakeHeaders = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = 'http://www.momoshop.com.tw/api/moecapp/getCategoryGoodsV2'
#     res = requests.get(url, params=myParams)
    res = requests.get(url, params=myParams, headers=fakeHeaders)
    print(res.url)
    print(res.request.headers) 
    print(res.status_code)
    print(res.text)

def doGetMomoL4(myParams):
    fakeHeaders = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    momoUrlLayer4 = 'https://m.momoshop.com.tw/cateGoods.momo'
    res = requests.get(momoUrlLayer4, params=myParams)
#     res = requests.get(momoUrlLayer4, params=myParams, headers=fakeHeaders)
    print(res.url)
    print(res.request.headers) 
    print(res.status_code)
    print(res.text)

def doPost(url, myParams):
    fakeHeaders = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.post(url, data=myParams, headers=fakeHeaders)
    print(r.status_code)
    print(r.text)
    
def doMomoPost(params):
    headers = {'user-agent': '"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    fakeHeaders = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    momoRestfulURL = 'http://www.momoshop.com.tw/api/moecapp/getCategoryGoodsV2'
#     momoRestfulURL2 = 'http://wsfuat3.momoshop.com.tw:8080/api/moecapp/getCategoryGoodsV2'
#     fakeHeaders = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    payload = json.dumps(params)
    print(payload)
    res = requests.post(momoRestfulURL, data=payload)
#     res = requests.post(momoRestfulURL, data=params)    
    print(res.request.headers) 
    print(res.status_code)
    print(res.text)

def doMomoPostTest(url, **kwargs):
    # kwargs is a dictionary.
    print(url)
    if('headers' in kwargs): # key in dict
        print(kwargs['headers'])
    if('params' in kwargs):
        print(kwargs['params'])

if __name__ == "__main__":
    my_data = {'key1': 'value1', 'key2': 'value2'} # testing
#     doPost('http://httpbin.org/post', my_data)
               
#     myParams = {'host':'momoshop', 'data':{'cateCode':'1900000000', 'curPage':'1', 'sortType':'6'}}
    myParams = {'host':'AMP', 'data':{'cateCode':'4000700009', 'curPage':'1'}}
    doMomoPost(myParams)
     
    moL4Params = {'cn':'1901100205'}
#     doGetMomoL4(moL4Params)

    myParams2 = {'cn':'1900000000', 'page':'2'}
#     doGetWithParams('https://m.momoshop.com.tw/category.momo', myParams2)

#     doMomoPostTest('https://m.momoshop.com.tw/category.momo', headers='5566', params={'cn':'1900000000'})