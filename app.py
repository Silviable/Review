from flask import redirect
import util
from flask import Flask, render_template, request
import pymysql

from sql import Mysql

app = Flask(__name__)


@app.route('/')
def login_1():
    return render_template("first_index.html")


@app.route('/login1')
def login1():
    return render_template("geren/login_1.html")


# 登录
@app.route('/login', methods=['post', 'get'])
def login():
    username = request.values.get("username")
    password = request.values.get("password")
    print(f"username:{username},password:{password}")
    # 查询数据库，验证user
    result = util.find_all()
    print(result)
    for user_1 in result:
        if username == user_1[0] and password == user_1[1]:
            return render_template("geren/index1.html")
    else:
        return "登录错误！"


@app.route('/indexgeren', methods=['post', 'get'])
def indexgeren():
    return render_template("geren/index1.html")


@app.route('/peixun', methods=['post', 'get'])
def peixun():
    return render_template("geren/peixun.html")


@app.route('/zhengce', methods=['post', 'get'])
def zhengce():
    return render_template("geren/zhengce.html")


@app.route('/about_us', methods=['post', 'get'])
def about():
    return render_template("geren/about_us.html")


@app.route('/our_services', methods=['post', 'get'])
def our_services():
    return render_template("geren/our_services.html")


@app.route('/select_company')
def select_company():
    return render_template("select_company.html")


@app.route('/e_to', methods=['post', 'get'])
def e_to():
    return render_template("geren/index1.html")


# HR登录
@app.route('/company_login')
def hr():
    return render_template("company/HR_login1.html")


@app.route('/hr_login', methods=['post', 'get'])
def hr_login():
    username = request.values.get("username")
    company = request.values.get("company")
    password = request.values.get("password")
    print(f"username:{username},company:{company},password:{password}")
    result = util.hrfind_all()
    print(result)
    for company_1 in result:
        if username == company_1[0] and company == company_1[1] and password == company_1[2]:
            return render_template("company/company_index.html")
    else:
        return "登录失败！"


# 用户注册
@app.route('/registration_employee', methods=['post', 'get'])
def register():
    return render_template("geren/registration_employee.html")


@app.route('/registration_employee1', methods=['post', 'get'])
def registration_employee1():
    username = request.values.get("username")
    password = request.values.get("password")
    xingbie = request.values.get("gender")
    address = request.values.get("address")
    print(f"username:{username},password:{password},xingbie:{xingbie},address:{address},")
    # 查询数据库，验证user
    result = util.find_all()
    print(result)

    for user_1 in result:
        if username == user_1[0]:
            return "注册失败！"
    else:
        util.insert_info(username, password, xingbie, address)
        return render_template("geren/login_1.html")


# 更改密码
@app.route('/change_password')
def change_password():
    return render_template("geren/change.html")


@app.route('/change_password1', methods=['post', 'get'])
def change():
    username = request.values.get("name")
    newpassword = request.values.get("newpassword")
    print(username, newpassword)
    util.change_info(username, newpassword)
    return render_template("geren/login_1.html")


# 公司注册
@app.route('/registration_authority', methods=['post', 'get'])
def register2():
    return render_template("company/registration_authority.html")


@app.route('/registration_authority1', methods=['post', 'get'])
def registration_authority1():
    username = request.values.get("companyusername")
    name = request.values.get("companyname")
    password = request.values.get("companypassword")
    companyaddress = request.values.get("companyaddress")
    hrname = request.values.get("hrname")
    print(f"username:{username},name:{name},password:{password},companyaddress:{companyaddress},hrname:{hrname},")
    # 查询数据库，验证user
    result = util.find_all2()
    print(result)

    for company_1 in result:
        if username == company_1[0]:
            return "注册失败！"
    else:
        util.insert_info2(username, name, password, companyaddress, hrname)
        return render_template("company/HR_login1.html")


# 公司更改密码
@app.route('/hr_change_password')
def change_password2():
    return render_template("company/hr_change.html")


@app.route('/hr_change_password1', methods=['post', 'get'])
def change2():
    username = request.values.get("name")
    newpassword = request.values.get("newpassword")
    print(username, newpassword)
    util.change_info2(username, newpassword)
    return render_template("company/HR_login1.html")


