import pymysql

# 连接database
conn = pymysql.connect(
host="127.0.0.1",
user ="root",
password ="123456",
database ="test",
charset ="utf8mb4")

# 获取一个可以执行SQL语句的光标对象
cursor = conn.cursor()

# 将结果作为字典返回的游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

def data_wash():
    f = open('../file/TXT/数据清洗.txt', 'r', encoding='UTF-8')
    line = f.readlines()  # 读取一行文件，包括换行符
    for i in line:
        try:
            cursor.execute(i)
            conn.commit()
        except Exception as e:
            print(e)



print('开始数据清洗（5s）')
data_wash()
print('数据清洗完成')

