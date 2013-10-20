#!/usr/bin/env python
# coding: utf-8
"""
画像をリサイズするスクリプト。
thumbnailフォルダがなければ、自動でthumbnailフォルダを作る。
もし、今のディレクトリにimagesフォルダがあれば、imagesフォルダの全画像をサムネイル化し、thumbnailフォルダに入れる。
なければ、今のディレクトリの全画像をサムネイル化し、thumbnailフォルダに入れる。
＊ただし、python用OpenCVがインストールが必要
	
Example: 
	python resize.py 90(resize_percent)
	
Pydoc:	
	pydoc -w resize
	＊ただしpydocの仕様上、ブラウザ上でutf-8にするか、pydoc自体のソースコードの"def pages"を変更しないと文字化けする。
	pydoc resize
	resize.pyの仕様をmanのように見ることが出来る。ターミナル上なので、日本語にも対応。
	
Comment:
	コメントの書き方は/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/内のソースコードを参考に書きました。汚いですが、あしからず。
"""
__author__  = "TasukuTAKAHASHI"
__version__ = "1.0.0"
__date__    = "20 Oct 2013"

import cv
import sys
import os

def get_load_directory():
	""" 画像をロードするディレクトリを応答する。
	"""
	if "images" in os.listdir('.'):
		load_directory = os.getcwd() + "/images"
	else: 
		load_directory = os.getcwd()
	return load_directory

def get_wirte_directory():
	""" サムネイルを保存するディレクトリを応答する。
	"""
	a_dir = "thumbnails"
	if not a_dir in os.listdir('.'):
		os.mkdir(a_dir)
	return a_dir

def get_images(load_directory, image_types):
	""" 画像ファイルの拡張子があれば、その画像ファイルたちを応答する。
	"""
	files = os.listdir(load_directory)
	images = [a_file for a_file in files for a_type in image_types if a_type in a_file]
	return images

def make_thumbnails(load_directory, write_directory, image_names):
	""" 画像をロードし、thumbnails/フォルダにサムネイル画像を作る。
	"""
	for a_name in image_names:
		print "thumbnails/"+a_name
		an_image = cv.LoadImageM(load_directory +"/"+ a_name)
		thumbnails = cv.CreateMat(an_image.rows*resize_percent/100, an_image.cols*resize_percent/100, cv.CV_8UC3)
		cv.Resize(an_image,thumbnails)
		cv.SaveImage(write_directory +"/"+ a_name, thumbnails)

if __name__ == '__main__':
	image_types = [".png",".jpg",".jpeg",".tiff"]
	if len(sys.argv) == 1:
		print "Arguments error: You need input resize percent."
		print "\t python resize.py 80"
		quit()
	else:
		resize_percent = int(sys.argv[1])
	
	load_directory = get_load_directory()
	images = get_images(load_directory, image_types)
	if images == []: 
		print "There isn't images in current_directory or current_directory/images/"
		quit()
	make_thumbnails(load_directory, get_wirte_directory(), images)
