# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 10:55:05 2018

@author: Manu Prasad
"""

import smtplib
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()

#Next, log in to the server
server.login("manu262n@gmail.com", "newpasswordpython")

import random
t='your otp is--    '+str(int(random.random()*100000))



#Send the mail
#msg = "wtf" # The /n separates the message from the headers
server.sendmail("manu262n@gmail.com", "manu262k@gmail.com", t)