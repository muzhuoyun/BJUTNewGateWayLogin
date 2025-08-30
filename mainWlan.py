from requests.exceptions import ConnectionError, Timeout, HTTPError, SSLError, RequestException
import context as CT
from lgn import *
import argparse

parser = argparse.ArgumentParser(description="BJUT new natgate login script.")

parser.add_argument("-t", "--ipType", type=str, help="IP type. 'ipv6&ipv4' or 'ipv6'.", default='ipv6&ipv4', choices=["ipv6&ipv4", "ipv6"], required=False)
parser.add_argument("--logout", action="store_true", help="Logout Gateway.")

def loginWlan(v46):
    CT.ipType = v46
    if CT.ipType == 'ipv6':
        CT.url = CT.urlDict['v6']
    else:
        CT.url = CT.urlDict['v46Wlan']
    initLgn()
    loadConfig()
    login()

def logoutWlan():
    CT.url = CT.urlDict['v46Wlan']
    initLgn()
    loadConfig()
    logout()

if __name__ == '__main__':
    args = parser.parse_args()
    try:
        loginWlan('ipv6&ipv4')
        logoutWlan()
        if not args.logout:
            loginWlan(args.ipType)
    except SSLError as e:
        print("[SSL] 证书校验失败：", e)
    except Timeout as e:
        print("[TIMEOUT] 请求超时：", e)
    except ConnectionError as e:
        print("[CONNECT] 网络或 DNS 错误：", e)
    except HTTPError as e:
        print("[HTTP]", e.response.status_code, e.response.reason)
    except RequestException as e:
        print("[OTHER] 未知异常：", e)