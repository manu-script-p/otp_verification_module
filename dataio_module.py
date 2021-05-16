# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 16:07:23 2018

@author: Manu Prasad
"""

def finput(email_id,otp):
    fin=open("database_module.txt","w")
    var=email_id+"    "+str(otp)
    fin.write(var)
    fin.close()


def foutput():
    fout=open("database_module.txt","r")
    print(fout.read()) 
    fout.close()
  
        

    