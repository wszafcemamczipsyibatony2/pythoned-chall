import re
import json
import os,binascii
import random
stringToRecreate = str(binascii.b2a_hex(os.urandom(random.randint(128,256))))[2:-1]

flagReward = "ping{90fe10dd84dff304c3479946cd6e299c1aed28a3a5c492a6f1725c8de9ad79f4}"

message = '''
Welcome to our awesome python message decoder!

Please provide some objects for our awesome decoder!
Example:
[{"cyrUjYDIx": 2574},{"pBrMPiopjwLG": 196},{"liIPqVsVwEdmgahZc": 3318},{"MZhFws": 187},{"GcudcezgtVUskxYsXq": 16808},{"UwYfrbhEtDwMbX": 117714},{"MQfDZLc": 3310},{"TByiPvC": 4314},{"naFYegAeknC": 4189},{"VdHQGuSKkUFAPJMkMziyD": 379},{"WLpgZrvDkmxkaH": 239},{"AcYIKZboDvyg": 32864},{"ZGRZUdimWu": 263},{"yXsUeTaiWoplBszOrs": 847},{"ozGmbTn": 7781},{"jjUwsMJgqSGlKpotA": 15683},{"QJxsTj": 7797},{"XUHXHGgd": 362},{"CAkuORohxrmEzQVduQGF": 73},{"MedmpdnYyWxSDbWn": 83},{"eyeaarLhUsVm": 15703},{"OMByrUxswVKWivu": 262235},{"IhArkspPMSvam": 435},{"HfHGvEunehHzrXIStH": 13},{"QvHdHpVZnACe": 861},{"cBxDchEKfeTVScjTketd": 262267},{"EBTvlRbAxRpEVND": 72},{"ZRWJzfMMTfNind": 117810},{"qvJzNVDmKDgmxEKDSZ": 629},{"EYnbJKOJUomESrhz": 117816},{"CYEeiUOWIUJphqNHnL": 55},{"ltEygsvoipMgNdif": 331},{"AELdsiaSNhNVphNik": 4285},{"qBrqBpaFykvsRcj": 227},{"XLKZetVUNPFCaIhaUSFcF": 807},{"qCfNseEspkuo": 134},{"CAsVONtpP": 15682},{"gSYkubGowJvuWf": 262259},{"dWQrQxF": 15863},{"UwmubPDqg": 531672},{"RZDcMdNmYqkt": 908},{"jqPCMrEVioWHzAwNQ": 422},{"PLaLvVe": 257},{"TfrUbaQbfjCRMvWdtVnFY": 1300},{"AJqrnW": 117668},{"hCzwQnDYKiTRCQr": 16916},{"TXZXwRPtFzTIsIrAvJr": 224},{"TLGDoRu": 82},{"dJEqXQkbfO": 906},{"CNnnJVgmhzfm": 87},{"CDGmmwqbdeQEPQtsRSF": 300},{"azhITWqqCeLWzHDAtJ": 46867},{"AFpAlVDjEnE": 239},{"NcipomszwmrGbgBEiT": 14},{"xLYTYDVraGB": 86},{"MCfTPwOqgxtzzhA": 32774},{"fOHZfhIFCcsnOQ": 55},{"MAjCYHrMgppIapQlL": 201},{"wJZXOqOf": 32834},{"ERzPvjsORnxKt": 2548},{"ZSXzFs": 780},{"zIDhGRful": 16812},{"nZdTPWHw": 167},{"ImqOcPlXZIcRiGhZV": 515},{"eZKoIp": 656},{"XNWwdFklUnWAP": 1495},{"UIIsgjNvwcOgrg": 4185}]
to get your own result!

If you will be able to create a following string in the result, you will get a free flag! What an opportunity, right?
'''+str(stringToRecreate)

class Caller:
	def __init__(self, call):
		self.code = call
		self.result = (len(call)*99)%256
		self.finalString = ""
		self.errors = 0
	
	def callFunction(self):
		for obj1 in self.code:
			try:
				for obj2 in obj1:
					self.result = ((((self.result^self.sumOfChar(obj2)))*12345) + obj1[obj2]^ord(obj2[0]))%54321
					self.finalString += chr((self.result % 256))
			except:
				self.errors += 1
	
	def sumOfChar(self, s):
		res = 0
		for c in s:
			res += ord(c)
		return res
	
	def finalizeFunction(self):
		print(f"Your code has evaluated.\nYour result is: \"{self.finalString}\".\nErrors you have risen: {self.errors}")
		if self.finalString == stringToRecreate:
			print("Congratz! You cracked it! Your reward is here:")
			print(flagReward)
		else:
			print("unfortunately you weren't able to reproduce the original string so I can't give you the flag... :(")

	

print(message)
print("Now provide a list of objects:")
while 1:
	userInput = str(input(">>> "))
	builder = Caller
	try:
		code = json.loads(userInput)
		userBuilder = builder(code)
		userBuilder.callFunction()
		userBuilder.finalizeFunction()
	except:
		print("Beep, boop bad input detected!")
