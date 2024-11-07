from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import SparkApi  # 确保你的项目中有这个模块，或者修改成正确的API调用
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import spacy
from cities_list import cities_list  # 导入城市列表
from datetime import datetime

app = Flask(__name__, static_folder='templates', static_url_path='')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# AI API配置
appid = "71379edd"
api_secret = "MWM3MWRmZWQ4NjU2YWYyZDk1MWRhYjgx"
api_key = "89bc3442f70485aebc01105df997f74d"
domain = "lite"
Spark_url = "wss://spark-api.xf-yun.com/v1.1/chat"
text = []
# 加载数据
try:
    df = pd.read_csv('data/data.csv')
except FileNotFoundError:
    print("data.csv 文件未找到。请确保文件存在并在正确路径中。")
    raise

# 加载spaCy中文模型
try:
    nlp = spacy.load('zh_core_web_sm')
except Exception as e:
    print(f"加载spaCy模型时发生错误: {e}")
    raise

# 特征提取
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['简介'])

# 建立模型
model = NearestNeighbors(n_neighbors=10, algorithm='auto')
model.fit(X)

def getText(role, content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text

def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length

def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text

# 解析城市函数
def parse_city(user_input):
    doc = nlp(user_input)
    for ent in doc.ents:
        if ent.label_ == 'GPE':
            print(f"识别到的城市: {ent.text}")  # 输出城市信息
            return ent.text
    return None

# 检查城市是否在列表中
def check_city_in_list(city):
    return city in cities_list

# 检查日期格式、人数、预算和时间
def validate_inputs(departure, destination, date, days, people, budget):
    errors = []  # 初始化 errors 列表
    if not check_city_in_list(departure):
        errors.append(f"出发地 '{departure}' 不在城市列表中。")
    if not check_city_in_list(destination):
        errors.append(f"目的地 '{destination}' 不在城市列表中。")
    
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        errors.append("日期格式不正确，应为 YYYY-MM-DD。")
    
    # 将 days、people 和 budget 转换为整数以进行比较
    try:
        days = int(days)
        people = int(people)
        budget = int(budget)
        
        if days <= 0:
            errors.append("游玩天数必须大于0。")
        if people <= 0:
            errors.append("出行人数必须大于0。")
        if budget <= 0:
            errors.append("人均预算必须大于0。")
    except ValueError:
        errors.append("游玩天数、出行人数和预算应为有效的数字。")

    return errors  # 返回 errors 列表

# 推荐函数
def recommend(place, model, data):
    vec = vectorizer.transform([place])
    distances, indices = model.kneighbors(vec)
    recommendations = data.iloc[indices[0]]
    
    city = parse_city(place)
    print(f"输入的城市: {city}")  # 输出解析到的城市
    
    if city:
        recommendations = recommendations[recommendations['城市'] == city]
        print(f"找到的推荐景点:\n{recommendations[['景点名称', '简介']]}")  # 输出找到的推荐景点
    
    formatted_recommendations = recommendations[['景点名称', '简介']]
    return formatted_recommendations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plan_trip', methods=['POST'])
def plan_trip():
    try:
        # user_input = request.json['input']

        data = request.json
        print("Received data:", data)  # 调试输出

        errors = validate_inputs(
            data['departure'], data['destination'], data['date'], 
            data['days'], data['people'], data['budget']
        )
        if errors:
            print("Validation errors:", errors)
            return jsonify({'error': '输入错误', 'messages': errors}), 400

        user_input = f"请帮我规划一个行程，从{data['departure']}出发，到{data['destination']}，出发日期为{data['date']}，计划游玩{data['days']}天，同行人数为{data['people']}人，人均预算{data['budget']}元。"
        print("Generated user input:", user_input)  # 调试输出
        question = checklen(getText("user", user_input))
        SparkApi.answer = ""
        SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
        ai_response = SparkApi.answer
        getText("assistant", ai_response)
        
        recommendations = recommend(data['destination'], model, df)
        recommendations_list = recommendations.to_dict(orient='records')
        
        return jsonify({'ai_response': ai_response, 'recommendations': recommendations_list})
    except Exception as e:
        print(f"处理请求时发生错误: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
