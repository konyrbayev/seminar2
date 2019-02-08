try:
	import myfile.py
	print ("This file exists!")
except:
	print ("File doesn't exist")

L=[]
try:
	print(L[1])
except:
	print("Index Error")

try:
	plint("Error comand!!!")
except:
	print("Syntax Error")
