import requests
import unittest
from 接口自动化框架.ulit.ulit import BASEURL,Fake_d
from 接口自动化框架.Con_data_base.Connectdata import connect_data
url = BASEURL+'add_guest/'
class Test_case(unittest.TestCase):
    '''添加嘉宾'''
    s = connect_data()
    data = {}
    f = Fake_d()
    def setUp(self):
        self.s.con_mysql()
        self.data['eid']=1231231
        self.data['realname'] = self.f.get_name()
        self.data['email'] = self.f.get_email()

    def tearDown(self):
        self.s.close_cur()
    def testcase1(self):
        '''输入正确的参数，添加成功'''
        self.data['phone'] = int(str(13) + str(self.f.get_number(000000000, 999999999)))
        r = requests.post(url, self.data)
        res = r.json()
        self.assertEqual(10000, res['status'])
        self.assertEqual('add guest success', res['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s"  and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.s.execute_sql(sql %(self.data['realname'],self.data['phone']))
        self.assertEqual(1,n)
    def testcase2(self):
        '''输入正确的参数，电话号码15开头添加成功'''
        self.data['phone'] = int(str(15) + str(self.f.get_number(000000000, 999999999)))
        r = requests.post(url, self.data)
        res = r.json()
        self.assertEqual(10000, res['status'])
        self.assertEqual('add guest success', res['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s"  and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.s.execute_sql(sql %(self.data['realname'],self.data['phone']))
        self.assertEqual(1,n)
    def testcase3(self):
        '''输入正确的参数，电话号码17开头添加成功'''
        self.data['phone'] = int(str(17) + str(self.f.get_number(000000000, 999999999)))
        r = requests.post(url, self.data)
        res = r.json()

        self.assertEqual(10000, res['status'])
        self.assertEqual('add guest success', res['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s"  and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.s.execute_sql(sql %(self.data['realname'],self.data['phone']))
        self.assertEqual(1,n)
    def testcase4(self):
        '''输入正确的参数，电话号码18开头添加成功'''
        self.data['phone'] = int(str(18) + str(self.f.get_number(000000000, 999999999)))
        r = requests.post(url, self.data)
        res = r.json()
        self.assertEqual(10000, res['status'])
        self.assertEqual('add guest success', res['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s"  and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.s.execute_sql(sql %(self.data['realname'],self.data['phone']))
        self.assertEqual(1,n)
    def testcase5(self):
        '''输入正确的参数，电话号码19开头添加成功'''
        self.data['phone'] = int(str(19) + str(self.f.get_number(000000000, 999999999)))
        r = requests.post(url, self.data)
        res = r.json()
        self.assertEqual(10000, res['status'])
        self.assertEqual('add guest success', res['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s"  and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.s.execute_sql(sql %(self.data['realname'],self.data['phone']))
        self.assertEqual(1,n)
    def testcase6(self):
        '''输入正确的参数，电话号码2开头添加失败'''
        self.data['phone'] = int(str(29) + str(self.f.get_number(000000000, 999999999)))
        r = requests.post(url, self.data)
        res = r.json()
        self.assertEqual(10027, res['status'])
        self.assertEqual('phone error', res['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s"  and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.s.execute_sql(sql %(self.data['realname'],self.data['phone']))
        self.assertEqual(0,n)
    def testcase7(self):
        '''输入正确的参数，电话号码12位数添加失败'''
        self.data['phone'] = int(str(13) + str(self.f.get_number(1000000001, 9999999999)))
        r = requests.post(url, self.data)
        res = r.json()
        self.assertEqual(10027, res['status'])
        self.assertEqual('phone error', res['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s"  and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.s.execute_sql(sql % (self.data['realname'], self.data['phone']))
        self.assertEqual(0, n)
    def testcase8(self):
        '''输入正确的参数，电话号码1位数添加失败'''
        self.data['phone'] =2
        r = requests.post(url,self.data)
        res = r.json()
        self.assertEqual(10027, res['status'])
        self.assertEqual('phone error', res['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s"  and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.s.execute_sql(sql % (self.data['realname'], self.data['phone']))
        self.assertEqual(0, n)
    def testcase9(self):
        '''发布会已满时，添加失败'''
        self.data['phone'] = int(str(13) + str(self.f.get_number(000000000, 999999999)))
        self.data['eid'] = 100025
        r = requests.post(url, self.data)
        res = r.json()
        self.assertEqual(10024, res['status'])
        self.assertEqual('event number is full', res['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s"  and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.s.execute_sql(sql % (self.data['realname'], self.data['phone']))
        self.assertEqual(0, n)
    def testcase10(self):
        '''添加嘉宾时发布会状态为0时，添加嘉宾失败'''
        self.data['phone'] = int(str(13) + str(self.f.get_number(000000000, 999999999)))
        self.data['eid'] = 100024
        r = requests.post(url, self.data)
        res = r.json()
        self.assertEqual(10023, res['status'])
        self.assertEqual('event status is not available', res['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s"  and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.s.execute_sql(sql % (self.data['realname'], self.data['phone']))
        self.assertEqual(0, n)
    def testcase11(self):
        '''当发布会不存在时，添加失败'''
        self.data['phone'] = int(str(13) + str(self.f.get_number(000000000, 999999999)))
        self.data['eid'] = 9898989898
        r = requests.post(url, self.data)
        res = r.json()
        self.assertEqual(10022, res['status'])
        self.assertEqual('event id null', res['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s"  and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.s.execute_sql(sql % (self.data['realname'], self.data['phone']))
        self.assertEqual(0, n)
    def testcase12(self):
        '''输入发布会已经开始时，添加嘉宾失败'''
        self.data['phone'] = int(str(13) + str(self.f.get_number(000000000, 999999999)))
        self.data['eid'] = 100026
        r = requests.post(url, self.data)
        res = r.json()
        self.assertEqual(10025, res['status'])
        self.assertEqual('event has started', res['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s"  and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.s.execute_sql(sql % (self.data['realname'], self.data['phone']))
        self.assertEqual(0, n)
    def testcase13(self):
        '''嘉宾电话重复时，添加嘉宾失败'''
        self.data['phone'] = 17721882186
        r = requests.post(url, self.data)
        res = r.json()
        self.assertEqual(10026, res['status'])
        self.assertEqual('the event guest phone number repeat', res['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s"  and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.s.execute_sql(sql % (self.data['realname'], self.data['phone']))
        self.assertEqual(0, n)
    def testcase14(self):
        '''不输入嘉宾电话时，添加嘉宾失败'''
        self.data['phone'] =''
        r = requests.post(url, self.data)
        res = r.json()
        self.assertEqual(10021, res['status'])
        self.assertEqual('parameter error', res['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s"  and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.s.execute_sql(sql % (self.data['realname'], self.data['phone']))
        self.assertEqual(0, n)
    def testcase15(self):
        '''不输入发布会id时，添加嘉宾失败'''
        self.data['eid'] =''
        r = requests.post(url, self.data)
        res = r.json()
        self.assertEqual(10021, res['status'])
        self.assertEqual('parameter error', res['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s"  and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.s.execute_sql(sql % (self.data['realname'], self.data['phone']))
        self.assertEqual(0, n)
    def testcase16(self):
        '''不输入嘉宾姓名时，添加嘉宾失败'''
        self.data['realname'] =''
        r = requests.post(url, self.data)
        res = r.json()
        self.assertEqual(10021, res['status'])
        self.assertEqual('parameter error', res['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s"  and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.s.execute_sql(sql % (self.data['realname'], self.data['phone']))
        self.assertEqual(0, n)
    def testcase17(self):
        '''不输入邮箱时，添加嘉宾失败'''
        self.data['email'] =''
        r = requests.post(url, self.data)
        res = r.json()
        self.assertEqual(10021, res['status'])
        self.assertEqual('parameter error', res['message'])
        sql = 'select * from sign_guest where realname="%s" and phone="%s"  and sign=0;'
        # 验证数据库中嘉宾数据是否正确保存
        n = self.s.execute_sql(sql % (self.data['realname'], self.data['phone']))
        self.assertEqual(0, n)


if __name__ == '__main__':
    unittest.main()