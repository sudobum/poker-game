#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:48:07 2020

@author: kash-py
"""
import random



class Card( object ):
    def __init__(self,name, value, suit):
        self.value = value
        self.suit = suit
        self.name = name
        self.showing = False
        
    def __repr__(self):
        if self.showing:
            return "{} of {}".format(str(self.name), str(self.suit), )
        else:
            return "Card"
    
    


class StandardDeck(list):
    
    def __init__(self):
        self.cards = []
        suits = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
        values = {'Two':2,'Three':3,'Four':4,
                  'Five':5,'Six':6,'Seven':7,
                  'Eight':8,'Nine':9,'Ten':10,
                  'Jack':11,'Queen':12,'King':13,'Ace':14}
        # ace can be used as a low card in straight
        
        #second value represents actual value
        [ self.cards.append(Card(name, values[name], suit))  for name in values  for suit in suits]
    def __repr__(self):
        return 'Standard Deck of Cards {} cards'.format(len(self.cards))
    
    
    def shuffle(self, times=1):
        random.shuffle(self.cards)
        print('Deck Shuffled')
        
    def deal(self):
        return self.cards.pop(0)
        
    
    













