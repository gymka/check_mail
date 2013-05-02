#!/usr/bin/env python
import imaplib
import base64
import os
f = open('pass.txt','r')
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
	print("gymka@archlinux.lt: %s\n" % box1)
	
if box2>0:
	print("margevicius.algimantas: %s\n" % box2)
	
if box3>0:
	print("gymka@mail.ru: %s\n" % box3)

laisku=box1+box2+box3

if laisku>0:
	os.system("mplayer /home/gymka/.config/email/DingDongNewEmail.wav")

