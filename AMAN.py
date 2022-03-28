import time,random,os,colorama,sys
import datetime as dt
from colorama import Fore as F
from random import uniform

#--------warna---------#
R   = F.RED
B   = F.BLUE
BL  = F.BLACK
Y   = F.YELLOW
M   = F.MAGENTA
C   = F.CYAN
G   = F.GREEN
W   = F.WHITE
RE  = F.RESET
RGB = random.choice([R,G,B,Y])


panah = (f"{C}〖{RGB}➤{C}〗{RE}")
panah2 = (f"{RGB}➜{RE}")

bannerlogin = (f"""
{RGB}\t┏━━━━━━━━━━━━━━━━━━━━━━━┓{RE}
{RGB}\t┃ Spam {RE}SMS{RE}
{RGB}\t┃ Dibuat oleh {RE}Om Senpai{RE}
{RGB}\t┃ Update Tgl {RE}27-03-2022{RE}
{RGB}\t┃ Masukin {RE}password {RGB}dulu{RE}
{RGB}\t┗━━━━━━━━━━━━━━━━━━━━━━━┛{RE}
""")
bannermenu = (f"""
{RGB}\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{RE}
{RGB}\t┃ Spam {RE}SMS{RE}
{RGB}\t┃ Dibuat oleh {RE}Om Senpai{RE}
{RGB}\t┃ Update Tgl {RE}27-03-2022{RE}
{RGB}\t┃ Check update disarankan 1 kali sehari
{RGB}\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RE}
""")

#----------------------#

class Typewriter:

    default_mode = 'ltr'

    @staticmethod
    def set_mode(mode):
        func_mode = {
            'ltr':__class__.print_ltr,
            'rtl':__class__.print_rtl,
            'scatter':__class__.print_scatter,
            }
        if mode in func_mode.keys():
           __class__.default_mode = mode
           __class__.default_func = func_mode[mode]
        else:
            print('-- Error: unkonwn mode --')

    @staticmethod
    def print_scatter(txt):
        len_txt = len(txt)
        pos = list(range(0, len_txt))
        random.shuffle(pos)
        dtxt = {}
        for i in range(len_txt): dtxt[i] = ' '

        print(' '*len_txt, end='')
        for p in pos:
            dtxt[p] = txt[p]
            print(chr(8)*len_txt ,end='')
            print(''.join(dtxt.values()), end='', flush=True)
            time.sleep(0.05)

    @staticmethod
    def print_rtl(txt):
        len_txt = len(txt)
        print(' '*len_txt, end='')
        for i in range(len_txt-1, -1, -1):
            print(chr(8)*len_txt ,end='')
            print(f'{txt[i:]:>{len_txt}}', end='', flush=True)
            time.sleep(0.1)
            
    @staticmethod
    def print_ltr(txt):
        for c in txt:
            print(c, end='', flush=True)
            time.sleep(uniform(0, 0.05))

    @staticmethod
    def print(*arg, **kwarg):
        sep = kwarg.get('sep', ' ')
        mode = kwarg.get('mode', __class__.default_mode)
        __class__.set_mode(mode)

        t = [str(w) for w in arg ]
        txt = sep.join(t)
        __class__.default_func(txt)
        #__class__.func_mode[__class__.default_mode](txt)
        kwarg.pop('mode',None)
        print(**kwarg)

    @staticmethod
    def input(prompt, **kwarg):
        __class__.print(prompt, **kwarg, end='')
        return input()

tw = Typewriter

def loading():
    os.system("clear")
    no = 0
    for x in range (20):  
        b = f"{panah}Loading" + f"{G}." * x
        print (b, end="\r",flush=True)
        time.sleep(uniform(0, 0.3))
        no += 1
        if no == 20:
            login()

def ulang():
    for i in reversed(range(4)):
        print (f"\r{panah}",end="")
        tw.print (f"Mengulang {B}{i:02}{RE} Detik",end="",flush=True)
        sys.stdout.write('\033[2K\033[1G')
        time.sleep(0.5)

def login():
    os.system("clear")
    tw.print (bannerlogin)
    try:
        check()
    except:
        check2()

