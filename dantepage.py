#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:05:17 2018

@author: Andrea Moro, andrea at andreamoro.net
"""

from collections import OrderedDict

def write_roman(num):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num > 0:
                roman_num(num)
            else:
                break

    return "".join([a for a in roman_num(num)])

from htmlpage import htmlPage
import os,re
import urllib.parse

class dantePage (htmlPage):

    def __init__ (self,episodeN=0,word="",wholeword='on',t='',h=''):
        htmlPage.__init__ (self, t,h)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        textFile = open(dir_path+"/1012-0.txt","r")
        self.lines = textFile.read().split("\n")
        # remove empty lines
        self.lines = list(filter(None,self.lines))

        try :
            self.url = os.environ['QUERY_STRING']
            query = urllib.parse.parse_qs(self.url)
        except :
            query = list()
            print('')

        self.episodeN = 0
        if 'e' in query :
            self.episodeN = int(query['e'][0])
        else :
            self.episodeN = episodeN
        if 'w' in query :
            self.word = query['w'][0]
        else :
            self.word = word
        if 'cs' in query :
            self.casesens = query['cs'][0]
        else :
            self.casesens = 'off'
        if 'ww' in query :
            self.wholeword = query['ww'][0]
        else :
            self.wholeword = wholeword

        self.cantiche = ('Inferno','Purgatorio','Paradiso')
        self.canti = {self.cantiche[0]:34,self.cantiche[1]:33,self.cantiche[2]:33}

        self.epbounds = list()
        self.epnames = list()
#        for cantica in self.cantiche :
#            for canto in range(self.canti[cantica]) :
#                searchString = '  '+cantica+' • Canto '+write_roman(canto+1)
#                self.epnames.append(searchString)
#                self.epbounds.append(self.lines.index(searchString))
#        self.epbounds.append(self.lines.index('  l’amor che move il sole e l’altre stelle.')+1)
#        print(self.epbounds)
#        print(self.epnames)
#        return self.epbounds

        self.epbounds = [22, 159, 302, 439, 591, 734, 850, 981, 1112, 1246, 1383, 1499, 1639, 
                         1791, 1934, 2059, 2196, 2333, 2470, 2604, 2735, 2875, 3027, 3176, 3328, 
                         3480, 3623, 3760, 3903, 4043, 4192, 4338, 4478, 4636, 4777, 4914, 5048, 
                         5194, 5334, 5471, 5623, 5760, 5900, 6046, 6186, 6329, 6466, 6621, 6773, 
                         6919, 7065, 7205, 7351, 7497, 7649, 7786, 7941, 8075, 8230, 8370, 8519, 
                         8662, 8811, 8966, 9112, 9258, 9419, 9566, 9709, 9858, 9989, 10132, 10272, 
                         10415, 10564, 10713, 10856, 11005, 11145, 11291, 11434, 11574, 11723, 11878, 
                         12021, 12158, 12307, 12456, 12599, 12754, 12894, 13049, 13189, 13332, 13481, 
                         13621, 13767, 13916, 14059, 14211, 14356]
        self.epnames = ['  Inferno • Canto I', '  Inferno • Canto II', '  Inferno • Canto III',
                        '  Inferno • Canto IV', '  Inferno • Canto V', '  Inferno • Canto VI',
                        '  Inferno • Canto VII', '  Inferno • Canto VIII', '  Inferno • Canto IX',
                        '  Inferno • Canto X', '  Inferno • Canto XI', '  Inferno • Canto XII',
                        '  Inferno • Canto XIII', '  Inferno • Canto XIV', '  Inferno • Canto XV',
                        '  Inferno • Canto XVI', '  Inferno • Canto XVII', '  Inferno • Canto XVIII',
                        '  Inferno • Canto XIX', '  Inferno • Canto XX', '  Inferno • Canto XXI',
                        '  Inferno • Canto XXII', '  Inferno • Canto XXIII', '  Inferno • Canto XXIV',
                        '  Inferno • Canto XXV', '  Inferno • Canto XXVI', '  Inferno • Canto XXVII',
                        '  Inferno • Canto XXVIII', '  Inferno • Canto XXIX', '  Inferno • Canto XXX',
                        '  Inferno • Canto XXXI', '  Inferno • Canto XXXII', '  Inferno • Canto XXXIII',
                        '  Inferno • Canto XXXIV', '  Purgatorio • Canto I', '  Purgatorio • Canto II',
                        '  Purgatorio • Canto III', '  Purgatorio • Canto IV', '  Purgatorio • Canto V',
                        '  Purgatorio • Canto VI', '  Purgatorio • Canto VII', '  Purgatorio • Canto VIII',
                        '  Purgatorio • Canto IX', '  Purgatorio • Canto X', '  Purgatorio • Canto XI',
                        '  Purgatorio • Canto XII', '  Purgatorio • Canto XIII', '  Purgatorio • Canto XIV',
                        '  Purgatorio • Canto XV', '  Purgatorio • Canto XVI', '  Purgatorio • Canto XVII',
                        '  Purgatorio • Canto XVIII', '  Purgatorio • Canto XIX', '  Purgatorio • Canto XX',
                        '  Purgatorio • Canto XXI', '  Purgatorio • Canto XXII', '  Purgatorio • Canto XXIII',
                        '  Purgatorio • Canto XXIV', '  Purgatorio • Canto XXV', '  Purgatorio • Canto XXVI',
                        '  Purgatorio • Canto XXVII', '  Purgatorio • Canto XXVIII', '  Purgatorio • Canto XXIX',
                        '  Purgatorio • Canto XXX', '  Purgatorio • Canto XXXI', '  Purgatorio • Canto XXXII',
                        '  Purgatorio • Canto XXXIII', '  Paradiso • Canto I', '  Paradiso • Canto II',
                        '  Paradiso • Canto III', '  Paradiso • Canto IV', '  Paradiso • Canto V',
                        '  Paradiso • Canto VI', '  Paradiso • Canto VII', '  Paradiso • Canto VIII',
                        '  Paradiso • Canto IX', '  Paradiso • Canto X', '  Paradiso • Canto XI',
                        '  Paradiso • Canto XII', '  Paradiso • Canto XIII', '  Paradiso • Canto XIV',
                        '  Paradiso • Canto XV', '  Paradiso • Canto XVI', '  Paradiso • Canto XVII',
                        '  Paradiso • Canto XVIII', '  Paradiso • Canto XIX', '  Paradiso • Canto XX',
                        '  Paradiso • Canto XXI', '  Paradiso • Canto XXII', '  Paradiso • Canto XXIII',
                        '  Paradiso • Canto XXIV', '  Paradiso • Canto XXV', '  Paradiso • Canto XXVI',
                        '  Paradiso • Canto XXVII', '  Paradiso • Canto XXVIII', '  Paradiso • Canto XXIX',
                        '  Paradiso • Canto XXX', '  Paradiso • Canto XXXI', '  Paradiso • Canto XXXII',
                        '  Paradiso • Canto XXXIII']



    def findEpisode(self,row) :
        thisep = 0
        for ep in range(len(self.epnames)) :
            if row >= self.epbounds[ep]:
                thisep= ep
        return thisep

    def addEpLink(self,num,text="",word="") :
        ep = self.findEpisode(num)
        if text == '' :
            text = '[ ]'
        rowtext = ""
        rowtext += "<div><span class='rown' id='row" + str(num) + "'>  \n"
        rowtext += "[<a href='?w="+word+"&e="+str(ep+1)+"#row" + str(max(1,num-self.epbounds[ep]+1-5))+ "'>"+str(num-self.epbounds[ep]+1)+"</a>]\n"

        rowtext += "</span>\n"
        rowtext += '<span class="row">'+text+'</span></div>'
        rowtext += "\n"

        return rowtext

    def addNameAnchor(self,num,text="") :
        if text == '' :
            text = '&nbsp;'
        rowtext =  ""
        rowtext += '<div><span class="rown" id="row'+str(num)+'">['+str(num)+']</span>'
        rowtext += '<span class="row">'+text+'</span></div>'
        rowtext += "\n"

        return rowtext

    def printEpisodeList(self) :
        html = ""
        html += "<div id='list'><h2> Testo dei Canti </h2>\n"
        html += "<form method='get' action='dantepage.py'>\n<select onchange='this.form.submit()' name='e'>"
        selected = ''
        # inferno
        if self.episodeN>34 :
            selected = ' selected '
        html += "<option value = ''"+selected+">Inferno</option>\n"
        for bound in range(34) :
            if self.episodeN == bound+1 :
                selected = ' selected '
            else :
                selected = ' '
            html += "<option value='"+str(bound+1)+"' "+selected+'>'+self.epnames[bound]+ "</option> \n"
        html += "</select></form>\n"
        html += "<form method='get' action='dantepage.py'><select onchange='this.form.submit()' name='e'>"

        # purgatorio
        if self.episodeN<=34 or self.episodeN>67 :
            selected = ' selected '
        html += "<option value = ''"+selected+">Purgatorio</option>\n"
        for bound in range(34,67) :
            if self.episodeN == bound+1 :
                selected = ' selected '
            else :
                selected = ' '
            html += "<option value='"+str(bound+1)+"' "+selected+'>'+self.epnames[bound]+ "</option> \n"
        html += "</select></form>\n"
        html += "<form method='get' action='dantepage.py'><select onchange='this.form.submit()' name='e'>"
        if self.episodeN<=67 :
            selected = ' selected '
        html += "<option value = ''"+selected+">Paradiso</option>\n"
        for bound in range(67,100) :
            if self.episodeN == bound+1 :
                selected = ' selected '
            else :
                selected = ' '
            html += "<option value='"+str(bound+1)+"' "+selected+'>'+self.epnames[bound]+ "</option> \n"
        html += "</select></form>\n"
        html += "</div>\n"

        return html

    def printForm(self) :
        if self.casesens =='on' :
            checked = 'checked'
        else:
            checked = ''
        if self.wholeword != 'off' :
            wwchecked = 'checked'
        else:
            wwchecked = ''
        html = ''
        html += "<h2>Ricerca parole</h2>\n<form action ='dantepage.py'> \n"
        inputvalue = ' '
        if self.word != '' :
            inputvalue = 'value = "'+self.word+'"'
        html += "<input type='text' name='w' "+inputvalue+" > \n"
        html += "<input type='submit' class='addlinks' value='Search' > \n"
        html += " <input type='checkbox' name='cs' " + checked +"> case sensitive \n"
        html += " <input type='checkbox' name='ww' " + wwchecked +"> parola intera\n"
        html += "<input type='hidden' name='ww' value='off' >"
        html += "</form>\n "

        return html

    def printCountForm(self) :
        if self.casesens=='on' :
            checked = 'checked'
        else:
            checked = ''
#        if self.wholeword != 'off' :
#            wwchecked = 'checked'
#        else:
#            wwchecked = ''
        html = ''
        html += "<h2>Count words</h2>\n<form action ='dantecounts.py'> \n"

        #episode
        html += '<select onchange="this.form.submit()" name="e">\n'
        selected = ''
        if self.episodeN == 0 :
            selected = ' selected '
        else :
            selected = ' '
        html+= '<option value="0" '+selected+' >All text</option>\n'
        for ep in self.epnames :
            selected = ''
            if ( ep == self.epnames[self.episodeN-1] and self.episodeN>0 ) :
                selected = ' selected '
            html+= '<option value="'+str(self.epnames.index(ep)+1)+'" '+selected+' >'
            html+= ep+"</option>\n"
        html += "</select>\n"

        #checkboxes
        html += " <input type='checkbox' name='cs' " + checked +"> case sensitive \n"
#        html += " <input type='checkbox' name='ww' " + wwchecked +" disabled> whole word \n"
        html += "<input type='hidden' name='ww' value='off' >"
        html += "<input type='submit' class='addlinks' value='Count' > \n"
        html += "</form>\n"

        return html

    def generate_body (self):
        episodeN = self.episodeN
        Nepisodes = len(self.epbounds)-1

        # remove title and author
        lines = self.lines[self.epbounds[0]:self.epbounds[Nepisodes]]
        lines = self.lines
   #     p.epbounds=[x - p.epbounds[0] for x in p.epbounds]

        html = ""

        html+= self.printEpisodeList()

        html+= "<div id='form'>\n"
        html+= self.printForm()
        html+= self.printCountForm()
        html+= "</div>\n"

        html += "<div id='text'>\n"

        # word search
        if self.episodeN == 0 and self.word != '':
            searchString = self.word
            if self.casesens == 'on' :
                foundLines = [lines.index(x) for x in lines if searchString in x]
                notifystring = ' - case sensitive'
            else :
                foundLines = [lines.index(x) for x in lines if searchString.lower() in x.lower()]
                notifystring = ' - not case sensitive '

            #remove instances where not the whole word
            if self.wholeword == 'on':
                notifystring +=  ' - parola intera '
                keepFoundLines = list(foundLines)
                for fline in foundLines:
                    if self.casesens =='on' :
                        if not self.word in re.split("\W+",lines[fline]) :
                            keepFoundLines.remove(fline)
                    else :
                        if not self.word.lower() in re.split("\W+",lines[fline].lower()) :
                            keepFoundLines.remove(fline)
                foundLines = keepFoundLines

            #count hits
            counthits = 0
            for fline in foundLines:
                if self.casesens =='on' :
                    counthits+= lines[fline].count(self.word)
                else :
                    counthits+= lines[fline].lower().count(self.word.lower())


            # display output
            html+= "<h2>Ricerca: "+self.word+" - "+str(counthits)+" casi "+notifystring+"</h2>\n"

            thisEpisode = -1
            for line in foundLines :
                lineEpisode = self.findEpisode(line)
                if lineEpisode > thisEpisode:
                    html+= "<h3>"+str(lineEpisode+1)+". "+self.epnames[lineEpisode]+"</h3>"
                    thisEpisode = lineEpisode

                html+= self.addEpLink(line,lines[line],self.word) + "\n"

        # display full episode
        elif episodeN > 0 :
            html+= "<h2>"+self.epnames[episodeN-1]+"</h2>\n"
            start = self.epbounds[episodeN-1]
            end = self.epbounds[episodeN]-1
            if episodeN==34 or episodeN==67 :
                end = end-1
            verse = 0
            for lineN in range(start,end):
                if (lines[lineN] != '') :
                    verse += 1
                html+= self.addNameAnchor(str(verse),lines[lineN]) + "\n"
                if verse%3 == 0 and lineN+2 != end:
                    html+= '<div> &nbsp</div>'
            if episodeN==100 :
                html+= self.addNameAnchor(str(verse),lines[end]) + "\n"
        html+= "</div>\n"
        if episodeN<Nepisodes and episodeN>0:
            html+= "<div id='sandbox'>\n"
            html+= "<a href='dantepage.py?e="+str(episodeN+1)
            html+= "'>Successivo: "+self.epnames[episodeN]+"</a>\n"
            html+= "</div>\n"
            #html+= str(start)+'aa'+str(end)

        return html


if __name__ == "__main__":
    p = dantePage(episodeN=0,word='',t="Concordanze nella Divina Commedia di Dante (beta)",
                    h="Concordanze nella Divina Commedia di Dante (beta)")
    print(p.generate())
    #print(p.episodeN)
