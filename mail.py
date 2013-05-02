#!/usr/bin/env python
import imaplib
import base64
import os
import time
import email
laiskai = ""
def check_mail():
	global laiskai
	f = open('/home/gymka/Dev/source/check_mail/pass.txt','r')
	lines = f.readlines()
	pass1 = bytes(lines[0],'utf-8')
	pass2 = bytes(lines[1],'utf-8')
	pass3 = bytes(lines[2],'utf-8')
	f.close()

	obj = imaplib.IMAP4_SSL('imap.gmail.com','993')
	obj.login('gymka@archlinux.lt',base64.decodestring(pass1).decode("utf-8"))
	obj.select()
	obj.search(None,'UnSeen')

	obj2 = imaplib.IMAP4_SSL('imap.gmail.com','993')
	obj2.login('margevicius.algimantas',base64.decodestring(pass2).decode("utf-8"))
	obj2.select()
	obj2.search(None,'UnSeen')

	obj3 = imaplib.IMAP4_SSL('imap.mail.ru','993')
	obj3.login('gymka@mail.ru',base64.decodestring(pass3).decode("utf-8"))
	obj3.select()
	obj3.search(None,'UnSeen')

			
	box1 = len(obj.search(None, 'UnSeen')[1][0].split())
	box2 = len(obj2.search(None, 'UnSeen')[1][0].split())
	box3 = len(obj3.search(None, 'UnSeen')[1][0].split())

	if box1>0:
		z=1
		while (z <= box1):
			try:
				laiskai += "Nuo: %s\nTema: %s\n" % parse_mail(-z,obj)
			except TypeError:
				print('no mail')
			z += 1		
	if box2>0:
		y=1
		while (y <= box2):
			try:
				laiskai += "Nuo: %s\nTema: %s\n" % parse_mail(-y,obj2)
			except TypeError:
				print('no mail')
			y += 1	
		
	if box3>0:
		i=1
		while (i <= box3):
			try:
				laiskai += "Nuo: %s\nTema: %s\n" % parse_mail(-i,obj3)
			except TypeError:
				print('no mail')
			i += 1	

	laisku=box1+box2+box3

	if laisku>0:
		os.system("mplayer /home/gymka/Dev/source/check_mail/DingDongNewEmail.wav >/dev/null 2>&1")
		cmd="export DISPLAY=:0; notify-send -i \"/home/gymka/Dev/source/check_mail/mail.png\" \"Paštas:\n"+laiskai+"\""
		os.system(cmd)
		laiskai = ""
		
def parse_mail(n,b):
		try:
			result, data = b.uid('search',None,'Unseen')
			latest_email_uid = data[0].split()[n]
			result, data = b.uid('fetch', latest_email_uid, '(BODY.PEEK[HEADER])')
			raw_email = data[0][1]
			email_message = email.message_from_string(raw_email.decode('utf-8'))
			sub=email_message['Subject']
			fro=email_message['From']
			return (fro,sub)
		except IndexError:
			print('no mail')
			
while (1==1):
    check_mail()
    time.sleep(300)
