#！/usr/bin/env python3
#-*- coding:utf-8 -*-

import pymysql
import os
import read as r

db = pymysql.connect(
    host='rm-uf6h0d6x74xv514n1ao.mysql.rds.aliyuncs.com',
    user='root',
    password='BCxTYzgCxSYL2Td2',
    database='tb_service',
    charset='utf8mb4',
)
cursor = db.cursor()

path_ = "jsonfile/"

def file_path(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return root, files
file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), path_)
a = file_path(file_dir)

def file_name(file_dir):
    tmp = []
    for root, dirs, files in os.walk(file_dir):
        # print(root) #当前目录路径
        # print("~~~~~~~~~~~~~~~~~~~~~~~")
        # print(dirs) #当前路径下所有子目录
        # print("~~~~~~~~~~~~~~~~~~~~~~~")
        # print(files) #当前路径下所有非目录子文件
        # print("~~~~~~~~~~~~~~~~~~~~~~~")
        if dirs:
            tmp.append(dirs)
    return tmp

all_list = file_name(file_dir)
first_list = all_list[0]
second_list = all_list[1:]
# 一位数组，一次列表
# print(first_list)
# 二维数组，二次列表
# print(second_list)


for i, first_dir in enumerate(first_list):
    for second_dir in second_list[i]:
        print(first_dir, second_dir)
        # 每个子路径下的 60 件商品的评论
        object= r.GetCommentsFromJson(first_dir, second_dir)
        comments, ids = object.main()
        for i in range(len(comments)):
            for comment in comments[i]:
                if comment != "此用户没有填写评论!":
                    # print(comment)
                    try:
                        # print(comment, first_dir, second_dir, ids[i])
                        sql = """ INSERT INTO tm(comments, category, tag, pID, url) VALUES ('%s','%s','%s','%s','%s')""" \
                              % (comment, first_dir, second_dir, ids[i], "https://detail.tmall.com/item.htm?id=%s" % ids[i])
                        cursor.execute(sql)
                        db.commit()
                    except Exception as e:
                        print(e)
            print("Success in product %s..." % ids[i])
        print("Finish %s/%s!" % (first_dir, second_dir))
