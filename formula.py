import numpy as np

def sigmoid(x):
    o_x=1/(1+np.exp(-x))
    return o_x

def gradient(p,goal):
    g=p-goal
    return g

def hessien(p):
    h=p*(1-p)
    return h

def Gain(g,h):
    G=0.5
    return G