#!/usr/bin/python
# -*- coding:utf-8 -*-
# wirter:En_dust
# Blog:http://www.opensource-sec.com/

from dns import *
import logging
import argparse

def parse_args():
	parser = argparse.ArgumentParser(description='DNS Tools V1.0', prog='DNS Tools', usage='DNS_query.py -d baidu.com -t A')
	parser.add_argument('-t', '--type', help="DNS记录类型")
	parser.add_argument('-d', '--domain', help="要查询的域名")
	parser.add_argument('-a', '--all', action='store_true', help="获取指定域名的所有DNS类型记录\n包括A,CNAME,MX,AAAA,TXT,NS,SRV,CAA记录")
	parser.add_argument('-f', '--file', help="导入文件批量查询指定DNS记录")
	return parser.parse_args()

def singleQuery():
	try:
		result = resolver.query(args.domain, args.type)
		print("%s记录查询结果：" % args.type)
		for i in result:
			print(i)
	except resolver.NoAnswer as e:
		logging.error(e)
	except rdatatype.UnknownRdatatype as e:
		logging.error(e)
	else:
		print("程序执行完毕!")

def allQuery():
	dnsList = ['A', 'CNAME', 'MX', 'AAAA', 'TXT', 'NS', 'SRV', 'CAA']
	for i in dnsList:
		try:
			result = resolver.query(args.domain, i)
			print("\n%s记录查询结果：" % i)
			for j in result:
				print(j)
		except resolver.NoAnswer as e:
			logging.error(e)
		except rdatatype.UnknownRdatatype as e:
			logging.error(e)

def FileQuery(path):
	domains = open(path,'r',encoding="utf-8",errors='ignore')
	for domain in domains:
		try:
			result = resolver.query(domain.strip(), args.type)
			print("\n%s%s记录查询结果：" % (domain,args.type))
			for i in result:
				print(i)
		except resolver.NoAnswer as e:
			logging.error(e)
		except rdatatype.UnknownRdatatype as e:
			logging.error(e)

if __name__ == '__main__':
	args = parse_args()
	logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
	if args.all:
		# print("进入批量查询")
		allQuery()
	elif args.file:
		if args.type != None:
			FileQuery(args.file)
		else:
			print("请通过-t指定DNS记录类型")
	else:
		# print("进入单个模式")
		singleQuery()
