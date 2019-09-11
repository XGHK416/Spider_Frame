import oss2, uuid
import os
import pymysql
import datetime


#
def oss(img_key, img_path):
    auth = oss2.Auth('LTAI6nNt77Q2G4oH', 'PfXVy56sFK5MLsMAYaBlmRSDieHQMm')
    endpoint = 'oss-cn-beijing.aliyuncs.com'
    bucket = oss2.Bucket(auth, endpoint, 'xghk416')
    a = bucket.put_object_from_file(img_key, img_path)
    url = 'https://xghk416.oss-cn-beijing.aliyuncs.com/' + img_key
    # print(url)
    url_insert(url)


def url_insert(url):
    db = pymysql.connect(host='39.106.228.42', user='Recognition', password='recognition', database='Recognition',
                         charset='utf8')
    cursor = db.cursor()
    uid = str(uuid.uuid4())
    suid = ''.join(uid.split('-'))
    # print(suid)
    sql = 'INSERT INTO `traffic_sign`(id,pic_url,create_time)VALUES(%s,%s,%s)'
    # print(sql)
    try:
        cursor.execute(sql, (str(suid), url,datetime.datetime.now()))
        db.commit()
    except Exception as exc:
        print(exc)
        db.rollback()
        print("error")
    db.close()


if __name__ == "__main__":
    img_key = 'test/' + str(uuid.uuid4()) + '.png'
    img_path1 = 'C:/Users/HJM/Desktop/学习资料/图像识别/traffic_sign_classfication-master/data/train/'
    for r, ds, fs in os.walk(img_path1):
        for fsItem in fs:
            img_key1 = str('train') + '/' + r[-4:] + '/' + str(uuid.uuid4()) + '.png'
            print(img_key1)
            s = r + '/' + fsItem
            print(s)
            oss(img_key1, s)
    # C:\Users\HJM\Desktop\爬虫\0003
    # oss(img_key, img_path)
    print("upload success!")
