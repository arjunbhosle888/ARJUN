# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 15:22:54 2026

@author: User
"""

year=int(input("Enter Year:"))
if(year%400==0)or(year%4==0 and year%100!=0):
  print("Leap Year")


else:
    print("Not a Leap Year")
    