from bs4 import BeautifulSoup, Tag

from momoItm import MomoItm

class ItmTag():
	def __init__(self, goodDict):
		self.goodDict = goodDict
		self.MomoItm = MomoItm(goodDict)

		# create html for this Item
		self.soup = BeautifulSoup()
		self.li_tag = self.soup.new_tag("li")
		self.input_tag = self.soup.new_tag("input")
		self.a_tag = self.soup.new_tag("a")
		self.div_tag = self.soup.new_tag("div")
		self.amp_img_tag = self.soup.new_tag("amp-img")
		self.p_prdEvent = self.soup.new_tag("p")
		self.p_prdName = self.soup.new_tag("p")
		self.p_priceArea = self.soup.new_tag("p")
		self.span_priceSymbol = self.soup.new_tag("span")
		self.b_price = self.soup.new_tag("b")
		self.b_priceText = self.soup.new_tag("b")
		self.span_discount = self.soup.new_tag("span")
		self.b_fastIcon = self.soup.new_tag("b")
		print(self.MomoItm)
		self.makeTag()

	def makeTag(self):
		# 填內容
		self.makeInputTag()
		self.makeATag()
		self.makeDivTag()
		self.makeAmpImgTag()
		self.makePTag()

		# 定義 element 之間的順序
		self.soup.append(self.li_tag)
		self.li_tag.append(self.input_tag)
		self.li_tag.append(self.a_tag)
		self.a_tag.append(self.div_tag)
		self.div_tag.append(self.amp_img_tag)
		self.a_tag.append(self.p_prdEvent)
		self.a_tag.append(self.p_prdName)
		self.a_tag.append(self.p_priceArea)
		self.p_priceArea.append(self.span_priceSymbol)
		self.span_priceSymbol.append(self.b_price)
		self.span_priceSymbol.append(self.b_priceText)
		self.p_priceArea.append(self.span_discount)
		self.span_discount.append(self.b_fastIcon)


	def makeInputTag(self):
		self.input_tag['type'] = 'hidden'
		self.input_tag['name'] = 'goodsCode'
		self.input_tag['id'] = 'goodsCode'
		self.input_tag['value'] = self.MomoItm.goodsCode

	def makeATag(self):
		self.a_tag['href'] = self.MomoItm.goodsUrl
		self.a_tag['title'] = self.MomoItm.goodsName

	def makeDivTag(self):
		self.div_tag['class'] = 'prdImgWrap'

	def makeAmpImgTag(self):
		self.amp_img_tag['class'] = 'goodsImg'
		self.amp_img_tag['alt'] = self.MomoItm.goodsName
		self.amp_img_tag['title'] = self.MomoItm.goodsName
		self.amp_img_tag['src'] = self.MomoItm.imgUrl
		self.amp_img_tag['layout'] = 'responsive'
		self.amp_img_tag['width'] = self.MomoItm.imgWidth
		self.amp_img_tag['height'] = self.MomoItm.imgHeight

	def makePTag(self):
		self.p_prdEvent['class'] = 'prdEvent'
		self.p_prdEvent.string = self.MomoItm.goodsSubName
		self.p_prdName['class'] = 'prdName'
		self.p_prdName.string = self.MomoItm.goodsName
		self.p_priceArea['class'] = 'priceArea'

	def getTag(self):
		print(self.soup.prettify())