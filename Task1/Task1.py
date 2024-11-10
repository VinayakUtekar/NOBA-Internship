import os
import random
import fbchat
import time
from getpass import getpass

filename = input("Enter filename to read from ")
if os.path.exists(filename):
	f = None
	try:
	    f = open(filename,"r")
	    data = f.readlines()
	    count = 0
	    myline = random.choice(data)
	    print(myline)
	except Exception as e:
		print("issue",e)
	finally:
		if f is not None:
			f.close()
else:
	print(filename,"does not exists")

username = input("Username: ")
client = fbchat.Client(username, getpass())
no_of_friends = int(raw_input("Number of friends: "))
for i in range(no_of_friends):
    name = input("Name: ")
    friends = client.searchForUsers(name) 
    friend = friends[0]
    while True : 
        time.sleep(21600)
        msg = input(myline)
        sent = client.sendMessage(msg, thread_id=friend.uid)
        if sent:
            print("Message sent successfully!")