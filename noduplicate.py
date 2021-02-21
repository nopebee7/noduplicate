# Sak Karepmu Mek Nopo

import os
import random
import sys
import time

c = ["\033[31m", "\033[32m", "\033[33m",
     "\033[34m", "\033[35m", "\033[36m", "\033[37m"]
output = open("SiteCleaned.txt", "a+")
tmp = []

def logo():
    if "nt" in os.name:
        os.system("cls")
    else:
        os.system("clear")

    logo = """
     _   __      ____              ___            __     
    / | / /___  / __ \__  ______  / (_)________ _/ /____ 
   /  |/ / __ \/ / / / / / / __ \/ / / ___/ __ `/ __/ _ \\
  / /|  / /_/ / /_/ / /_/ / /_/ / / / /__/ /_/ / /_/  __/
 /_/ |_/\____/_____/\__,_/ .___/_/_/\___/\__,_/\__/\___/ 
                       /_/ {y}by {w}: {y}nopebee7
    """.format(y=c[2], w=c[6])
    for line in logo.split("\n"):
        print(random.choice(c)+line)
        time.sleep(0.1)

def check (word):
    global output
    word = word.replace("\n", "").replace("\r", "")
    if word not in tmp:
        tmp.append(word)
        output.write(word+"\n")
    else:
        print(" {w}[{r}-{w}] {y}duplicate : ".format(w=c[6], y=c[2], r=c[0])+word)

def isThread (thread, wordList):
    try: from multiprocessing.dummy import Pool
    except: print(" {w}[{r}-{w}] {b}pip {w}install {y}multiprocessing".format(w=c[6], b=c[3], y=c[2], r=c[0])); exit()
    pool = Pool(thread)
    pool.map(check, wordList)
    pool.close()
    pool.join()     

if __name__ == "__main__":
    logo()
    fileName = raw_input(
        " {w}[{g}+{w}] {y}the list {w}> ".format(w=c[6], g=c[1], y=c[2]))
    if not os.path.exists(fileName):
        print(" {w}[{r}-{w}] {y}file not found".format(w=c[6], r=c[0], y=c[2]))
        exit();
    useThread = raw_input(" {w}[{g}+{w}] {y}use thread {w}[{y}y{w}/{y}N{w}]? {w}> ".format(w=c[6], g=c[1], y=c[2]))
    if useThread.lower() == "y":
        thread = raw_input(" {w}[{g}+{w}] {y}thread {w}> ".format(w=c[6], g=c[1], y=c[2]))
        try: thread = int(thread)
        except: print(" {w}[{r}-{w}] {y}thread must be int".format(w=c[6], r=c[0], y=c[2]))
        isThread(thread, open(fileName, "r+").readlines())
    else:
        for word in open(fileName, "r+").readlines():
            word = word.replace("\n", "").replace("\r", "")
            check(word)
            
# Copyright 2021 nopebee7