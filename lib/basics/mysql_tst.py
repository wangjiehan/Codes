import pymysql
db = pymysql.connect(
	host = 'localhost',
	user = 'root',
	password = 'wjh321088',
	database = 'test',
	charset = 'utf8mb4'
	)

cursor = db.cursor()

sql = """INSERT INTO test(age)
		 VALUES ('2019-04-19')"""
cursor.execute(sql)
db.commit()

db.close()

