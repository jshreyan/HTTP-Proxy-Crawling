import requests
import rotate_proxy_agent as prx

s = requests.Session()
RETRY_LIMIT = 30

def send_request(url):
    bad_proxies,proxies = [],None
    retry,retry_cnt,response_status = True,0,0
    time.sleep(2)
    while retry:
        try:
            retry_cnt += 1
            match,proxies,headers = prx.get_proxy_headers(bad_proxies);
            response = s.get(url,headers=headers,proxies=proxies,timeout=10)
            response_status = response.status_code
        except:
            retry = True
            bad_proxies.append(proxies)
            
        if response_status == 200:
            retry = False
        else:
            retry = True
        if retry_cnt >= RETRY_LIMIT:
            retry = False            
    return response
