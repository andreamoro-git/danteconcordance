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

p = dantePage()
nlines = p.epbounds[100]-p.epbounds[0]
randline = round(nlines*np.random.rand())+p.epbounds[0]

for idx,bound in enumerate(p.epbounds):
    if randline<=p.epbounds[idx+1]:
        cantorand = randline - bound
        startoffset = cantorand % 3
        begin = randline-startoffset
        end = randline-startoffset+3
        
        if idx==33 or idx==66:
            if end>=p.epbounds[idx+1]-3:
                end = p.epbounds[idx+1]-2
        else:
            if end>=p.epbounds[idx+1]-2:
                end = p.epbounds[idx+1]-1
        while end-begin<3:
            begin = begin-3
        randomterc = p.lines[begin:end]
        break

randomterc = [line.strip() for line in randomterc]
tercstr = "\n".join(randomterc)

verses = " ("+str(cantorand-startoffset+1) + "-" + str(cantorand-startoffset+1+len(randomterc))+")"

if idx<34:
    cantica = 'Inf'
    canto = idx+1
elif idx < 67:
    cantica = 'Purg'
    canto = idx-33
else:
    cantica = 'Par'
    canto = idx-66

tweet = (tercstr + "\n\n-- " + p.epnames[idx].strip() + verses
         + "\n\nCommenti: https://dante.princeton.edu/cgi-bin/dante/campuscgi/mpb/GetCantoSection.pl?INP_POEM="
         + cantica + '&INP_SECT=' + str(canto) + "&INP_START=1&INP_LEN=150&LANG=2"
         + "\nConcordanze:  https://danteconcordance.andreamoro.net/dantepage.py?e="
         + str(idx+1).strip()
         + "#row"+str(begin-p.epbounds[idx]+1)
         )

with open('path-/creds-twitter') as f:
    lines = f.read().splitlines()

twitter = Twython(lines[0], lines[1], lines[2], lines[3])
twpost = twitter.update_status(status= tweet)

import facebook
with open('path-/creds-facebook') as f:
    lines = f.read().splitlines()
graph = facebook.GraphAPI(access_token= lines[0], version="3.1")

fbpost = graph.put_object(parent_object='me', connection_name='feed', message=tweet)

print(tweet)
print('\nfacebook: ', fbpost)
print('twitter: ', twpost['user']['name']+'/'+str(twpost['id']))
