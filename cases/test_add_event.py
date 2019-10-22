import requests
import unittest
from ulit.ulit import BASEURL,Fake_d
from Con_data_base.Connectdata import connect_data
url = BASEURL+'add_event/'
class Test_case(unittest.TestCase):
    '''添加发布会'''
    s = connect_data()
    data = {}
    f = Fake_d()
    def setUp(self):
        self.s.con_mysql()
    def tearDown(self):
        self.s.close_cur()
    def testcase1(self):
        '''输入正确的参数，添加成功'''
        self.data['eid']=self.f.get_number(2000,9000)
        self.data['name'] = 'iphone'+str(self.f.get_number(1,9999))+'发布会'
        self.data['status'] = self.f.get_number(0,1)
        self.data['start_time'] = self.f.get_datetime()
        self.data['address'] = self.f.get_address()
        self.data['limit'] = 500
        r = requests.post(url,self.data)
        res = r.json()
        print(res)
        sql = 'select * from sign_event where id ="%d" and name="%s";'
        self.s.execute_sql(sql)
        #select_result = self.s.execute_sql(cur,sql %(self.data['eid'],self.data['name']))
        if res['message'] == 'add event success':
            print('Pass')
        else:
            print('Fail')


if __name__ == '__main__':
    unittest.main()