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

import sys
from urlmaker import URLMaker
from hacker import Hacker

def main():
	maker = URLMaker()
	urls = maker.urls(144250,145000)
	hacker = Hacker()
	with open("log.txt", "w") as a_file:
		hacker.set_file(a_file)
		hacker.set_urls(urls)
		hacker.hack()

if __name__ == "__main__":
	sys.exit(main())

