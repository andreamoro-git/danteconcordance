# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from twython import Twython, TwythonError 
import numpy as np
np.random.rand()
  
# setting path
from dantepage import dantePage

p = dantePage(episodeN=3)

nlines = p.epbounds[100]-p.epbounds[0]
randline = round(nlines*np.random.rand())

for idx,bound in enumerate(p.epbounds):
    if randline<p.epbounds[idx+1]:
        cantorand = randline - bound
        startoffset = cantorand % 3
        randomterc = p.lines[randline-startoffset:randline-startoffset+3]
        break

with open('creds-twitter') as f:
    lines = f.read().splitlines()


twitter = Twython(lines[0], lines[1], lines[2], lines[3])
twitter.update_status(status=randomterc[0].strip()+"\n"+
                             randomterc[1].strip()+"\n"+
                             randomterc[2].strip()+
                             "\n\n" +
                             p.epnames[idx].strip()   +
                             " \nhttps://danteconcordance.andreamoro.net/dantepage.py?e=" + str(idx+1).strip() +
                             "#row"+str(cantorand-startoffset+1) +
                             '' )


