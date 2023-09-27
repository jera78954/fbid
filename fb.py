import os, sys, bs4, time, datetime, requests, re, random, urllib
from datetime import datetime
from bs4 import BeautifulSoup as bs

#--> Global Variable
bulan = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
perangkat = '; m_pixel_ratio=1.25; dpr=1.125; wd=360x780'
ok = 0
cp = 0
fuid=[]
#--> Warna
P = "\x1b[38;5;231m" # Putih
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
A = '\x1b[38;5;248m' # Abu-Abu
R='\033[1;31m'
G='\033[1;32m'
B='\033[1;36m'
W='\033[1;37m'
P='\033[1;35m'
#--> Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system('clear')
    elif "win" in sys.platform.lower():os.system('cls')
def random_ua():
    model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
    fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
    ua1 = 'Mozilla/5.0 (iPhone, CPU iPhone '+fbsv+' like Mac OS '+str(random.randint(8,16))+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+build+') Safari/604.1'
    ua2 = "Mozilla/5.0 (iPhone "+str(random.randrange(4,6))+" X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/"+str(random.randint(4,13))+".1.1 Mobile/"+model+" Safari/604.1"
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    ua3 = f"Mozilla/5.0 (Linux; Android {str(random.randint(4,13))}; "+dv_typ+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua4 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua5 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160'])
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua6 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    ua = random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
    return(ua)
shahin=[]
for love in range(10000):
	ax = 'Mozilla/5.0 (Linux; Android '
	bx = random.randrange(8,13)
	cx = '; SHARK KTUS-H0 Build/KTUS'
	dx = random.randrange(1111,9999)
	ex = '00OS00MP2; wv) AppleWebkit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	fx = random.randrange(100,999)
	gx = '.0.'
	hx = random.randrange(1111,9999)
	ix = '.'
	jx = random.randrange(100,999)
	kx = ' Mobile Safari/537.36'
	hot = f'{ax}{bx}{cx}{dx}{ex}{fx}{gx}{hx}{ix}{jx}{kx}'
	shahin.append(hot)
#--> Waktu
def waktu():
    _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
    hari_ini = ("%s%s%s"%(datetime.now().day,_bulan_,datetime.now().year))
    return(str(hari_ini.lower()))

#--> User Agent Vivo
def random_ua_vivo():
    a = random.randrange(110,113)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)                                                            #--> OS Version
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160']) #--> Device Type
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])                                       #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                    #--> Device Version
    sd_ver = random.randrange(1,10)                                                             #--> Update Version
    ch_ver = f'{a}.0.{b}.{c}'                                                                   #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)
from concurrent.futures import ThreadPoolExecutor as tred
#--> User Agent Samsung
def random_ua_samsung():
    a = random.randrange(110,113)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)                                                            #--> OS Version
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B']) #--> Device Type
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])                       #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                    #--> Device Version
    sd_ver = random.randrange(1,10)                                                             #--> Update Version
    ch_ver = f'{a}.0.{b}.{c}'                                                                   #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)
