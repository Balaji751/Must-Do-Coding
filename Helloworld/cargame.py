# command=input("> ")
# if command=="Help" or command=="help":
# 	print("Start - to start the engine")
# 	print("Stop - to stop the engine")
# 	print("quit - to quit")
# else:
# 	print("I don't understand that ...")
# entered=input()

# if entered=="Start":
# 	print("Engine started, Ready to go!")
# elif entered=="Stop":
# 	print("Engine stopped")
# elif entered=="quit":
# 	print(" ")

command=""
started=False
while True:
 	command=input("> ")
 	if command=="start":
 		if started:
 			print("Car, already started")
 		else:
 			started=True
 			print("Car started")
 	elif command=="stop":
 		if not started:
 			print("Car,already stopped")
 		else:
 			started=False
 			print("Car stopped")
 	elif command=="help":
 		print("""
start - to start the car
stop - to stop the car
quit - to quit
 		""")
 	elif command=="quit":
 		break
 	else:
 		print("I don't understand that ...")
