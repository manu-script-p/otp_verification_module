# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 10:55:05 2018

@author: Manu Prasad
"""  

try:
    #inputting  values
    email_id=input("Enter your email address:   ")
    
    
    #generating otp
    import random
    otp=int(random.random()*100000)
    t='Hey there!Your otp for our registration is--    '+str(otp)

    #storing the values
    #from dataio_module import finput
    #finput(email_id,otp)
    

    #Sending otp part
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    #Next, log in to the server
    server.login("#youremail", "#yourpassword")
    #Send the mail
    server.sendmail("#youremail",email_id, t)

    
except Exception:
    print("Invalid Data Entered")

except:
    print("ERROR")    



    