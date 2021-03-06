#!/usr/bin/env python

import urllib
import json
import os
import constants
import accounts

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

PERSON = constants.TEST_1

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "account-balance":
        return constants.ERR_DICT(req.get("result").get("action"))

    result = req.get("result")
    parameters = result.get("parameters")
    acct = parameters.get("account-type")
    acct = acct.strip()
    if acct=='401k':
        acct='WI'

    qual = parameters.get("qualifier")

    speech = str(req.get("result").get("action"))

    if acct:
        if acct in constants.ACCT_TYPES:
            speech = "The value of your {ACCT_TYPE} accounts is {VALU} dollars.".format(VALU=accounts.get_balance(PERSON, acct), ACCT_TYPE=acct)
        else:
            speech = "You don't have any accounts of that type. The total value of your other accounts is {VALU} dollars.".format(
                VALU=accounts.get_balance(PERSON))
    elif qual:
        speech = "The total value of your accounts is {VALU} dollars.".format(VALU=accounts.get_balance(PERSON))
    else:
        speech = "The total value of your accounts is {VALU} dollars.".format(VALU=accounts.get_balance(PERSON))

    # speech = "The cost of shipping to " + zone + " is " + str(cost[zone]) + " euros."

    print("Response:")
    print(speech)

    speech += "\nAnything else I can help you with today?"

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "home"
    }



if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
