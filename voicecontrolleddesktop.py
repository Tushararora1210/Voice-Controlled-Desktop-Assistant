from assistantfunctions import *
import threading
import winsound

while(1):
	try:
		cmd=command()
		if("google" in cmd):
			winsound.Beep(2000,500)
			cmd1=command()
			print(cmd1)
			if("open my computer" in cmd1):
				openmycomputer()

			elif("play music" in cmd1):
				say("Which Music Do you want to play ")
				cmd2=command()
				print(cmd2)
				try:
					t=threading.Thread(target=playMusic,args=(cmd2,))
					t.start()
					t.join()
				except:
					say("No music"+cmd2+"is present")

			elif("take screenshot" in cmd1):
				takess()

			elif("add" in cmd1):
				y=cmd1.split()
				print(y)
				for i in range(len(y)):
					if(y[i]=="with"):
						sum=int(y[i-1])+int(y[i+1])
				say("Answer is")
				say(sum)
				
			elif("subtract" in cmd1):
				y=cmd1.split()
				try:
					for i in range(len(y)):
						if(y[i]=="from"):
							diff=int(y[i+1])-int(y[i-1])
							say("Answer is ")
							say(diff)
				except:
					pass

			elif("multiply" in cmd1):
				y=cmd1.split()
				try:
					for i in range(len(y)):
						if(y[i]=="with"):
							prod=int(y[i+1])*int(y[i-1])
							say("Answer is ")
							say(prod)
				except:
					pass

			elif("divide" in cmd1):
				y=cmd1.split()
				try:
					for i in range(len(y)):
						if(y[i]=="with"):
							div=int(y[i-1])/int(y[i+1])
							say("Answer is ")
							say(div)
				except:
					pass

			elif("how are you" in cmd1):
				say("I am fine..what about you")

			elif("power" in cmd1):
				y=cmd1.split()
				for i in range(len(y)):
					if(y[i]=="raised"):
						a=y[i-1]
					if(y[i]=="power"):
						b=y[i+1]
				c=a*b
				say("answer is ",c)

			elif("tell me about" in cmd1):
				y=cmd1.split()
				for i in range(len(y)):
					if(y[i]=="about"):
						break
				y="".join(y[i+1:len(y)])
				information(y)

			elif("open website" in cmd1):
				say("please tell the name of the website ,you wish to open")
				cmd2=command()
				openWebsite(cmd2)

			elif("running task" in cmd1):
				taskmanagerlist()

			elif("kill task" in cmd1):
				say("please tell the name of the task ,you wish to kill")
				cmd2=command()
				killtask(cmd2)

			elif("login to facebook" in cmd1):
				t=threading.Thread(target=loginfacebook)
				t.start()
				t.join()
				

			elif("wish me" in cmd1):
				wishme()

			elif("time" in cmd1):
				timee()

			elif("date" in cmd1):
				date()

			elif("present year" in cmd1):
				presentyear()

			elif("present month" in cmd1):
				presentmonth()

			else:
				say("sorry,i didnt get you")
	except:
		pass;