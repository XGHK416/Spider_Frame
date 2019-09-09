# 参数制定
import pymysql
def write_into_mysql():
    # 数据库链接自写
    db = pymysql.connect(host='120.78.136.84', user='android', password='Android-123', db='android')
    cursor = db.cursor()
    # 数据库语句自写
    #sql = 'INSERT INTO news_content(id,news_type,title,message) values(%s,%s,%s,%s)ON DUPLICATE KEY UPDATE id=values(id)'
    try:
        # 运行sql
        # cursor.execute(sql, (id, type, title, message))
        db.commit()
    except Exception as exc:
        print(exc)
        db.rollback()
        print("error")
    db.close()
