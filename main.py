#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:48:07 2020

@author: kash-py
"""
import random
import uuid


class Card( object ):
    
    def __init__(self,name, value, suit):
        self.value = value
        self.suit = suit
        self.name = name
        self.showing = True
        
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
        
    
    
class Player(object):
    def __init__(self, name):
        self.cards = []
        self.name = name
    def __repr__(self):
        return 'Player:{} Hand:{}'.format(self.name, self.cards)





class Table(object):
    def __init__(self,number_of_players=3):
        self.deck = StandardDeck()
        self.deck.shuffle()
        self.cards = []
        self.players = []
        for i in range(number_of_players):
            random_name = str(uuid.uuid1()).split('-')[0]
            self.players.append(Player(random_name))
            
    def __repr__(self):
        return '{}{}'.format(self.cards, self.players)
    
    def deal_to_players(self):
        for player in self.players:
            player.cards.append(self.deck.deal())
            
    def deal_table_flop(self):
        for i in range(3):
            self.cards.append(self.deck.deal())
            
    def deal_table_turn(self):
            self.cards.append(self.deck.deal())
            
    def deal_table_river(self):
            self.cards.append(self.deck.deal())        



        



















