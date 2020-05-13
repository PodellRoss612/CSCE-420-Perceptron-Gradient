# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 20:10:53 2020

@author: Ross Podell
"""

import random
import matplotlib.pyplot as plt
import numpy as np
def main():
    #testType = input()
    testType = "OR"
    t = 0
    w1 = random.uniform(-6, 6) #initialize random starting weights
    w2 = random.uniform(-6, 6)
    xInput = [0,0,1,1]
    yInput = [0,1,0,1]
    answer = []
    end = 0
    fig, axis = plt.subplots()
    if testType == "AND":
        t = 1.5
        answer = [0,0,0,1]
        axis.plot(0, 0, "ro")
        axis.plot(0, 1, "ro")
        axis.plot(1, 0, "ro")
        axis.plot(1, 1, "go")
    elif testType == "OR":
        t = 0.5
        answer = [0,1,1,1]
        axis.plot(0, 0, "ro")
        axis.plot(0, 1, "go")
        axis.plot(1, 0, "go")
        axis.plot(1, 1, "go")
    elif testType == "XOR":
        answer = [0,1,1,0]
        axis.plot(0, 0, "ro")
        axis.plot(0, 1, "go")
        axis.plot(1, 0, "go")
        axis.plot(1, 1, "ro")
    else:
        print("invalid test type")
        return
    results = []
    while results != answer:
        results = []
        for x in range(0,4):
            output = w1*xInput[x] + w2*yInput[x] - t
            if output > 0:
                results.append(1)
            elif output <= 0:
                results.append(0)
        if testType == "XOR":
            end+=1
            if end == 9:
                results = answer
        for x in range(0,4):
            if results[x] < answer[x]:
                if w1 < w2:
                    w1+= 0.1
                else:
                    w2+= 0.1
                break
            if results[x] > answer[x]:
                if w1 > w2:
                    w1-= 0.1
                else:
                    w2-= 0.1
                break
    x = np.linspace(0, 2, 100)
    axis.plot(x, (-w1/w2*x + t/w2))
    
if __name__ == "__main__":
    main()