#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json, requests
from DBTools.Operate_DB import OperateDB
from json_data.format_fs import FormatFuncs
import time


def main():
    '''
    1、获取用例数据，read数据库
    2、循环
            用查到的数据，替换原来的json，组成新的json,
            request
            获取response
            写入数据库
    '''

    input_string = input("请输入要测试的费率模板编号，以空格分隔，以回撤结束\n")
    input_slist = input_string.split()
    file_codes = list(map(int, input_slist))
    #print(type(file_codes))
    if len(file_codes) == 0:
        file_codes = [10, 11, 12, 13, 20, 21, 22, 30, 31]
    conn = OperateDB()
    for code in file_codes:
        print('---即将执行编号{}费率模板对应的用例---'.format(code))
        rate_file = r'../json_data/rate_request{}.json'.format(code)
        json_rate = FormatFuncs(json_file=rate_file).json_dic
        sql = 'select * from cases_rate where id between {} and {}'.format(code*10000,(code+1)*10000)
        #print(sql)
        data = conn.searchAll(sql)
        for i in data:
            id = i[0]
            inTime = i[1]
            outTime = i[2]
            prediction = i[3]

            json_rate['inTime'] = inTime
            json_rate['outTime'] = outTime
            #json_req = json.dumps(json_rate)
            #print(json_rate)
            res = requests.post(url='http://58.214.27.26:8888/member/anon/rate', json=json_rate)
            response = json.loads(res.text)["data"]["amount"]
            if(response!=None):
                response = int(response/100)
            result = 0
            if response == prediction:
                result = 1

            ######打印错误结果#######
            if result == 0:
                print('result={},inTime={},outTime={},prediction={},response={}'.format(result,inTime,outTime,prediction,response))

            # print(res.text,type(res.text))
            upsql = conn.update_sql('cases_rate', result=result, response=response,
                                    modifiedTime='CURRENT_TIMESTAMP') + conn.kw_link('AND', id=id)
            # print(upsql)
            conn.update_yty(upsql)
            # insql = 'insert into operation (case_id,operate_time,result)values('+str(id)+','+'CURRENT_TIMESTAMP,'+str(result)+')'
            insql = 'insert into operation (case_id,operate_time,result)values(%s,%s,%s)'

            conn.cursor.execute(insql, (str(id), time.strftime('%Y-%m-%d %H:%M:%S'), str(result)))

    conn.conn.commit()
    conn.cursor.close()


if __name__ == '__main__':
    main()
    print('*****执行结束*****')
