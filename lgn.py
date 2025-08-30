
import requests
from bs4 import BeautifulSoup
import re
from time import sleep
from utils import *
import context as CT

def initLgn():
    initUrl = CT.url + '/a79.htm'
    response = requests.get(initUrl)
    soup = BeautifulSoup(response.text, 'html.parser')
    script_tags = soup.find_all('script')
    def_script = script_tags[0].string
    ver_script = script_tags[-3].string
    pattern = r'(\w+)\s*=\s*([^;]+);'
    patternVar = r'var\s+(\w+)\s*=\s*([^;]+);'
    matches = re.findall(pattern, def_script)
    Version = re.findall(patternVar, ver_script)[0][1]
    variables = {}
    for var_name, value in matches:
        variables[var_name] = value
    if CT.ipType == 'ipv6':
        CT.loginIpv6 = cleanJSVar(variables['v46ip'])
    else:
        CT.loginIpv4 = cleanJSVar(variables['v46ip'])
    CT.loginMac = cleanJSVar(variables['ss4'])
    CT.loginVlanid = cleanJSVar(variables['vlanid'])
    a41Url = CT.url + '/' + [script.get('src') for script in script_tags if script.get('src')][0]
    responseA41 = requests.get(a41Url)
    matches = re.findall(patternVar, responseA41.text)
    if 'https' in CT.url:
        CT.secretKey = [cleanJSVar(x[1]) for x in matches if x[0] == 'secret_key'][0]
        CT.apiPort = [int(x[1]) for x in matches if x[0] == 'enHTTPSPort'][0]
    else:
        CT.apiPort = [int(x[1]) for x in matches if x[0] == 'epHTTPPort'][0]
    a40Url = CT.url + '/a40.js?v=_' + Version
    responseA40 = requests.get(a40Url)
    responseA40Text = responseA40.text
    CT.jsVersion = responseA40.text.split("var jsVersion='")[1].split("'")[0]
    pattern = r"'user_account':\s*'([^']*)'\s*,\s*'user_password':\s*'([^']*)'"
    match = re.search(pattern, responseA40Text)
    CT.drcomAccount = match.group(1)
    CT.drcomPassword = match.group(2)

def loadConfig():
    if 'https' in CT.url:
        CT.keyHash = getKey(CT.secretKey)
        ldCfgReady = process_data(CT.createLoadConfigParams(), CT.keyHash)
    else:
        ldCfgReady = CT.createWlanLdCfgReady()
    loadConfigUrl = CT.getPortalApi() + '/page/loadConfig'
    configData = getJsonP(loadConfigUrl, wrap(ldCfgReady))['data']
    CT.loginMethod = configData['login_method']
    CT.programIndex = configData['program_index']
    CT.pageIndex = configData['page_index']
    CT.acLogout = configData['ac_logout']
    CT.registerMode = configData['register_mode']

def checkV6():
    checkV6Url = CT.urlDict['v6'] + '/drcom/getipv6'
    checkV6Data = getJsonP(checkV6Url, wrap(CT.createCheckV6ready()))
    if checkV6Data["result"] == 1:
        CT.loginIpv6 = checkV6Data['ip']

def login():
    if 'https' in CT.url:
        loginReady = process_data(CT.createLoginParams(), CT.keyHash)
    else:
        loginReady = CT.createWlanLoginReady()
    loginUrl = CT.getPortalApi() + '/login'
    loginData = getJsonP(loginUrl, wrap(loginReady))
    print(loginData['msg'])

def logout():
    if 'https' in CT.url:
        logoutReady = process_data(CT.createLogoutParams(), CT.keyHash)
    else:
        logoutReady = CT.createWlanLogoutReady()
    logoutUrl = CT.getPortalApi() + '/logout'
    logoutData = getJsonP(logoutUrl, wrap(logoutReady))
    print(logoutData['msg'])

