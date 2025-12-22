#Import librairies
import os
from data_loader import *
from data_visualization import *
from formula import *
import numpy as np

#variable
dataset=r"data\raw.csv"

#Hyper-parameters
epoch=10
learning_rate=0.01
lamda=1

#Pre process dataset
data=load(dataset)
show_df(data)
transform(data)

#graphs part
#matrice(data)
#hist(data)
#distribution(data,"is_goal")

