#!/usr/bin/env python
# coding: utf-8
# -*- coding: utf-8 -*-
"""
リサイズする。
thumbnailフォルダがなければ、自動でthumbnailフォルダを作る。
もし、今のディレクトリにimagesフォルダがあれば、imagesフォルダの全画像をサムネイル化し、thumbnailフォルダに入れる。
なければ、今のディレクトリの全画像をサムネイル化し、thumbnailフォルダに入れる。
＊ただし、python用OpenCVがインストールが必要
	
Example: 
	python resize.py 90(resize_persent)
"""
__author__  = "TasukuTAKAHASHI"
__version__ = "1.0.0"
__date__    = "20 Oct 2013"

import cv
import sys
import os

def get_load_directory():
	if "images" in os.listdir('.'):
		load_directory = os.getcwd() + "/images"
	else: 
		load_directory = os.getcwd()
	return load_directory

def make_thumbnails_dir():
	if not "thumbnails" in os.listdir('.'):
		os.mkdir("thumbnails")

def make_thumbnails(names, load_directory):
	for a_name in names:
		print "thumbnails/"+a_name
		anImage = cv.LoadImageM(load_directory +"/"+ a_name)
		thumbnails = cv.CreateMat(anImage.rows*resize_persent/100, anImage.cols*resize_persent/100, cv.CV_8UC3)
		cv.Resize(anImage,thumbnails)
		cv.SaveImage("thumbnails/"+a_name, thumbnails)

def get_images(image_types, load_directory):
	files = os.listdir(load_directory)
	images = [a_file for a_file in files for a_type in image_types if a_type in a_file]
	return images
	
if __name__ == '__main__':
	image_types = [".png",".jpg",".jpeg",".tiff"]
	resize_persent = int(sys.argv[1])
	
	load_directory = get_load_directory()
	images = get_images(image_types,load_directory)
	if images == []: 
		print "現在のディレクトリ内またはimages/に画像がありません。"
		quit()
	make_thumbnails_dir()
	make_thumbnails(images,load_directory)