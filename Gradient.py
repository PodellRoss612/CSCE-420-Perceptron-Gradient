# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 16:48:39 2020

@author: Ross Podell
"""
import random
import matplotlib.pyplot as plt
def main():
    
    x = -2.0
    xlst = []
    ylst = []
    while x <= 6:
        xlst.append(x)
        ylst.append((x + 1) * (x - 1) * (x - 3) * (x - 4 ))
        x += 0.01
    fig, axis = plt.subplots()
    axis.plot(xlst,ylst, label="E(w)") #graph E(w) function
    l = float(input()) 
    w = random.uniform(-2,6) #initialize random starting w
    wStart = w
    endLoop = False
    axis.plot(w, (w + 1) * (w - 1) * (w - 3) * (w - 4 ), 'go', label= "initial w: " + str(wStart))
    while endLoop == False:
        dW = -l * (4.0*(w**3) - 21.0*(w**2) + 22.0*w + 7) #get delta w
        w = w + dW #update w
        axis.plot(w, (w + 1) * (w - 1) * (w - 3) * (w - 4 ), 'ko')
        if abs(dW) < 0.0001:
            axis.plot(w, (w + 1) * (w - 1) * (w - 3) * (w - 4 ), 'ro', label= "final w: " + str(w))
            endLoop = True
    axis.set_title("Question 12")
    axis.legend()
    
    
    
    
if __name__ == "__main__":
    main()