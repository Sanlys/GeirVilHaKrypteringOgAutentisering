import hashlib

passordOgBrukernavn = {
	'brukernavn':'38a6dcc494484553c8291fce2ab8d5b5311caa02', 		#hei
	'MailandElev':'9531b84eef1433e50093843a1ec11cd5bdb60947', 		#Mailandvgs123
	'ElendigBrukernavn':'5c46799b9d8be8abb6adfa41f41ac5f66093d2a6' 	#ElendigPassord
}

brukernavn = input("Skriv inn brukernavn: ")
passord = input("Skriv inn passord: ")

if passordOgBrukernavn[brukernavn] == hashlib.sha1(passord.encode('utf-8')).hexdigest():
	print(":)")
else:
	print(":(")