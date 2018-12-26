import pymysql

host = '127.0.0.1'
user = 'root'
passwd = '123456'
db = 'djangofrom'
port = 3306
charset = 'utf8'
conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db, port=port, charset=charset)

cur = conn.cursor()

for i in range(1, 100):
    sql = "insert into host(HostName,IP) values('aaa{}','{}.{}.{}.{}');".format(i, i, i, i, i)
    cur.execute(sql)
    conn.commit()
    print(sql)
cur.close()
conn.close()
