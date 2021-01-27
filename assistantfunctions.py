import psutil

import time

import datetime

import speech_recognition as sr

import pyttsx3

import os

import subprocess

import wikipedia

from selenium import webdriver

engine=pyttsx3.init('sapi5')

engine.setProperty('rate',145)

def command():
	rec=sr.Recognizer()
	with sr.Microphone(sample_rate=48000,chunk_size=8192) as source:
		print('Ready to say')
		rec.pause_threshold=1
		rec.adjust_for_ambient_noise(source,duration=1)
		audio=rec.listen(source)
	try:
		command=rec.recognize_google(audio).lower()
		return command
	except:
		pass

def say(text):
	engine.say(text)
	engine.runAndWait()


def openmycomputer():
	os.system('explorer.exe')


def playMusic(musicname):
	os.system("vlc --play-and-exit music/"+musicname+".mp3")


def takess():
	x=len(os.listdir('screenshots'))+1
	os.system("nircmd.exe savescreenshot screenshots/screen"+str(x)+".png")


def add(a,b):
	return (a+b)


def minus(a,b):
	return (a-b)


def mul(a,b):
	return (a*b)


def divide(a,b):
	return(a/b)


def power(a,b):
	return(a**b)



def information(text):
	say(wikipedia.summary(text,sentences=2))


def openWebsite(name):
	os.system("start https://"+name+".com")


def taskmanagerlist():
	for proc in psutil.process_iter():
		print(proc.name())

def killtask(name):
	for proc in psutil.process_iter():
		if(proc.name()==(name+".exe")):
			proc.kill()


def loginfacebook():
	options = webdriver.ChromeOptions()
	options.add_argument('--ignore-certificate-errors')
	options.add_argument("--test-type")
	driver=webdriver.Chrome(chrome_options=options, executable_path=r"C:\Users\admin\Desktop\Tushar\voice controlled Desktop Assistant\chromedriver.exe")
	driver.get("https://facebook.com")
	time.sleep(10)
	username_box = driver.find_element_by_id('email') 
	username_box.send_keys("YourEmail")
	password_box = driver.find_element_by_id('pass') 
	password_box.send_keys("Your password")
	login_box = driver.find_element_by_id('loginbutton') 
	login_box.click() 
	driver.quit()


def wishme():
	hour=int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		say("Good Morning")
	elif hour>=12 and hour<12:
		say("Good AfterNoon")
	else:
		say("Good Evening")

def timee():
	strTime=datetime.datetime.now().strftime("%H:%M:%S")
	say("The time is "+strTime)


def date():
	date_object = datetime.date.today()
	say("todays's date is")
	say(date_object)


def presentyear():
	say("Current year is")
	say(datetime.date.today().year)


def presentmonth():
	d=['JANUARY','FEBUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
	say("Current month is")
	say(d[datetime.date.today().month-1])

