from app import app,db
from flask import render_template, request, jsonify
from app.model import User
from werkzeug.security import check_password_hash

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
            user=User.query.filter_by(username=username).first()
            btn=''+btext
            if btn=='Add':
                if user is not None and check_password_hash(user.password,password):
                    msg="Credentials are already in the database!"
                if user is not None and not check_password_hash(user.password,password):
                    msg="Username already in use! Please choose a different username!"
                if user is None:
                    newUser=User(username,password)
                    db.session.add(newUser)
                    db.session.commit()
                    msg="New user successfully added to database!"
                return jsonify({'data':msg})
            if btn=='Check':
                if user is not None and check_password_hash(user.password,password):
                    msg="Credentials exist in the database!"
                else:
                    msg="Credentials do not exist within database!"
                return jsonify({'data':msg})

        
    return render_template('login.html')

