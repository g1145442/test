# coding: utf-8
""" 
学生証番号からページを探索し、printする。（クラス名なし）
ドメインは「http://www.cc.kyoto-su.ac.jp, http://www.cse.kyoto-su.ac.jp, http://github.com」とし、
http://www.cc.kyoto-su.ac.jp/~g1学生証番号/SouriDaijin/
http://www.cc.kyoto-su.ac.jp/~g1学生証番号/PL/
http://www.cc.kyoto-su.ac.jp/~g1学生証番号/PL/SouriDaijin/
http://www.cse.kyoto-su.ac.jp/~g1学生証番号/SouriDaijin/
http://www.cse.kyoto-su.ac.jp/~g1学生証番号/PL/
http://www.cse.kyoto-su.ac.jp/~g1学生証番号/PL/SouriDaijin/
http://github.com/g1学生証番号/
の中から探索する。

探査スピードは4m8.819s
subprocessから、wgetを使えばページ取得も可能
http://github.com/g1144407/
http://github.com/g1144560/
http://github.com/g1144704/
http://github.com/g1144902/
http://www.cc.kyoto-su.ac.jp/~g1144911/SouriDaijin/
http://www.cc.kyoto-su.ac.jp/~g1144911/PL/
http://www.cse.kyoto-su.ac.jp/~g1144911/PL/
http://www.cc.kyoto-su.ac.jp/~g1144948/SouriDaijin/
"""

import subprocess
import urllib2
folder_list = ["SouriDaijin","PL","PL/SouriDaijin"]
ksu_domain_list = ["http://www.cc.kyoto-su.ac.jp","http://www.cse.kyoto-su.ac.jp"] 
github_domain = "http://github.com"

def getStudentNumberList():
	studentNumberList = []
	for studentNumber in range(144011,145334):
		totalSum = sum( [int(index) for index in str(studentNumber)] )
		if totalSum % 10 == 0: #if fomal number.
			studentNumberList.append(studentNumber)
	return studentNumberList

def request(address):
	try: 
		urllib2.urlopen(address)
		aFile.write(address+'\r\n')
		print "I found " + address
	except urllib2.URLError, anException:
		pass
	except urllib2.HTTPError, anException:
		print anException.reason

def mater(index):
	pasent = (index / a_length) * 100
	print '=',
		
studentNumberList = getStudentNumberList()
a_length = float(len(studentNumberList))
aFile = open("a.txt","w")

for index, studentNumber in enumerate(studentNumberList):
	print studentNumber
	for a_ksu_domain in ksu_domain_list:
		for a_folder in folder_list:
			address = a_ksu_domain + "/" + "~g1" + str(studentNumber) + "/" +a_folder+ "/"
			request(address)
	address = github_domain + "/" + "g1" + str(studentNumber) + "/"
	request(address)
aFile.close()
