#!/usr/bin/env python

class calculator:
    def __init__(self):
        pass

    def add(self,x,y):
        return x+y

    def sub(self,x,y):
        return x-y

    def mult(self,x,y):
        return x*y

    def div(self,x,y):
        return x/y
cal=calculator()
print(cal.add(2,3))
print(cal.sub(2,3))
print(cal.mult(2,3))
print(cal.div(2,3))
