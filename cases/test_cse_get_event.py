import requests
import unittest
import pymysql
from ulit.ulit import BASEURL
from Con_data_base.Connectdata import connect_data
url = BASEURL+'sec_get_event_list/'
class Test_case(unittest.TestCase):
    '''有用户验证的情况下查询发布会'''
    s = connect_data()
    data = {}
    data['eid'] = 1231231
    def setUp(self):
        self.s.con_mysql()
    def tearDown(self):
        self.s.close_cur()
    def testcase1(self):
        '''输入正确的用户名，密码，参数，查询成功'''
        r = requests.get(url, self.data,auth = ('useer6', 'Sys123456'))
        res = r.json()
        sql = 'select * from sign_event where id ="%d";'
        self.s.execute_sql(sql)
        select_result = self.s.execute_sql(sql %self.data['eid'])

        try:
            self.assertEqual(select_result,1)
            self.assertEqual(200, res['status'])
            self.assertEqual('success', res['message'])
        except:
            raise Exception
    def testcase2(self):
        '''输入错误的用户名，密码，参数，查询失败'''
        r = requests.get(url, self.data, auth=('user6', 'Sys123456'))
        res = r.json()
        sql = 'select * from sign_event where id ="%d";'
        self.s.execute_sql(sql)
        select_result = self.s.execute_sql(sql % self.data['eid'])
        try:
            self.assertEqual(select_result, 1)
            self.assertEqual(10012, res['status'])
            self.assertEqual('user auth fail', res['message'])
        except:
            raise Exception
    def testcase3(self):
        '''用户名为空，查询失败'''
        r = requests.get(url, self.data, auth=('', 'Sys123456'))
        res = r.json()
        sql = 'select * from sign_event where id ="%d";'
        self.s.execute_sql(sql)
        select_result = self.s.execute_sql(sql % self.data['eid'])
        try:
            self.assertEqual(select_result, 1)
            self.assertEqual(10012, res['status'])
            self.assertEqual('user auth fail', res['message'])
        except:
            raise Exception
    def testcase4(self):
        '''密码为空，查询失败'''
        r = requests.get(url, self.data, auth=('useer', ''))
        res = r.json()
        sql = 'select * from sign_event where id ="%d";'
        self.s.execute_sql(sql)
        select_result = self.s.execute_sql(sql % self.data['eid'])
        try:
            self.assertEqual(select_result, 1)
            self.assertEqual(10012, res['status'])
            self.assertEqual('user auth fail', res['message'])
        except:
            raise Exception
    def testcase5(self):
        '''密码错误，查询失败'''
        r = requests.get(url, self.data, auth=('useer', 's'))
        res = r.json()
        sql = 'select * from sign_event where id ="%d";'
        self.s.execute_sql(sql)
        select_result = self.s.execute_sql(sql % self.data['eid'])
        try:
            self.assertEqual(select_result, 1)
            self.assertEqual(10012, res['status'])
            self.assertEqual('user auth fail', res['message'])
        except:
            raise Exception
    def testcase6(self):
        '''不输入eid，查询失败'''
        self.data['eid']=''
        r = requests.get(url, self.data, auth=('useer6', 'Sys123456'))
        res = r.json()
        sql = 'select * from sign_event where id ="";'
        self.s.execute_sql(sql)
        select_result = self.s.execute_sql(sql)
        try:
            self.assertEqual(select_result, 0)
            self.assertEqual(10021, res['status'])
            self.assertEqual('parameter error', res['message'])
        except:
            raise Exception
    def testcase7(self):
        '''输入不存在的eid，查询失败'''
        self.data['eid']='12131231'
        r = requests.get(url, self.data, auth=('useer6', 'Sys123456'))
        res = r.json()
        sql = 'select * from sign_event where id ="%d";'
        self.s.execute_sql(sql)
        select_result = self.s.execute_sql(sql % int(self.data['eid']))
        try:
            self.assertEqual(select_result, 0)
            self.assertEqual(10022 ,res['status'])
            self.assertEqual('query result is empty',res['message'])
        except:
            raise Exception
    def testcase8(self):
        '''输入正确的eid不存在的name，查询成功'''
        self.data['name']='收集售机'
        r = requests.get(url, self.data, auth=('useer6', 'Sys123456'))
        res = r.json()
        sql = 'select * from sign_event where id ="%d";'
        self.s.execute_sql(sql)
        select_result = self.s.execute_sql(sql % int(self.data['eid']))
        try:
            self.assertEqual(select_result, 1)
            self.assertEqual(200 ,res['status'])
            self.assertEqual('success',res['message'])
        except:
            raise Exception
    def testcase9(self):
        '''只输入用户名与密码'''
        r = requests.get(url, auth=('useer6', 'Sys123456'))
        res = r.json()
        try:
            self.assertEqual(10021 ,res['status'])
            self.assertEqual('parameter error',res['message'])
        except:
            raise Exception
if __name__ == '__main__':
    unittest.main()