import os, sys
from flask import Flask, request
from utils import wit_response
from pymessenger import Bot
from konlpy.tag import Twitter

twitter = Twitter

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAZAfvkVBy8sBADgMzL6jSYK77kEOPRupeQOzsCS12qJN5CmyvcyLsBLseIiA5xqQKAuuDABEWEzEcgld0mGh0NGgCCfPniZCy9OgN87YL13npeAGAqIZC6sPuQxLMiEh9Q2ZB4yxSdcVmpyGT2PeWDltaC7SK0x7Qxd4ifxTiO2xZAp0m8UQ"

bot = Bot(PAGE_ACCESS_TOKEN)

@app.route('/', methods=['GET'])
def verify():
    # Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)
    
    if data ['object'] == 'page' :
        for entry in data ['entry']:
            for messaging_event in entry['messaging']:
                
                # Ids
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']
                
                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    else:
                        messaging_text = 'no text'
                        
                        
                    #Echo
                    #response = messaging_text
                    #response = None
                   
                   
                    ''' wit.ai 처리방식
                    entity, value = wit_response(messaging_text)
                    
                    if entity == 'midrate':
                        response = "ok. i will send you {} news".format(str(value))
                    elif entity == "api":
                        response = "Ok. Som you live in {0}. I will send you top headlines from {0}".format(str(value))
                        
                    if response == None:
                        response = messaging_text
                    '''                        
                    ko_message = twitter_korean.normalize(messaging_text)
                    tokens_text = twitter_korean.tokenize(ko_message)
                    
                    response = tokens_text
                                            
                                            
                                            
                    bot.send_text_message(sender_id, response)
                
    
    
    return "ok", 200
    
def log(message):
    print(message)
    sys.stdout.flush()
    
    
if __name__ == "__main__":
    app.run(debug = True, port = 80)
    