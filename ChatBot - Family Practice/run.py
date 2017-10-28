# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
import untangle

from twilio.twiml.messaging_response import MessagingResponse, Body, Message
global question
question = 0
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	Questions = ["Are you currently employed?",
             "Are you currently in a stable house?",
             "Is your education going well?",
             "Another Question",
             "A last Question"]

	resp = MessagingResponse()
	message_body = request.form['Body']
	print message_body
	if (message_body.lower() == "start"):
		resp.message(Questions[0])
		return str(resp)
	elif(message_body.lower() == "yes"):
		resp.message(Questions[1])
		return str(resp)
	elif(message_body.lower() == "reset"):
		question = 0
		return str(res)
	else:
		resp.message("A Case Manager will be in contact with you soon")
		question = 5
		return str(resp)


if __name__ == "__main__":
	app.run(debug=True)
