
import random
import base64
import requests, json

def getKey(secretKey):
    ret = 0
    for char in secretKey:
        ret ^= ord(char)
    return ret

def enc_pwd(pass_in, key):
    pass_out = ""
    if pass_in is None or pass_in == "":
        return pass_out
    length = len(pass_in)
    if length > 512:
        return "-1"
    
    for char in pass_in:
        ch = ord(char) ^ key
        str_ch = hex(ch)[2:]
        if len(str_ch) == 1:
            str_ch = "0" + str_ch
        pass_out += str_ch
    
    return pass_out

def process_data(params, keys):
    arr = {}
    for key in params:
        if key == 'encrypt':
            arr[key] = params[key]
        arr[key] = enc_pwd(params[key], keys)
    return arr

def getV():
    return str(int(random.random()* 10000) + 500)

def b64Encocde(x: str):
    return base64.b64encode(x.encode('utf-8')).decode('utf-8')

def wrap(d: dict):
    d['v'] = getV()
    d['lang'] = 'zh'
    return d

def getJsonP(jsonPUrl: str, params: dict):
    r = requests.get(jsonPUrl, params=params)
    return json.loads(r.text.split("(")[1].split(")")[0])

def cleanJSVar(x: str):
    return x.strip().replace("'", '').replace('"', '')