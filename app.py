import requests
import rotate_proxy_agent as prx
import traceback
import time

RETRY_LIMIT = 30
TIMEOUT = 10  #Seconds

SESSION = requests.Session()
URL = "https://www.google.com"


def send_request(url):
    bad_proxies,proxies = [],None
    retry,retry_cnt,response_status = True,0,0
    #time.sleep(1)
    while retry:
        try:
            retry_cnt += 1
            match,proxies,headers = prx.get_proxy_headers(bad_proxies);
            response = SESSION.get(url,headers=headers,proxies=proxies,timeout=TIMEOUT)
            response_status = response.status_code
        except:
            #print('>ERROR:',traceback.format_exc())
            retry = True
            bad_proxies.append(proxies)

        print('response_status:',response_status)
            
        if response_status == 200:
            retry = False
        else:
            retry = True
        if retry_cnt >= RETRY_LIMIT:
            retry = False            
    return response


if __name__ == "__main__":
    response = send_request(URL)
    