ualist=[]
for i in range(2000):
    fbs = random.choice([
        'com.facebook.adsmanager',
        'com.facebook.lite',
        'com.facebook.orca',
        'com.facebook.katana',
        'com.facebook.mlite'])
    application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    application_version_code = str(random.randint(000000000,999999999))
    android_version = str(random.randrange(5,15))
    dens = str(random.randrange(0,5))
    xzx = random.choice(['Samsung', 'Galaxy A7(2016)', 'a7xltechn', 'SM-A710XZ', 'Absolute', 'GT-B9120', 'GT-B9120', 'Acclaim', 'SCH-R880', 'SCH-R880', 'Admire', 'SCH-R720', 'SCH-R720', 'Amazing', 'amazingtrf', 'SGH-S730M', 'Baffin', 'baffinltelgt', 'SHV-E270L', 'Captivate Glide', 'SGH-I927 Samsung-SGH-I927', 'Captivate Glide', 'SGH-I927', 'SGH-I927', 'China Telecom', 'kylevectc', 'SCH-I699I', 'Chromebook Plus', 'kevin_cheets', 'kevin', 'Chromebook Plus', 'kevin_cheets Samsung Chromebook Plus', 'Chromebook Pro', 'caroline_cheets', 'caroline', 'Chromebook Pro', 'caroline_cheets Samsung Chromebook Pro', 'Conquer', 'SPH-D600', 'SPH-D600', 'DoubleTime', 'SGH-I857 Samsung-SGH-I857', 'Droid Charge', 'SCH-I510', 'SCH-I510', 'Elite', 'eliteltechn', 'SM-G1600', 'Elite', 'elitexltechn', 'SM-G1650', 'Europa', 'GT-I5500B', 'GT-I5500B', 'Europa', 'GT-I5500L', 'GT-I5500L', 'Europa', 'GT-I5500M', 'GT-I5500M', 'Europa', 'GT-I5503T', 'GT-I5503T', 'Europa', 'GT-I5510L', 'GT-I5510L', 'Exhibit', 'SGH-T759', 'SGH-T759', 'Galaxy (China)', 'GT-B9062', 'GT-B9062', 'Galaxy 070', 'hendrix', 'YP-GI2', 'Galaxy A', 'archer', 'archer', 'Galaxy A', 'archer', 'SHW-M100S', 'Galaxy A3 (2017)', 'a3y17lte', 'SM-A320Y', 'Galaxy A3', 'a33g', 'SM-A300H', 'Galaxy A3', 'a3lte', 'SM-A300F', 'Galaxy A3', 'a3lte', 'SM-A300M', 'Galaxy A3', 'a3lte', 'SM-A300XZ', 'Galaxy A3', 'a3lte', 'SM-A300YZ', 'Galaxy A3', 'a3ltechn', 'SM-A3000', 'Galaxy A3', 'a3ltechn', 'SM-A300X', 'Galaxy A3', 'a3ltectc', 'SM-A3009', 'Galaxy A3', 'a3ltedd', 'SM-A300G', 'Galaxy A3', 'a3lteslk', 'SM-A300F', 'Galaxy A3', 'a3ltezh', 'SM-A3000', 'Galaxy A3', 'a3ltezt', 'SM-A300YZ', 'Galaxy A3', 'a3ulte', 'SM-A300FU', 'Galaxy A3', 'a3ulte', 'SM-A300XU', 'Galaxy A3', 'a3ulte', 'SM-A300Y', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310F', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310M', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310X', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310Y', 'Galaxy A3(2016)', 'a3xeltekx', 'SM-A310N0', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320F', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320FL', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320X', 'Galaxy A5', 'a53g', 'SM-A500H', 'Galaxy A5', 'a5lte', 'SM-A500F', 'Galaxy A5', 'a5lte', 'SM-A500G', 'Galaxy A5', 'a5lte', 'SM-A500M', 'Galaxy A5', 'a5lte', 'SM-A500XZ', 'Galaxy A5', 'a5ltechn', 'SM-A5000', 'Galaxy A5', 'a5ltechn', 'SM-A500X', 'Galaxy A5', 'a5ltectc', 'SM-A5009', 'Galaxy A5', 'a5ltezh', 'SM-A5000', 'Galaxy A5', 'a5ltezt', 'SM-A500YZ', 'Galaxy A5', 'a5ulte', 'SM-A500FU', 'Galaxy A5', 'a5ulte', 'SM-A500Y', 'Galaxy A5', 'a5ultebmc', 'SM-A500W', 'Galaxy A5', 'a5ultektt', 'SM-A500K', 'Galaxy A5', 'a5ultelgt', 'SM-A500L', 'Galaxy A5', 'a5ulteskt', 'SM-A500F1', 'Galaxy A5', 'a5ulteskt', 'SM-A500S', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510F', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510M', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510X', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510Y', 'Galaxy A5(2016)', 'a5xeltecmcc', 'SM-A5108', 'Galaxy A5(2016)', 'a5xeltektt', 'SM-A510K', 'Galaxy A5(2016)', 'a5xeltelgt', 'SM-A510L', 'Galaxy A5(2016)', 'a5xelteskt', 'SM-A510S', 'Galaxy A5(2016)', 'a5xeltextc', 'SM-A510Y', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A5100', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A5100X', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A510XZ', 'Galaxy A5(2017)', 'a5y17lte', 'SM-A520F', 'Galaxy A5(2017)', 'a5y17lte', 'SM-A520X', 'Galaxy A5(2017)', 'a5y17ltecan', 'SM-A520W', 'Galaxy A5(2017)', 'a5y17ltektt', 'SM-A520K', 'Galaxy A5(2017)', 'a5y17ltelgt', 'SM-A520L', 'Galaxy A5(2017)', 'a5y17lteskt', 'SM-A520S', 'Galaxy A5x(2016)', 'a5xeltextc', 'SM-A510Y', 'Galaxy A7', 'a73g', 'SM-A700H', 'Galaxy A7', 'a7alte', 'SM-A700F', 'Galaxy A7', 'a7lte', 'SM-A700FD', 'Galaxy A7', 'a7lte', 'SM-A700X', 'Galaxy A7', 'a7ltechn', 'SM-A7000', 'Galaxy A7', 'a7ltechn', 'SM-A700YD', 'Galaxy A7', 'a7ltectc', 'SM-A7009', 'Galaxy A7', 'a7ltektt', 'SM-A700K', 'Galaxy A7', 'a7ltelgt', 'SM-A700L', 'Galaxy A7', 'a7lteskt', 'SM-A700S', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710F', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710M', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710X', 'Galaxy A7(2016)', 'a7xeltecmcc', 'SM-A7108', 'Galaxy A7(2016)', 'a7xeltektt', 'SM-A710K', 'Galaxy A7(2016)', 'a7xeltelgt', 'SM-A710L', 'Galaxy A7(2016)', 'a7xelteskt', 'SM-A710S', 'Galaxy A7(2016)', 'a7xeltextc', 'SM-A710Y', 'Galaxy A7(2016)', 'a7xltechn', 'SM-A7100', 'Galaxy A7(2017)', 'a7y17lte', 'SM-A720F', 'Galaxy A7(2017)', 'a7y17lteskt', 'SM-A720S', 'Galaxy A8', 'a8elte', 'SM-A800F', 'Galaxy A8', 'a8elte', 'SM-A800YZ', 'Galaxy A8', 'a8elteskt', 'SM-A800S', 'Galaxy A8', 'a8hplte', 'SM-A800I', 'Galaxy A8', 'a8hplte', 'SM-A800IZ', 'Galaxy A8', 'a8ltechn', 'SM-A8000', 'Galaxy A8', 'a8ltechn', 'SM-A800X', 'Galaxy A8', 'SCV32', 'SCV32', 'Galaxy A8(2016)', 'a8xelte', 'SM-A810F', 'Galaxy A8(2016)', 'a8xelte', 'SM-A810YZ', 'Galaxy A8(2016)', 'a8xelteskt', 'SM-A810S', 'Galaxy A9 Pro', 'a9xproltechn', 'SM-A9100', 'Galaxy A9 Pro', 'a9xproltesea', 'SM-A910F', 'Galaxy A9(2016)', 'a9xltechn', 'SM-A9000', 'Galaxy Ace 4 Lite', 'vivalto3g', 'SM-G313U', 'Galaxy Ace 4', 'vivaltods5m', 'SM-G313HU', 'Galaxy Ace 4', 'vivaltods5m', 'SM-G313HY', 'Galaxy Ace 4', 'vivaltods5m', 'SM-G313M', 'Galaxy Ace 4', 'vivaltods5m',])
    ualist.append(f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(xzx[3])} Build/{str(xzx[2])} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density='+dens+'.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBMF/{str(xzx[0])};FBBD/{str(xzx[0])};FBPN/{str(fbs)};FBDV/{str(xzx[3])};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]')

def cvt(st,ran):
    try:
        if st == 'ok': cookie = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(ran['sb'],ran['datr'],ran['c_user'],ran['xs'],ran['fr']))
        elif st == 'cp': cookie = ('checkpoint=%s;datr=%s;fr=%s'%(ran['checkpoint'],ran['datr'],ran['fr']))
    except Exception as e : cookie = '; '.join([str(x)+"="+str(y) for x,y in ran])
    return(str(cookie))


