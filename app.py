from flask import Flask, render_template, jsonify, request, abort
from flask import current_app as app
from flask_cors import CORS
import pymysql
import json
import os


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

# 文件上传保存路径
temp_base = os.path.expanduser("./bigfiles")

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


def get_chunk_name(uploader_filename, chunk_number):
    return uploader_filename + "_part_%03d" %chunk_number


# 获取分片信息
@app.route('/api/upload', methods=['GET'])
def getChunkInfo ():
    if request.method == 'GET':
        identifier = request.args.get('identifier', type=str)
        fileName = request.args.get('fileName', type=str)
        chunkNumber = request.args.get('chunkNumber', type=int)
    
        if not identifier or not fileName or not chunkNumber:
            abort(500, 'Parameter error')
        #PATH DEFINE
        temp_dir = os.path.join(temp_base, identifier)
        #getchunkname将filename和chunkNumber拼接并格式化
        chunk_file = os.path.join(temp_dir, get_chunk_name(fileName, chunkNumber))
        app.logger.debug('Getting chunk: %s', chunk_file)
    
        if os.path.isfile(chunk_file):
            return jsonify('chunk %s OK', chunkNumber)
        else:
            abort(404, 'Not Found')


#接收上传的文件并保存
@app.route('/api/upload', methods=['POST'])
def upLoading():
    if request.method == 'POST':
        totalChunks = request.form.get('totalChunks', type=int)
        chunkNumber = request.form.get('chunkNumber', default=1, type=int)
        fileName = request.form.get('fileName', default='error', type=str)
        identifier = request.form.get('identifier', default='error', type=str)

        if not identifier or not fileName or not chunkNumber or not totalChunks:
            print("参数错误")
    
        chunk_data = request.files["file"]
        temp_dir = os.path.join(temp_base, identifier)
        if not os.path.isdir(temp_dir):
            os.makedirs(temp_dir, mode=0o777)
            print("path created")
        #getchunkname将filename和chunkNumber拼接并格式化
        chunk_name = get_chunk_name(fileName, chunkNumber)
        chunk_file = os.path.join(temp_dir, chunk_name)
        chunk_data.save(chunk_file)
        app.logger.debug('Saved chunk: %s', chunk_file)
    
        chunk_paths = [os.path.join(temp_dir, get_chunk_name(fileName, x)) for x in range(1, totalChunks+1)]
        upload_complete = all([os.path.exists(p) for p in chunk_paths])
    
        if upload_complete:
            target_file_name = os.path.join(temp_base, fileName)
            with open(target_file_name, "ab") as target_file:
                for p in chunk_paths:
                    stored_chunk_file_name = p
                    stored_chunk_file = open(stored_chunk_file_name, 'rb')
                    target_file.write(stored_chunk_file.read())
                    stored_chunk_file.close()
                    os.unlink(stored_chunk_file_name)
            target_file.close()
            os.rmdir(temp_dir)
            app.logger.debug('File saved to: %s', target_file_name)
        return jsonify("Upload complete")


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

