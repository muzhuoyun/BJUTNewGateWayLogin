UserAccount = '替换为学号'
UserPassWord = '替换为密码'

from utils import *

urlDict = {
    'v4Lan': 'https://lgn.bjut.edu.cn',
    'v6': 'https://lgn6.bjut.edu.cn',
    'v46Wlan': 'http://10.21.221.98'
}
url = urlDict['v4Lan']
ipType = 'ipv4&ipv6'
apiPort = '802'

loginCallback = 'dr1005'
logoutCallback = 'dr1008'
loadConfigCallback = 'dr1001'
checkV6Callback = 'dr1004'

loginIpv4 = ''
loginIpv6 = ''
loginVlanid = ''
loginMac = ''
jsVersion = ''

programIndex = ''
pageIndex = ''
loginMethod = ''
acLogout = ''
registerMode = ''

drcomAccount = ''
drcomPassword = ''

secretKey = ''
keyHash = 0

v46s = {
    'ipv6&ipv4': '0',
    'ipv4': '1',
    'ipv6': '2',
}

def getPortalApi():
    return url + f':{apiPort}/eportal/portal'

def createLoadConfigParams():
    return {
        'callback': loadConfigCallback,           
        'program_index': '',      
        'lan_vlan_id': loginVlanid,        
        'wlan_user_ip': loginIpv4,       
        'wlan_user_ipv6': '',     
        'wlan_user_ssid': '',     
        'wlan_user_areaid': '',   
        'wlan_ac_ip': '',         
        'wlan_ap_mac': loginMac,        
        'gw_id': '000000000000',              
        'page_index': '',         
        'jsVersion': jsVersion,          
        'encrypt': '1',
    }

def createCheckV6ready():
    return {
        'callback': checkV6Callback,
        'program_index': programIndex,
        'page_index': pageIndex,
        'jsVersion': '4.2.2',
    }

def createLoginParams():
    return {
        'callback': loginCallback,         
        'login_method': loginMethod,     
        'user_account': ',0,' + UserAccount,     
        'user_password': UserPassWord,    
        'wlan_user_ip': loginIpv4 if 'ipv4' in ipType else '',     
        'wlan_user_ipv6': loginIpv6 if 'ipv6' in ipType else '',   
        'wlan_user_mac': loginMac,    
        'wlan_vlan_id': loginVlanid,     
        'wlan_ac_ip': '',       
        'wlan_ac_name': '',     
        'authex_enable': '',    
        'jsVersion': jsVersion,        
        'login_ip_type': v46s[ipType],    
        'terminal_type': '1',    # pc端：1
        'lang': 'zh-cn',             
        'program_index': programIndex,    
        'page_index': pageIndex,       
        'encrypt': '1'
    }

def createLogoutParams():
    return {
        'callback': logoutCallback,
        'login_method': loginMethod,
        'user_account': drcomAccount,
        'user_password': drcomPassword,
        'ac_logout': acLogout,
        'register_mode': registerMode,
        'wlan_user_ip': loginIpv4,
        'wlan_user_ipv6': loginIpv6,
        'wlan_user_mac': loginMac,
        'wlan_ac_ip': '',
        'wlan_ac_name': '',
        'jsVersion': jsVersion,
        'program_index': programIndex,
        'page_index': pageIndex,
        'encrypt': '1'
    }

def createWlanLdCfgReady():
    return {
        'callback': loadConfigCallback,           
        'program_index': '',      
        'lan_vlan_id': loginVlanid,        
        'wlan_user_ip': b64Encocde(loginIpv4),    
        'wlan_user_ipv6': '',     
        'wlan_user_ssid': '',     
        'wlan_user_areaid': '',   
        'wlan_ac_ip': '',         
        'wlan_ap_mac': loginMac,        
        'gw_id': '000000000000',              
        'page_index': '',         
        'jsVersion': jsVersion,
    }

def createWlanLoginReady():
    return {
        'callback': loginCallback,     
        'login_method': loginMethod,   
        'user_account': UserAccount + '@campus',
        'user_password': UserPassWord, 
        'wlan_user_ip': loginIpv4,     
        'wlan_user_ipv6': '',   
        'wlan_user_mac': loginMac,     
        'wlan_ac_ip': '',       
        'jsVersion': jsVersion,        
        'terminal_type': '1',
        'lang': 'zh-cn',             
    }

def createWlanLogoutReady():
    return {
        'callback': logoutCallback,
        'login_method': loginMethod,
        'user_account': drcomAccount,
        'user_password': drcomPassword,
        'ac_logout': acLogout,
        'register_mode': registerMode,
        'wlan_user_ip': loginIpv4,
        'wlan_user_ipv6': '',
        'wlan_user_mac': loginMac,
        'wlan_ac_ip': '',
        'wlan_ac_name': '',
        'jsVersion': jsVersion,
        'encrypt': '1',
    }