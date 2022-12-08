import http.client
import bs4
import time
import requests


RED='\033[0;31m'
NC='\033[0m'
BLUE = '\033[0;34m'
CYAN = '\033[0;36m'
LRED = '\033[1;31m'
start = time.perf_counter()

def siteavail(datadomain):
        try:
            connection = http.client.HTTPSConnection(datadomain,timeout=2)
            connection.request('GET','/')
            response = connection.getresponse()
            location_header = response.getheader('location')
          
            if location_header is None:
                    s_code = response.getcode()
                    domaindata = response.read()
                    soup = bs4.BeautifulSoup(domaindata,'html.parser')
                    title1 = soup.find("title").text

                    request_url = requests.get("http://"+datadomain)
                    if request_url.url:
                        print(f"{CYAN}https://{datadomain}{NC} {RED}{[s_code]}{NC} {BLUE}{[title1]}{NC}")
                    else:
                        print(f"{CYAN}http://{datadomain}{NC} {RED}{[s_code]}{NC} {BLUE}{[title1]}{NC}")
            else:
                    siteavail(location_header.split('/')[2])

        except Exception:
                print(f"{LRED}{datadomain} [Domain is not found] {NC}")
       
if __name__ == "__main__":

    with open ('domain.txt','r') as f:
        for i in f:
            siteavail(i.strip())
    finissh = time.perf_counter()
    print(f'Finished in {round(finissh-start ,2)} second (s)')




# request_url = 'testphp.vulnweb.com'
# connection = HTTPConnection(request_url,timeout=2)
# connection.request('GET', '/')
# tmp = connection.getresponse()
# print(tmp.getcode())






# site_is_online('http://testphp.vulnweb.com')






















  






# w = whois.whois('142.250.182.238')
# dns = socket.gethostbyname(tttt)
# print(w)
# print(dns)
# dns = socket.gethostbyname(tttt)
# domain = "https://"+tttt
# if dns:
#                             try:
#                                     # request_url = requests.get(domain,timeout=1,allow_redirects=True)
#                                     start = time.perf_counter()
#                                     print(requests.get(domain))
#                                     finissh = time.perf_counter()
#                                     print(f'Finished in {round(finissh-start ,2)} second (s)')
#                             except Exception:
#                                 print("error")
# else:
    # print("no")
