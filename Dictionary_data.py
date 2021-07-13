import json
from difflib import get_close_matches

class english_dic:
	
	def Find(lf,data,inp):
		for i in data[inp]:
			print(i)
	
	def Notexist(lf):
		print("that word is not there")

	def Exit_end(lf):
		exit()

	def Noword(lf):
		print("Enter word to find")
		

data=json.load(open("data.json"))
obj = english_dic()

while(1):

	inp = input()
	inp = inp.lower()

	if inp == 'end':
		obj.Exit_end()

	elif inp == "":
		obj.Noword()

	elif inp in data:
		obj.Find(data,inp)

	elif len(get_close_matches(inp,data.keys())) > 0:
		val = get_close_matches(inp,data.keys())[0]
		print("Did you mean %s instead?" %val)
		print("Type yes-y or no-n")
		yes_inp = input()
		if yes_inp == "y":
			obj.Find(data,val)
		elif yes_inp == 'n':
			print("Search for new word.")
		else:
			print("we don't undurstand")

	else:
		obj.Notexist()

