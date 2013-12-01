# coding: utf-8

class URLMaker:
	""" URLメーカー 
	"""
	def __init__(self):
		self._paths= ["SouriDaijin","PL","PL/SouriDaijin"]
		self._roots = ["http://www.cc.kyoto-su.ac.jp/","http://www.cse.kyoto-su.ac.jp/","http://github.com/"]
		self._urls = []

	def urls(self, first, last):
		""" 指定された学生証番号のリストからURLを作って応答する。
		"""
		for number in range(first, last):
			if sum(map(int,list(str(number)))) % 10 == 0:
				self.url(number)
		return self._urls
				
	def url(self, number):
		""" 指定された学生証番号からURLを作って応答する。
		"""
		for root in self._roots:
			if "kyoto-su.ac.jp" in root:
				for path in self._paths:
					url = root + "~g1" + str(number) + "/" + path + "/"
			else:
				url = root + "g1"  + str(number) + "/"
			self._urls.append(url + " ")
		return
