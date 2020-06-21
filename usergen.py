#!/usr/bin/env python3

import random
import linecache

#https://gist.github.com/hugsy/8910dc78d208e40de42deb29e62df913 adj list
#https://gist.github.com/davidbalbert/ac7b813f498de4a1b02e nouns list

nounsList = "nouns.txt"
adjsList = "adjs.txt"

def combineWords(adj, noun, num):
    username = adj + noun + num   
    return username

def readAdj():
    linNum = -1
    file = open(adjsList, "r")
    for line in file:
        linNum=linNum+1

    randLine = random.randint(1,linNum)
    adj = linecache.getline(adjsList, randLine).replace('\n','')

    return adj

def readNoun():
    linNum = -1
    file = open(nounsList, "r")
    for line in file:
        linNum=linNum+1

    randLine = random.randint(1,linNum)
    noun = linecache.getline(nounsList, randLine).replace('\n','')

    return noun

print("============================================")
print("         By github.com/carlslatter16        ")
print("")
print("-----------10 Randomized Usernames-----------")
print("")

for i in range(10):
    print(combineWords(readAdj(),readNoun(), str(random.randint(10,190))))

print("")
print("============================================")