def get_nope():
	u = f'xdxerx+str(random.randrange(1000,10000))@gmail.com'
	uu = '+8801615161056'
	ni   = str(random.randrange(1000,10000))
	nu   = str(random.randrange(111111,999999))
	nope = '+8801615%s'%(nu)
	return(nope)
def get_pass():
	u = 'MKSINGRAJU@123'
	return(u)
#--> User Agent Realme
def random_ua_realme():
    a = random.randrange(110,113)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)                                                        #--> OS Version
    dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])   #--> Device Type
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])                     #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                #--> Device Version
    sd_ver = random.randrange(1,10)                                                         #--> Update Version
    ch_ver = f'{a}.0.{b}.{c}'                                                               #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)
    






ua = random.choice(ualist)




perangkat = '; m_pixel_ratio=1.25; dpr=1.125; wd=360x780'
r_em  = requests.Session()
#data = {'country':'indian','gender_type':'Male','number_generate':'1','submit':'Generate'}
#reqa = bs(requests.post('http://ninjaname.net/indian_name.php',data=data).content,'html.parser')



def logo():
	#t = print(49*'-')
	os.system('clear')
	print(f'''\x1b[1;97m
 	   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄  
 	  ▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ 
 	  ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
	  ▐░▌          ▐░▌       ▐░▌
 	  ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
 	  ▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ 
 	  ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
	  ▐░▌          ▐░▌       ▐░▌
 	  ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌
 	  ▐░▌          ▐░░░░░░░░░░▌ 
 	   ▀            ▀▀▀▀▀▀▀▀▀▀  
                          
     ┌───────────────────────────────────────
      [<>] FB AUTO CREATE
     └───────────────────────────────────────''')

