import pymysql
class connect_data():
    def con_mysql(self):
        global con,cur
        try:
            con = pymysql.connect('localhost','root','root','learn')
        except:
            print('连接数据库失败，请检查连接参数')
        else:
            cur = con.cursor()#创建游标
        return con , cur
    def execute_sql(self,sql):
        return cur.execute(sql)
    def close_cur(self):
        cur.close()
        con.commit()
