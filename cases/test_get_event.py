import requests
import unittest
from ulit.ulit import BASEURL
from Con_data_base.Connectdata import connect_data
url = BASEURL+'get_event_list/'
class Test_case(unittest.TestCase):
    '''查询发布会'''
    s = connect_data()
    data ={'eid':1002}
    def setUp(self):
        self.s.con_mysql()
    def tearDown(self):
        self.s.close_cur()
    def testcase1(self):
        '''查询数据库中id为1002的发布会'''
        r = requests.get(url,self.data)
        res = r.json()
        print(res)
        sql = 'select * from sign_event where id =1002 ;'
        self.s.execute_sql(sql)
        if res['status']==10000:
            print('Pass')
        else:
            print('Fail')


if __name__ == '__main__':
    unittest.main()