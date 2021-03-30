import sys
import logging.config
import json

from send_mail import MailSender
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route("/sendmail", methods=["POST"])
def test_functions():

    try:
        request_body = json.loads(request.data)
        
        plaintext = request_body["plaintext"]
        asunto = request_body["asunto"]
        sender = request_body["sender"]
    
        print("REQ: "+str(request_body))
        result = {
                    "option": "EMAIL",
                    "visibleContext":request_body["visibleContext"],
                    "openContext":request_body["openContext"],
                    "hiddenContext":request_body["hiddenContext"]        
        }
        info = request_body["info"]

        data = {
            'sessionCode': info["sessionCode"],
            'name': request_body["text"]
        }

        ourmailsender = MailSender('info.eva.everis@gmail.com', 'sbjhvaqwgjcuvwsz', ('smtp.gmail.com', 587))
        ourmailsender.set_message(plaintext, asunto, sender)
        #ourmailsender.set_recipients([request_body["text"]])        
        ourmailsender.connect()
        ourmailsender.send_all()
    except:
        logging.exception("Unexpected error parsing payload: %s ", sys.exc_info()[0])
        result = "Error..."

    print(result)
    return result


if __name__ == "__main__":
    #start_logging_conf()    
    app.run(debug=True, port=8002)
    #test_functions()
