import json
from app import app
from flask import render_template, request, jsonify

@app.route('/', methods=['GET'])
def login():
    if request.is_json:
        btext=request.args.get('btn_text')
        username=request.args.get('username')
        password=request.args.get('password')
        print(username, password, btext)

        
    return render_template('login.html')

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)