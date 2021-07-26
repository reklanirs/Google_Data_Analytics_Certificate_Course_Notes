#!/usr/local/bin/python3
# -*- coding: utf-8 -*- 
import os,re,sys,time
import subprocess,shlex
import math,random
import requests,json
import unicodedata

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
#sys.stdin=open('in.txt','r')

def strrepl(obj):
    return f"![](attachments/{obj.group(0)[3:-2]})"

def repfile(f):
    os.system(f'cp "{f}" "{f+".bk"}"')
    l = []
    with open(f, 'r') as fin:
        l = fin.readlines()
    l = [re.sub("!\[\[.+?\]\]", strrepl, i) for i in l]
    with open(f, 'w') as fout:
        for i in l:
            fout.write(i)
        fout.flush()
    pass

def main():
    print(sys.argv)
    for i in range(1, len(sys.argv)):
        repfile(sys.argv[i])
    pass

if __name__ == '__main__':
    main()
    