def check():
    pw = "dava"
    open1 = open("token.txt","r")
    baca1 = open1.read()
    if baca1 == f"{pw}":
        tw.print (f"{panah}Proses Masuk {G}DISETUJUI{RE}") 
        main()
    else:
        tw.print (f"\n\n\n\n{panah}Copy dan paste ke browser kalian")
        print ("......\n\n")
        usr = tw.input(f"{panah}Password : {BL}")
        if usr == f"{pw}":
            open2 = open("token.txt", "w")
            open2.write(f"{pw}")
            tw.print (f"{panah}Proses Masuk {G}DISETUJUI!{RE}")
            time.sleep(1)
            main()
        else:
            open3 = open("token.txt", "w")
            tw.print (f"{panah}Proses Masuk {R}DITOLAK!{RE}")
            ulang()
            login()

def check2():
    FileNotFoundError
    pw = "dava"
    tw.print (f"\n\n\n\n{panah}Copy dan paste ke browser kalian")
    print ("......\n\n")
    open4 = open("token.txt", "w")
    usr2 = tw.input(f"{panah}Password : {BL}")
    if usr2 == f"{pw}":
        open4.write(f"{pw}")
        tw.print (f"{panah}Proses Masuk {G}DISETUJUI!{RE}")
    else:
        open5 = open("token.txt","w")
        tw.print (f"{panah}Proses Masuk {R}DITOLAK!{RE}")
        ulang()
        login()

def main():
    menu = f"""
    \n\n
    {RGB}\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {RGB}\t┃{RE}1. Check Update
    {RGB}\t┃{RE}2. Spam OLX
    {RGB}\t┃{RE}3. Spam Matahari
    {RGB}\t┃{RE}4. Spam Alodok
    {RGB}\t┃{RE}5. Spam Pizza Hut
    {RGB}\t┃{RE}6. Spam Unlimitid Pake Delay (whatsapp)
    {RGB}\t┃{RE}7. Spam Brutal
    {RGB}\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """
    os.system("clear")
    tw.print (bannermenu)
    tw.print (menu)
    jawab = int(tw.input(f"{panah}Pilih Nomer {panah2} "))
    if jawab == 1:
        os.system("git pull")
        sys.exit(f"{panah2}{R}Mulai ulang Script{RE}")
    elif jawab == 2:
        olx()
    else:
        tw.print(f"{panah}{RE}Pilih yang bener{RE}")

def olx():
    os.system("clear")
    print (f"""
{RGB}\t┏━━━━━━━━━━━━━━━━━━━━━━━━━┓{RE}
{RGB}\t┃ Script : {RE}Olx{RE}
{RGB}\t┃ Dibuat : {RE}Omsenpai{RE}
{RGB}\t┃ Update Tgl {RE}27-03-2022{RE}
{RGB}\t┗━━━━━━━━━━━━━━━━━━━━━━━━━┛{RE}
""")
    tw.print(f"\n\n\n{panah}Gunakan 8xxx")
    nomor = tw.input(f"{panah}nomor : ")
    jumlah = tw.input(f"{panah}Jumlah : ")
    headers = {
		"Host": 			"api.danacita.co.id",
		"Content-Length": 	"86",
		"Accept": 			"application/json, text/plain, */*",
		"Content-Type": 	"application/json",
		"User-Agent": 		"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39",
		"Origin": 			"https://app.danacita.co.id",
		"Sec-Fetch-Site": 	"same-site",
		"Sec-Fetch-Mode": 	"cors",
		"Sec-Fetch-Dest": 	"empty",
		"Referer":			"https://app.danacita.co.id/",
		"Accept-Encoding": 	"gzip, deflate, br",
		"Accept-Language": 	"en-US,en;q=0.9,id;q=0.8",
    }
    data = {
        "username":nomor,
        "password":"crHA#=5wcfbF",
        "accept_terms_and_policy":"true"
    }
    
    tw.print (f"\t{C}Hasilnya{RE} : ")
    for i in range(jumlah):
        respon=requests.post("https://api.danacita.co.id/v3/users/mobile_register", headers=headers,json=data)
        senpai=json.loads(respon.text)
        if senpai["detail"]=="Successfully sent OTP SMS":
                tw.print(f"\t{panah}{G}Berhasil{RE} Mengirim {nomor}")
        else:
                tw.print(f"\t{panah}{R}Gagal{RE} Mengirim {nomor}")
        time.sleep(2)
    main()

if __name__ == '__main__':
	try:
		loading()
 
    except:
        KeyboardInterrupt
        os.system("clear")
        sys.exit(f"{panah}{RGB}Keluar dari script{RE}")