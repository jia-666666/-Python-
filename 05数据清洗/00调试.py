

f = open('../file/CSV/智能手机-all-bak.csv', 'r', encoding='UTF-8')
line = f.readlines()  # 读取一行文件，包括换行符
for i in line:
    k = i.split(',')
    # cursor.execute("insert into xie11(color,size,source,discuss,time) values(%s,%s,%s,%s,%s)",(k[0], k[1], '天猫', k[2], k[3].split('\n')[0]))
    # conn.commit()
    print('写入成功')