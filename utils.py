from wit import Wit

access_token = "KO2F7MZNIOGR4IP3ENW2KCAVEZWVGSFJ"

client = Wit(access_token = access_token)

def wit_response(message_text):
    resp = client.message(message_text)
    entity = None
    value = None
    
    try:
        entity = list(resp['entities'])[0]
        value = resp['entities'][entity][0]['value']
    except:
        pass
    return (entity, value)




#print(wit_response("미드레이트는 어떤회사인가요?"))