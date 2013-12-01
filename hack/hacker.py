# coding: utf-8
import sys
import urllib2

class Hacker:
	""" ハッカークラス 
	"""
	def __init__(self):
		"""ハッカーコンストラクタ"""
		self._file = None
		self._urls = None
	
	def set_file(self, a_file):
		""" ファイルを設定する。"""
		self._file = a_file
		return
	
	def set_urls(self, urls):
		""" URLたちを設定する。"""
		self._urls = urls
		return
	
	def hack(self):
		""" URLたちをハックする。
		"""
		urls_length = float(len(self._urls))
		for index,a_url in enumerate(self._urls):
			sys.stdout.write("\x1b[0m=")
			if self.request(a_url):
				self._file.write(a_url+"\r\n")
				percent = str("%.1f" % (100*index/urls_length))
				rate = str("(%d,%d)" %(index, int(urls_length)) )
				sys.stdout.write(">\r\n")
				sys.stdout.write("\x1b[32m" + percent + "%" + rate + "\r\n")
				sys.stdout.write("\x1b[31m\x1b[1m")
				sys.stdout.write("Hit! ")
				sys.stdout.write("\x1b[34m\x1b[4m" + a_url + "\r\n")
			sys.stdout.flush()
		sys.stdout.write("\x1b[0m\x1b[33m")
		sys.stdout.write("\n100.0%\n")
		return
	
	def request(self, a_url):
		""" 指定したURLからページがあるかリクエストする。
		"""
		is_url = False
		try:
			urllib2.urlopen(a_url)
			is_url = True
		except urllib2.URLError, anException:
			pass
		except urllib2.HTTPError, anException:
			pass
		return is_url

