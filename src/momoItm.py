
class MomoItm():
	def __init__(self, goodDict):
		self.categoryUrl = goodDict['categoryUrl']
		self.goodsCode = goodDict['goodsCode']
		self.goodsUrl = goodDict['goodsUrl']
		self.goodsName = goodDict['goodsName']
		self.goodsSubName = goodDict['goodsSubName']
		self.imgUrl = goodDict['imgUrl']
		self.imgHeight = goodDict['imgHeight']
		self.imgWidth = goodDict['imgWidth']
		self.goodsPrice = self.getPrice(goodDict['goodsPrice'])
		self.goodsPriceText = self.getPriceText(goodDict['goodsPrice'])
		self.icons = goodDict['icon']
		self.fastIcon = self.getFastIcon(goodDict['icon'])
		self.couponIcons = self.getCouponIcons(goodDict['icon'])
		# print("===========")
		# print('momoItm')

	def getPrice(self, priceStr):
		pList = priceStr.split()
		if(len(pList) == 1 or len(pList) ==2):
			return pList[0]
		else:
			return ''

	def getPriceText(self, priceStr):
		pList = priceStr.split()
		if(len(pList) ==2):
			return pList[1]
		else:
			return ''

		print("price: " + self.goodsPrice.split())

	def getFastIcon(self, iconList):
		if(len(iconList) >= 1):
			return iconList[0]['iconContent']
		else:
			return ''
	def getCouponIcons(self, iconList):
		couponIconList = []
		if(len(iconList) >= 2):
			for couponItm in iconList[1:len(iconList)+1]:
				couponIconList.append(couponItm['iconContent'])
			return couponIconList
		else:
			return couponIconList

	def __str__(self):
		print("goodsCode :" + self.goodsCode)
		print("goodsUrl :" + self.goodsUrl)
		print("goodsName :" + self.goodsName)
		print("goodsSubName :"+self.goodsSubName)
		print("imgUrl :" + self.imgUrl)
		print("imgHeight :" + self.imgHeight)
		print("imgWidth :" + self.imgWidth)
		print("goodsPrice :" + self.goodsPrice)
		print("goodsPriceText :" + self.goodsPriceText)
		print("fastIcon :" + self.fastIcon)
		print(self.couponIcons)
		print(self.icons)
		return str("===========")
		