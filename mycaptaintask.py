# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 20:20:19 2022

@author: Lenovo
"""

PI=3.14
r=float(input("Enter the radius of the circle:"));
area=PI*r*r
print("Area of the circle is ",area)
fn=input("Enter the file name:")
f=fn.split(".")
print("Extension of the file name is "+f[-1])