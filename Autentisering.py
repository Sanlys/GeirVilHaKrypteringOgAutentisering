import hashlib

passord = [
	'38a6dcc494484553c8291fce2ab8d5b5311caa02', #hei
	'9531b84eef1433e50093843a1ec11cd5bdb60947', #Mailandvgs123
	'5c46799b9d8be8abb6adfa41f41ac5f66093d2a6'  #ElendigPassord
]

inp = input("Skriv inn passord: ")
password = False
for i in passord:
	if i == hashlib.sha1(inp.encode('utf-8')).hexdigest():
		password = True
		break
print(password)