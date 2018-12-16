import requests

# Dont forget to port-forward Graylog Server to localhost if server is not running locally
graylog_url = "http://127.0.0.1:12201/gelf"

def  transport(data):
    header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    payload = "{'host':'yahoofinancials_itu.org', 'short_message':'sako'," + str(data).replace('{', '').replace('}', '') + "}".replace('\'', '"')
    response_code=requests.post(graylog_url, data=payload, headers=header)
    if response_code == '202':
        print('Data was successfully sent to Graylog Server')
    else:
        print('Failed to sent data to Graylog Server')