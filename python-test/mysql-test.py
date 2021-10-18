import pymysql

 
conn = pymysql.connect(host='localhost', user='root', password='1234qwer',
                       db='test_db', charset='utf8')

conn.close()