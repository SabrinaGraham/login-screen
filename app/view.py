from app import app
from flask import render_template, request, jsonify
from app.model import User

@app.route('/', methods=['GET','POST'])
def login():
    global btext, username, password
    if request.is_json:
        if request.method=='GET':
            btext=request.args.get('btn_text')
            username=request.args.get('username')
            password=request.args.get('password')
            print(username, password, btext)
        if request.method=='POST':
            #user=User.query.filter_by(username=username).first()
            btn=''+btext
            if btn=='Add':
                print('Add button clicked')
                return jsonify({'msg':'Add button clicked'})
            if btn=='Check':
                print('Check button clicked')

        
    return render_template('login.html')

