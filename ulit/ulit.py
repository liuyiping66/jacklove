from faker import Faker
import os,time,csv
class Fake_d():
    fake = Faker(locale='zh_CN')
    def get_number(self,m,n):#随机生成指定范围内的数字
        return self.fake.random_int(min=m,max=n)
    def get_string(self):
        return self.fake.sentence()[:-1] #随机生成一句话
    def get_address(self):
        return self.fake.province()+'-'+self.fake.city()#随机生成地址
    def get_datetime(self):
        return self.fake.future_datetime()# 随机生成未来时间
    def get_name(self):
        return self.fake.name()#随机生成用户名
    def get_phone(self):
        return self.fake.phone_number()#随机生成电话号码
    def get_email(self):
        return self.fake.ascii_email()#随机生成电子邮箱
BASEPATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]  # 获取项目路径
CASEPATH = os.path.join(BASEPATH,'cases')    # 获取测试用例文件目录路径
DRIVERPATH = os.path.join(BASEPATH,'drivers')    # 获取浏览器驱动目录路径
IMGPATH = os.path.join(BASEPATH,'imgs')    # 获取截图文件目录路径
PAGEPATH = os.path.join(BASEPATH,'pages')    # 获取页面类文件目录路径
REPORTPATH = os.path.join(BASEPATH,'report')    # 获取测试报告文件目录路径
DATAPATH = os.path.join(BASEPATH,'datas')     # 获取测试数据文件目录路径
BASEURL = 'http://127.0.0.1:8000/api/'
def get_time():
    return time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())
def get_test_data(file):
    test_data = []
    f = open(file)  # 打开文件
    data = csv.reader(f)  # 调用reader()，读取csv文件内容
    for i in data:
        test_data.append(i) # 将读取的数据追加到列表中
    f.close()  # 关闭文件
    return test_data



if __name__ in '__main__':
    d=get_test_data(DATAPATH+'/user_paw.csv')
    for i in d[0]:
        print(i)