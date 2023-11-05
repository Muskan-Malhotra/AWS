import os
from text_extraction import text_extraction
from flask import Flask, request
from authorization import auth

app = Flask(__name__)
file_dir = "./input_files"


@app.route("/greet")
# @auth.login_required
def hello():
    return {
        "Hello, World!":"123"
    }

######################## HW For name and surname
@app.route('/get_details/<first_name>/<last_name>',methods=['POST'])
def getDetails(first_name=None, last_name=None):
  return 'Hi! I am ' + first_name + ' ' + last_name


@app.route('/get_data',methods=['POST'])  #aar ispe login req nahi dala toh yeh walla api working rahega bina token ke
# @auth.login_required
def getData():
    file = request.files['file']
    filePath = os.path.join(file_dir,file.filename)
    file.save(filePath)
    data = text_extraction(filePath)
    print(file.filename)
    return data  #return convention JSON/string

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True) 
     #accessible from all server and all ips
     #code mein koi bhi changes to server automaticllay start hota hai..
     # production ke tym pe debug = false rakhte hain..agar new api bana rahe hai n toj server stop karna hotahai
    #  hain toh don't run in automatic server refresh 