@app.route("/zhao", methods=['GET', 'POST'])
def info1():
    # 调用
    db = Mysql()
    results = db.getdata1()
    return render_template("geren/zhao.html", results=results)


@app.route("/rencaidangan", methods=['GET', 'POST'])
def info2():
    # 调用
    db = Mysql()
    results = db.getdata2()
    return render_template("company/information_employee.html", results=results)


@app.route("/gongsirencai", methods=['GET', 'POST'])
def info3():
    # 调用
    db = Mysql()
    results = db.getdata3()
    return render_template("company/gongsirencai.html", results=results)


@app.route("/ssss")
def select_employee():
    return render_template("company/select_employee.html")


@app.route("/search", methods=["POST", "GET"])
def search():
    keywords = request.values.get("key_word")
    print(keywords)
    conn, cursor = util.get_conn()
    sql = '''select * from company1 where 公司名称 like "%%%s%%"''' % keywords
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    context = {"company": result}
    return render_template("select_company_result.html", **context)


@app.route("/search1", methods=["POST", "GET"])
def search1():
    keyword = request.values.get("keyword1")
    print(keyword)
    conn, cursor = util.get_conn()
    sql = '''select * from user1 where 个人简历 like "%%%s%%"''' % keyword
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    context = {"employee": result}
    return render_template("selec_employee_result.html", **context)


@app.route('/information_username')
def information_username():
    return render_template("geren/verify_user.html")


@app.route('/message_user')
def message_user():
    return render_template("geren/xiugaixinxi.html")


@app.route('/change_message', methods=['post', 'get'])
def change_message():
    name = request.values.get("name")
    gender = request.values.get("gender")
    email = request.values.get("email")
    age = request.values.get("age")
    phone = request.values.get("phone")
    address = request.values.get("address")
    cardnum = request.values.get("cardnum")
    zhiwei = request.values.get("zhiwei")
    money = request.values.get("money")
    message = request.values.get("message")

    util.insert_info3(name, gender, email, age, phone, address, cardnum, zhiwei, money, message)

    return render_template("geren/index1.html")


@app.route("/verify_user", methods=["POST", "GET"])
def verify_user():
    username = request.values.get("username")
    print(username)
    conn, cursor = util.get_conn()
    sql = "select * from user_2 where name1 like %s"
    cursor.execute(sql, [username])
    result = cursor.fetchall()
    print(result)
    context = {"user": result}
    return render_template("geren/information_username.html", **context)


@app.route('/company_index')
def company_index():
    return render_template("company/company_index.html")


@app.route('/new_employee')
def new_employee():
    return render_template("company/new_employee.html")


@app.route('/new_message', methods=['post', 'get'])
def new_message():
    name = request.values.get("name")
    gender = request.values.get("gender")
    age = request.values.get("age")
    date = request.values.get("date")
    zhiwei = request.values.get("zhiwei")
    money = request.values.get("money")
    qita = request.values.get("qita")
    # 查询数据库，验证user
    result = util.find_all3()
    print(result)

    for mycompany_employee in result:
        if name == mycompany_employee[1]:
            return "添加失败"
    else:
        util.insert_info4(name, gender, age, date, zhiwei, money, qita)
        return render_template("company/company_index.html")


@app.route('/change_employee')
def change_employee():
    return render_template("company/change_employee.html")


@app.route('/change_emessage', methods=['post', 'get'])
def change_emessage():
    username = request.values.get("name")
    newzhiwei = request.values.get("zhiwei")
    newmoney = request.values.get("money")
    util.change_info3(username, newzhiwei, newmoney)
    return render_template("company/company_index.html")


@app.route('/fabuchangpin')
def fabuzhaopin():
    return render_template("company/fabuzhaopin.html")


@app.route('/fabu', methods=['post', 'get'])
def fabu():
    postname = request.values.get("postname")
    number = request.values.get("number")
    salary = request.values.get("salary")
    education = request.values.get("education")
    request1 = request.values.get("request1")
    hrname = request.values.get("hrname")
    # 查询数据库，验证user
    util.insert_info5(postname, number, salary, education, request1, hrname)
    return render_template("company/company_index.html")


if __name__ == '__main__':
    app.run()
