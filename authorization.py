#this is for security purpose  --> hidden is authorizaion token and check he expiry data.
# Are toekns
# IRIS 
# ADMIN
# MINE --> when doing dev
#api or token sirf req ke according hi expose hoga.._> iss tym pe db mein api token ka set karte hain ki kitne din ke liye den ahia

from flask_httpauth import HTTPTokenAuth

auth = HTTPTokenAuth(scheme='Bearer')

tokens = { #token : name
    "ea0c369eceef8c6adc28c0b12538d98564696a7623dad225536a6274a730ab5f5fd9e943643879854e7858d6bf232cf12ca4e14b0119b88a7ba0ebf8b57937e2": "muskan", 
    "4e228f45844e7f7b0d69a7a1cd0931f7f80fe07a0ee245c4facfbeef5d5f7903ff8ad7bb5a9ea15a3ac839f0228d4459b9a2715cbfbc9d9aafbcbb968a4169d7": "preetam"
} # have added the tokens

@auth.verify_token  #tocken dekh raha hai jo api se araha hai woh present hai yah nahi
#return two things, either token or the username
def verify_token(token):
    if token in tokens:
        print(tokens[token])
        return tokens[token]  #only do yah toh true/false or token ke bearer ka name

#lengthier the token more secure

