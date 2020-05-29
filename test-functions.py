#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 16:12:54 2020

@author: kash-py
"""
import uuid

print()

    
def highcard(lst):
    if len(lst) != 0:
        lst.sort()
        return lst[-1:][0]


def pair(lst):
    lst = [lst.count(x) for x in lst if lst.count(x) != 1 ]
    if len(lst) == 2:
        return True
    return False
    

def two_pair(lst):
    lst = [lst.count(x) for x in lst if lst.count(x) != 1 ]
    if len(lst) == 4 and 2 in lst:
        return True
    return False
        

def threekind(lst):
    lst = [lst.count(x) for x in lst if lst.count(x) != 1 ]
    if len(lst) == 3:
        return True
    return False


def straight(lst):
    
    lst.sort()
    if 14 in lst:
        lst.pop()
        lst = lst+[1]
        lst.sort()
    
    return True if len([True for x in lst[:-1] for y in lst[1:] if x + 1 == y]) == len(lst[1:]) else False


def fourkind(lst):
    lst = [lst.count(x) for x in lst if lst.count(x) != 1 ]
    if len(lst) == 4 and 4 in lst:
        return True
    return False


def flush(lst):
    
    if lst.count(lst[0]) == len(lst):
        return True
    else:
        return False


def full_house(lst):
    
    return True if len(set(lst)) == 2 else False







lst2 = [11,2,3,14,5]  

print(highcard(lst2))
  
print(pair(lst2))
print(two_pair(lst2))
print(threekind(lst2))
print(straight(lst2))
print(fourkind(lst2))
print(full_house(lst2))
 
    
suits = ['Heart','Heart','Heart','Heart','spade']    
    
#print(flush(suits))    
    
       