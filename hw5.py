#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 21:44:44 2019

@author: ajay
"""

import Tkinter as Tk
import networkx as nx
import numpy as np

START_X=0
START_Y=0
REC_LEN=50
move_offsets= np.array=[(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]
class knightsTour(object):
    def __init__(self,master=None):
        #make a graph to represent game
        self.board=[]
        #make a list for nodes visited
        self.nodes=[]
        #dict for accessing coords
        self.index={}
        #canvas for game
        self.canvas = Tk.Canvas(master, width=1000, height=1000, bg="white")
        self.canvas.pack()
    def create_board(self,DIM):
        x=START_X
        y=START_Y
        self.width=DIM
        count=0
        self.matrix=np.zeros([REC_LEN*DIM,REC_LEN*DIM])
        for i in range(DIM):
            self.board.append([0]*DIM) 
            for j in range (DIM):
                coord=(x,y) #coordinate tuple
                self.canvas.create_rectangle(x, y,x+REC_LEN, y+REC_LEN,outline="black")
                self.board[i][j]=([count])#tracks game
                self.matrix[x:x+REC_LEN,y:y+REC_LEN]=count
                self.index[count]=coord
                x+=REC_LEN
                count=count+1
            x=x-(REC_LEN*DIM)
            y+=REC_LEN
        self.canvas.create_rectangle(START_X, START_Y,START_X+REC_LEN, START_Y+REC_LEN,fill="orange")
        self.current_pos=[START_X,START_Y]
    def knightsGame(self,DIM):
        self.create_board(DIM)  
        self.canvas.bind("<Button-1>",self.on_mouse) 
        
    def on_mouse(self,event):
       self.haveVisited()
       #do a tour to see all possible moves
       #if possible, make that square current orange and last square blue, add that to list
       X=event.x
       Y=event.y
       rec_num=self.matrix[X][Y] 
       xy_coord=self.index[rec_num]
       in_x=xy_coord[0]
       in_y=xy_coord[1]
       if self.legalMove(X,Y):
           self.canvas.create_rectangle(in_x,in_y,in_x+REC_LEN,in_y+REC_LEN,fill="orange")
           self.nodes.append(rec_num)
           self.current_pos=[in_x,in_y]
       else:
           print "Move not Possible"
    
    def haveVisited(self):
        self.canvas.create_rectangle(START_X, START_Y,START_X+REC_LEN, START_Y+REC_LEN,fill="blue")
        for i in range(len(self.nodes)):
            rec_num=self.nodes[i]
            xy_coord=self.index[rec_num]
            in_x=xy_coord[0]
            in_y=xy_coord[1]
            self.canvas.create_rectangle(in_x,in_y,in_x+REC_LEN,in_y+REC_LEN,fill="blue")
    def legalMove(self,event_X,event_Y):
       rec_num=self.matrix[event_X][event_Y] 
       xy=self.index[rec_num]
       _x=xy[0]
       _y=xy[1]
       difference_x=(_x-self.current_pos[0])/REC_LEN
       difference_y=(_y-self.current_pos[0])/REC_LEN
       move=(difference_x,difference_y)
       for i in range(len(move_offsets)):
           if move==move_offsets[i]:  
               return True
       return False 
"""    
    def tour(self,x_coord,y_coord):
"""

def main(): 
    root = Tk.Tk()
    #dimensions=raw_input('Enter your input:')
    game = knightsTour(root)
    game.knightsGame(5)
    root.mainloop()

if __name__ == '__main__':
    main()