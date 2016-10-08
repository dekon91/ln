from flask import Flask, request
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"
# callback for Webhook
@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded["events"][0]['replyToken']
    #id=[d['replyToken'] for d in user][0]
    #print(json_line)
    print("User:",user)
    sendText(user,'WTF?') # send message "WTF?"
    return '',200

def sendText(user, text):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'AP17YidoPSuuJqIxCDRWbE3ySmBtYLgxDRBF8j+Rywxa1JbehnO7CTW9GFTt4wbXhfnFxGl0KbQLI4ev+PmOOIZrjNo6PbM8PN0z5DxFAhPhIb+OujIYJDDbqI4F2eU4FIMu7mqSe2yeFUlS6E2xkwdB04t89/1O/w1cDnyilFU=' # put ENTER_ACCESS_TOKEN here
    #AP17YidoPSuuJqIxCDRWbE3ySmBtYLgxDRBF8j+Rywxa1JbehnO7CTW9GFTt4wbXhfnFxGl0KbQLI4ev+PmOOIZrjNo6PbM8PN0z5DxFAhPhIb+OujIYJDDbqI4F2eU4FIMu7mqSe2yeFUlS6E2xkwdB04t89/1O/w1cDnyilFU=
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = json.dumps({
        "replyToken":user,
        "messages":[{
            "type":"text",
            "text":text
        }]
    })

    #print("Data",data)
    r = requests.post(LINE_API, headers=headers, data=data) # send data
    #print(r.text)

if __name__ == '__main__':
     app.run(debug=True)

# any problem goes here!
#https://developers.line.me/messaging-api/getting-started#apply_messagingapi
