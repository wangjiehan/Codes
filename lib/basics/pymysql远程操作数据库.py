import pymysql
db = pymysql.connect(
	host = 'rm-uf6tz1g9l077nkd0do.mysql.rds.aliyuncs.com',	# 本地的话为"localhost"
	user = 'rdsroot',		# 输入你的数据库账号
	password = 'yinnuo123!@#',		# 数据库密码
	database = 'test',		# 数据库名（database名）
	charset = 'utf8mb4',	# 读取中文不想乱码的话，记得设置这个
	)
# 创建游标，()内为空默认是元组格式
cursor = db.cursor()
# 操作设置为字典类型，返回结果为字典格式：
# cursor = db.cursor(cursor = pymysql.cursors.DictCursor)

'''
一、查询数据库版本
'''
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print ("Database version : %s " % data)
'''
# 读取一行：
data = cursor.fetchone() 	# 一维tuple
# 读取多行：
data1 = cursor.fetchmany(2) 	# 2就是两行，形成一个二维tuple
# 读取所有：
data2 = cursor.fetchall() 	# 形成一个二维tuple
'''

'''
二、创建数据库表
'''
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)

'''
三、数据库插入操作
'''
# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
'''
也可以这么写：
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)

# '%s' 代表string型，'%d'代表int型，'%c'代表char型（也可以写成string型）
'''
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()
'''rollback 回滚，数据库里做修改(update,insert,delete)后、commit之前，
	使用rollback可以恢复数据到修改之前'''

'''
四、数据库查询
Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
	fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
	fetchall(): 接收全部的返回结果行.
	rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
'''

# SELECT * FROM `aiw_read_article` WHERE content is NULL or content = ''

# SQL 查询语句：收入大于1000的
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)	# 一个数直接%，多个数用 % \
    # SELECT * FROM <表名> (WHERE ...)：从一个表中按某个条件提取所有列
    # SELECT <列名> FROM <表名>：从一个表中单独提取某个列，注意列名中间不能有空格
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # 打印结果
      print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income ))
except:
   print ("Error: unable to fetch data")

'''
五、数据库更新
'''
# SQL 更新语句，将 TESTDB 表中 SEX 为 'M' 的 AGE 字段递增 1
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%s'" % ('M')
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()

'''
六、数据删除
'''
# SQL 删除语句，删除数据表 EMPLOYEE 中 AGE 大于 20 的所有数据
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()


# finally关闭数据库连接
db.close()

'''
1、数据库名与表名是严格区分大小写的；
2、表的别名是严格区分大小写的；
3、列名与列的别名在所有的情况下均是忽略大小写的；
4、字段内容默认情况下是大小写不敏感的。
'''



