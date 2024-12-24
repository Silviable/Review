import pymysql


class Mysql(object):
    def __init__(self):
        try:
            self.db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="gnls", charset="utf8")
            # 游标对象
            self.cursor = self.db.cursor()
            print("连接成功！")
        except:
            print("连接失败！")

    # 查询数据函数
    def getdata1(self):
        sql = "select * from company1"
        # 执行sql语句
        self.cursor.execute(sql)
        # 获取所有的记录
        results = self.cursor.fetchall()
        return results

    def getdata2(self):
        sql = "select * from user1"
        # 执行sql语句
        self.cursor.execute(sql)
        # 获取所有的记录
        results = self.cursor.fetchall()
        return results

    def getdata3(self):
        sql = "select * from mycompany_employee"
        # 执行sql语句
        self.cursor.execute(sql)
        # 获取所有的记录
        results = self.cursor.fetchall()
        return results
    # 关闭
    def __del__(self):
        self.db.close()
