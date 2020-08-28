import flask, json

server = flask.Flask(__name__)  # __name__代表当前的python文件。把当前的python文件当做一个服务启动

'''
只有在函数前加上@server.route (),这个函数才是个接口，不是一般的函数
第一个参数就是路径,第二个参数支持的请求方式，不写的话默认是get
'''
@server.route('/rate', methods=['POST'])
def index():
    res = {'msg': '这是我开发的第一个接口', 'msg_code': 0, 'json_data': '0'}
    return json.dumps(res, ensure_ascii=False)

'''
debug=True，在代码进行修改后，程序会自动重新加载，不用再次运行。
也就是运行一次即可，即使改动代码，也不需要重启服务
'''
server.run(port=15958, debug=True, host='0.0.0.0')
