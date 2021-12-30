import pymysql
#告诉Django用pymysql来替代默认的MYSQLdb
#print(dir(pymysql)) #打印该应用具备模块
pymysql.install_as_MySQLdb()