def xerx():
    logo();print(50*f'{B}_{W}')
    print(f' [1] create auto id {R}[{G}FACEBOOK{R}]{W} ')
    print(50*f'{B}_{W}')
    __ = input(' >> choose <<  ')
    if __ in ['1','01']:
    	mail()

def mail():
    logo()
    print(50*f'{B}_{W}')
    print('   [<>] Prosess started')
    print(50*f'{B}_{W}')
    #limit = int(input(' [*] input limit here :- '))
    limit = int(input(f'  {R}[{B}≈{R}]{W} How many Ids you want to Create? :{G} '))
    print(50*f'{B}_{W}')
    for xd in range(limit):
        create()


def create():
    try:
        r_fb = requests.Session()
        r_nm  = requests.Session()
        r_fb  = requests.Session()
        r_em  = requests.Session()
        r_fbx  = requests.Session()
        r_nm.cookies.clear()
        r_fb.cookies.clear()
        r_fbx.cookies.clear()
        r_em.cookies.clear()
        nope = get_nope()
        
        try:
            data = {'country':'indian','gender_type':'Male','number_generate':'1','submit':'Generate'}
            reqa = bs(requests.post('http://ninjaname.net/indian_name.php',data=data).content,'html.parser')
            nm = re.search('• (.*?)<br/>',str(reqa)).group(1)
        except Exception as e:
            
            nam1 = random.choice(['Aryan','rohit','bikash','manoj','anjan','rayan','sandeep','ali','rajib'])
            nam2 = random.choice(['tamang','rajput','xheetri','chaudhary','kumar'])
            nm = f'{nam1} {nam2}'
        pw = 'LOVE@123'
        
        nb = '0123456789'
        up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lw = up.lower()
        ch = up + lw + nb
        r = ''.join(random.choice(ch) for _ in range(3))
        nm_mail          = f'%s{r}'%(nm.replace(' ','').lower())
        em          = f'%s{r}@icznn.com'%(nm.replace(' ','').lower())
        ua = random.choice(ualist)
        host  = 'mbasic.facebook.com'
        head1 = {'accept-encoding':'gzip, deflate','accept-language':'en-US,en;q=0.9','cache-control':'max-age=0','referer':f'https://{host}/reg/','sec-ch-ua':'','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'Android','sec-fetch-dest':'document','sec-fetch-mode':'navigate','sec-fetch-site':'same-origin','sec-fetch-user':'?1','upgrade-insecure-requests':'1','user-agent':ua}
        cid  = str(random.randrange(100,999))
        url1 = f'https://mbasic.facebook.com/reg/?cid={cid}&refsrc=deprecated&_rdr'
        req1 = bs(r_fb.get(url1,headers=head1).content,'html.parser')
        raq1 = req1.find('form',{'method':'post'})
        sess=requests.Session()
        first = r_fb.get('https://m.facebook.com/reg/?').text
        lsd=re.search('name="lsd" value="(.*?)"',str(first)).group(1)
        jazo=re.search('name="jazoest" value="(.*?)"',str(first)).group(1)
        inta=re.search('name="reg_instance" value="(.*?)"',str(first)).group(1)
        impres=re.search('name="reg_impression_id" value="(.*?)"',str(first)).group(1)
        gr = '2' 
        ttl_tgl = str(random.randrange(1,29))   
        ttl_bln = str(random.randrange(1,13))    
        ttl_thn = str(random.randrange(1970,2001))  
        ttl = '%s %s %s'%(ttl_tgl,bulan[ttl_bln],ttl_thn)
        dat = {
		
            'ns':re.search('name="ns" type="hidden" value="(.*?)"',str(raq1)).group(1),'ccp':re.search('name="ccp" type="hidden" value="(.*?)"',str(raq1)).group(1),'lsd':re.search('name="lsd" type="hidden" value="(.*?)"',str(raq1)).group(1),'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq1)).group(1),'reg_instance':re.search('name="reg_instance" type="hidden" value="(.*?)"',str(raq1)).group(1),'reg_impression_id':re.search('name="reg_impression_id" type="hidden" value="(.*?)"',str(raq1)).group(1),
                #--> Second Data
            'submission_request':'true','helper':'','zero_header_af_client':'','app_id':'','logger_id':'',
                #--> Field Data
            'field_names[]':'firstname','field_names[]':'reg_email__','field_names[]':'sex','field_names[]':'reg_passwd__',
                #--> Input Data
        'firstname':nm,'reg_email__':nope,'reg_passwd__':pw,'pass':pw,'sex':gr,'gender':gr,'did_use_age':False,'birthday_day':ttl_tgl,'birthday_month':ttl_bln,'birthday_year':ttl_thn,'is_birthday_confirmed':'confirmed','submit':'Daftar'}
        #print(dat)
        cok  = '; '.join([str(x)+"="+str(y) for x,y in r_fb.cookies.get_dict().items()])
        cok += perangkat
        pos1 = r_fb.post(f'https://m.facebook.com/reg/submit/',headers=head1,data=dat,cookies={'cookie':cok})
        pos2 = bs(pos1.content,'html.parser')
        raq2 = pos2.find('form',{'method':'post'})
        #print(raq2)
        for raq2 in pos2.find_all('form', {'method': 'post'}):
            if 'checkpoint' in str(raq2['action']):
                print(' checkpoint ')
               # ftx()
                break
            elif 'save-device' in str(pos1.url):
               # print('ok')
                dat = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq2)).group(1),'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq2)).group(1),'flow' : 'interstitial_nux','next' : False,'nux_source' : 'dbl_nux_after_reg','submit' : 'OK'}
                nek  = 'https://mbasic.facebook.com' + raq2['action']
                #print(nek)
                #print(nope)
               # print(pw)
                cok  = '; '.join([str(x)+"="+str(y) for x,y in r_fb.cookies.get_dict().items()])
                cok += perangkat
                pos2 = r_fb.post(nek,headers=head1,data=dat,cookies={'cookie':cok})
                pos3 = bs(pos2.content,'html.parser')
                nok = [x['href'] for x in pos3.find_all('a',href=True) if 'changeemail' in str(x['href'])][0]
                nek = 'https://mbasic.facebook.com' + nok
                cok  = '; '.join([str(x)+"="+str(y) for x,y in r_fb.cookies.get_dict().items()])
                cok += perangkat
                pes = r_fb.get(nek,headers=head1,cookies={'cookie':cok})
                pos = bs(pes.content,'html.parser')
                raq3 = pos.find('form',{'method':'post'})
                dat = {'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq3)).group(1),'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq3)).group(1),'next' : False,'old_email' : re.search('name="old_email" type="hidden" value="(.*?)"',str(raq3)).group(1),'reg_instance' : re.search('name="reg_instance" type="hidden" value="(.*?)"',str(raq3)).group(1),'new' : em,'submit' : 'Add'}
                #print(dat)
                nek = 'https://mbasic.facebook.com' + raq3['action']
                #print(' step 3.1 url :'+nek)
                cok = '; '.join([str(x)+"="+str(y) for x,y in r_fb.cookies.get_dict().items()])
                cok += perangkat
                pes = r_fb.post(nek,headers=head1,data=dat,cookies={'cookie':cok})
                pos = bs(pes.content,'html.parser')
                #print(pos)
               # print(53*'-')
                #print(em)
                #print(nm_mail)
                time.sleep(10)
                url = f'https://www.1secmail.com/api/v1/?action=getMessages&login={nm_mail}&domain=icznn.com'
                response = r_fbx.post(url).json()
                if response and isinstance(response, list) and len(response) > 0:
                    
                #print(response)
                #subject = response[0]['subject']
                    first_message = response[0]
                    subject = first_message.get('subject', '')
                    code_match = re.search(r'FB-(.*?) is', subject)
                    codef = code_match.group(1)
                #print(codef)
                    codex_str = ''.join(codef)
               # code = input(' input the code bruh')
                #codex = re.search(r'\d+', subject).group()
                
                #code = input( ' input code we sended to you yandex mail')
                #code = codex
                    print(50*f'{B}_{W}')
                    raq4 = pos.find('form',{'method':'post'})
                #print(raq4)
                    dat = {'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq4)).group(1),'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq4)).group(1),'c' : codex_str,'submit[confirm]' : 'Confirm'}
                    nek  = 'https://mbasic.facebook.com' + raq4['action']
                #print(nek)
               # print(dat)
                    cok  = '; '.join([str(x)+"="+str(y) for x,y in r_fb.cookies.get_dict().items()])
                    #print(cok)
                    cok += perangkat
                    pos5 = r_fb.post(nek,headers=head1,data=dat,cookies={'cookie':cok})
                    uid = {'cookie':cok}
                #print(pos5)
                    fuid = cok.split('c_user=')[1].split(';')[0]
                    stat = 'ok+'
                    cookie = cvt('ok',r_fb.cookies.get_dict())
                #print(pos5.text)
                #react(cookie, post_ids_to_react)
                    print(f' {B} name :{G} {nm}')
                    print(f' {B} uid :{G} {fuid}')
                    print(f' {B} number :{G} {nope}')
                    print(f' {B} email :{G} {em}')
                    print(f' {B} pw :{G} {pw}')
                    #print(f' code :- {codex_str}')
                    print(f' cookie :- {cookie}')
                    print(50*f'{B}_{W}')
                    open('/sdcard/auto-create.txt', 'a').write(fuid+' | '+pw+'|'+cookie+'\n')
                    
                    
                else:
                   # pass
                    print(f'{R} FAILD ');print(50*f'{B}_{W}');pass
            else:
                pass
    except Exception as e:
        pass
 
 
def ml(nm_mail,em):
    url = f'https://www.1secmail.com/api/v1/?action=getMessages&login={nm_mail}&domain=icznn.com'
    response = requests.get(url).json()
    subject = response[0]['subject']
    code = re.search(r'\d+', subject).group()
    return(code)
xerx()
