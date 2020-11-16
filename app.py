from flask import Flask,render_template,jsonify,request
from flask_cors import CORS
import pymysql
import json


# 声明app 强指定文件路径
app = Flask(__name__,
            static_folder = "./geof/dist/static",
            template_folder = "./geof/dist")
cors = CORS(app, resources={"/api/*": {"origins": "*"}})
#密钥 字符串
app.secret_key = 'secretkey'


# 连接数据库
db = pymysql.connect(host='localhost', user='root', password='lyz0704.', database='demo', port=3306)
cursor = db.cursor()


# 将所有路由指向index.html
@app.route('/', defaults={'path':' '})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

            
@app.route('/login', methods=['POST'])
def login ():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        username = data['username']
        password = data['password']
        print(username,password)
        cursor.execute("select id,username,password from admin where username=\""+str(username)+"\" and password=\""+str(password)+"\"")
        data = cursor.fetchone()
        if(data!=None):
            print("result:",data)
            response = '登陆成功'
            return jsonify(response)
        else:
            response = '登录失败'
            return jsonify(response)


@app.route('/register', methods=['POST'])
def register ():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        username = data['username']
        password = data['password']
        cpassword = data['cpassword']
        print(username,password,cpassword)
        if (password != cpassword):
            return jsonify("密码输入不一致！")
        else:
            cursor.execute("INSERT INTO admin (username,password) values (\""+str(username)+"\",\""+str(password)+"\")")
            db.commit()
            return jsonify("注册成功！")    
    else:
        pass


@app.route('/api/get_geojson', methods=['POST'])
def get_geojson():
    if request.method == 'POST':
        f = open("beijing.json", encoding="utf8")
        data = json.loads(f.read())
        return jsonify(data)
    else:
        pass


@app.route('/dbscan', methods=['POST'])
def dbscan ():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        # 从前端获取dbscan的参数
        radius = data['eps']
        mins = data['mins']
        import numpy as np
        import geojson
        import json
        from sklearn.cluster import DBSCAN
        from sklearn import metrics
        from sklearn.datasets import make_blobs
        from sklearn.preprocessing import StandardScaler
        eps = float(radius)
        min_samples = int(mins)
        # 读取测试文件
        import pandas as pd
        testdata = pd.read_csv("test1.csv")
        array_data = np.array(testdata)#np.ndarray()
        X = array_data
        db = DBSCAN(eps=eps, min_samples=min_samples).fit(X)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        labels = db.labels_
        # labels 即聚类结果的标签,-1为噪声,格式为ndarray
        
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise_ = list(labels).count(-1)
        result = ('聚类数: ' + str(n_clusters_) + '\n噪声数:' + str(n_noise_))
        # 转换格式
        xy_list = X.tolist()
        data = geojson.MultiPoint(xy_list)
        label_list = labels.tolist()
        return jsonify(result, data ,label_list)


if __name__ == '__main__':
    app.run(debug = True)

