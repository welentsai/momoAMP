
class MomoItm():
	def __init__(self, goodDict):
		self.goodsCode = goodDict['goodsCode']
		self.goodsUrl = goodDict['goodsUrl']
		self.goodsName = goodDict['goodsName']
		self.goodsSubName = goodDict['goodsSubName']
		self.imgUrl = goodDict['imgUrl']
		self.imgHeight = goodDict['imgHeight']
		self.imgWidth = goodDict['imgWidth']
		self.goodsPrice = goodDict['goodsPrice']
		self.icons = goodDict['icon']
		print("===========")
		print('momoItm')

	def __str__(self):
		print("goodsCode :" + self.goodsCode)
		print("goodsUrl :" + self.goodsUrl)
		print("goodsName :" + self.goodsName)
		print("goodsSubName :"+self.goodsSubName)
		print("imgUrl :" + self.imgUrl)
		print("imgHeight :" + self.imgHeight)
		print("imgWidth :" + self.imgWidth)
		print("goodsPrice :" + self.goodsPrice)
		print(self.icons)
		return str("===========")
		