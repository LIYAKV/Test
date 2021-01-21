from flask import Flask, jsonify
from flask import render_template
import mysql.connector
from flask import request

condb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='112233',
    database='db1'
)

newcursor=condb.cursor(dictionary=True, buffered=True)
app = Flask(__name__)

@app.route('/')
def hello_world():
    dict1 = {'name':"yoyo",'phone':123123}
    return jsonify(dict1)
    
@app.route('/hello/')
def hello():
    newcursor.execute("SELECT * from test")
    users_list = newcursor.fetchall()
    print(users_list)
    return render_template('index.html',name=users_list)
    

@app.route('/link/')
def link():
    return render_template('add.html')


@app.route('/add/',methods=["POST"])
def add():
    name=request.form['name12']
    phone=request.form['phone']
    date=request.form['date']
    address=request.form['address']
    values=(name,phone,date,address)
    sql = "INSERT INTO test(name1,phone,date1,address) VALUES(%s,%s,%s,%s)"  
    newcursor.execute(sql,values)
    condb.commit()
    return 'helloooo'

    
