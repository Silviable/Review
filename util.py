import pymysql


def get_conn():
    '''连接数据库'''
    conn = pymysql.connect(
        host="localhost", port=3306,
        user="root", password="123456",
        database="gnls", charset="utf8"
    )
    cursor = conn.cursor()
    #返回数据库连接和cursorconn,cursor = get_conn()
    return conn, cursor


def find_all():
    conn, cursor = get_conn()
    sql = "select * from user_1"
    # 执行查询操作
    cursor.execute(sql)
    # 查询所有信息
    result = cursor.fetchall()
    return result


def insert_info(username, password, xingbie, address):
    conn, cursor = get_conn()
    sql = "insert into user_1 values(%s,%s,%s,%s)"
    cursor.execute(sql, [username, password, xingbie, address])
    conn.commit()
    conn.close()


def hrfind_all():
    conn, cursor = get_conn()
    sql = "select * from company_1"
    # 执行查询操作
    cursor.execute(sql)
    # 查询所有信息
    result = cursor.fetchall()
    return result


def select():
    conn, cursor = get_conn()
    sql = "select * from company1"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def change_info(username, newpassword):
    print(username, newpassword)
    conn, cursor = get_conn()
    sql = "update user_1 set 密码=%s where 用户名=%s"
    cursor.execute(sql, [newpassword, username])
    conn.commit()
    conn.close()
    cursor.close()


def insert_info2(username, name, password, companyaddress, hrname):
    conn, cursor = get_conn()
    sql = "insert into company_1 values(%s,%s,%s,%s,%s)"
    cursor.execute(sql, [username, name, password, companyaddress, hrname])
    conn.commit()
    conn.close()


def find_all2():
    conn, cursor = get_conn()
    sql = "select * from company_1"
    # 执行查询操作
    cursor.execute(sql)
    # 查询所有信息
    result = cursor.fetchall()
    return result


def change_info2(username, newpassword):
    print(username, newpassword)
    conn, cursor = get_conn()
    sql = "update company_1 set 密码=%s where 用户名=%s"
    cursor.execute(sql, [newpassword, username])
    conn.commit()
    conn.close()
    cursor.close()


def insert_info3(name, gender, email, age, phone, address, cardnum, zhiwei, money, message):
    conn, cursor = get_conn()
    sql = "insert into user_2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, [name, gender, email, age, phone, address, cardnum, zhiwei, money, message])
    conn.commit()
    conn.close()


def find_all3():
    conn, cursor = get_conn()
    sql = "select * from mycompany_employee"
    # 执行查询操作
    cursor.execute(sql)
    # 查询所有信息
    result = cursor.fetchall()
    return result


def insert_info4(name, gender, age, date, zhiwei, money, qita):
    conn, cursor = get_conn()
    sql = "insert into mycompany_employee values(%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, [name, gender, age, date, zhiwei, money, qita])
    conn.commit()
    conn.close()


def change_info3(username, newzhiwei, newmoney):
    conn, cursor = get_conn()
    sql = "update mycompany_employee set 职位=%s,薪资=%s where 姓名=%s"
    cursor.execute(sql, [newzhiwei, newmoney, username])
    conn.commit()
    conn.close()
    cursor.close()


def insert_info5(postname, number, salary, education, request1, hrname):
    conn, cursor = get_conn()
    sql = "insert into zhaopin values(%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, [postname, number, salary, education, request1, hrname])
    conn.commit()
    conn.close()
