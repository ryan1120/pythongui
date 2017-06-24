#!/usr/bin/python

from Tkinter import *
import tkMessageBox
import urllib
import re
import urlparse
from ScrolledText import ScrolledText

top = Tk()
top.title('Read novel tool')


text = ScrolledText(top, width=100, height=5, font=11, spacing1=1, spacing2=1, spacing3=1)

text1 = Text(top, width=100, height=1, font=16)
text11 = Text(top, width=100, height=1, font=16)
text111 = Text(top, width=100, height=1, font=16)

text2 = ScrolledText(top, width=100, height=16, font=16, spacing1=1, spacing2=1, spacing3=1)

base = "http://www.siluke.tw/ny10413/"
# Code to add widgets will go here...


def infocallback():
#    tkMessageBox.showinfo("info", "Scratch success!")
    html = getHtml(base)
    getinfo(html)


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getinfo(html):
    req=r"</dd><dd><a href=\"(.*?)\".*?>(.*?)</a>"
    reqcompile=re.compile(req, re.DOTALL)
    b=re.findall(reqcompile, html)
    b.reverse()
    ind = len(b)
    text.configure(state="normal")
    text.delete(1.0, END)
    for x in b:
        text.insert(INSERT, ind)
        gradeurl = urlparse.urljoin(base, x[0])
        if ind <= 1:
            text.insert(END, '\t'+gradeurl+'\t\t'+x[1])
        else:
            text.insert(END, '\t'+gradeurl+'\t\t'+x[1]+'\n')
        ind -= 1
        if ind == len(b)-1:
            text1.delete(1.0, END)
            text1.insert(1.0, gradeurl)
        if ind == len(b)-2:
            text11.delete(1.0, END)
            text11.insert(1.0, gradeurl)
        if ind == len(b)-3:
            text111.delete(1.0, END)
            text111.insert(1.0, gradeurl)
    text.configure(state="disabled")

def catchtext(s):
    text2.configure(state="normal")
    text2.delete(1.0, END)
    html = getHtml(s)
    gettext(html)


def gettext(html):
    req=r"ead.*?content\">(.*?)</div>"
    reqcompile=re.compile(req, re.DOTALL)
    b=re.findall(reqcompile, html)
    c=b[0].replace('&nbsp;','')
    # text2.insert(INSERT,html)
    # text2.insert(END, '\n')
    # text2.insert(END, '\n')
    text2.insert(INSERT, c.replace('<br /><br />','\n'))
    text2.configure(state="disabled")


# def callback(event):
#     text1.delete(1.0, END)
#     text1.insert(1.0, event.x, event.y)


if __name__ == '__main__':

    B = Button(top, text="Scratch content", command=infocallback, height=2, width=13)
#    B.pack()

    C = Button(top, text="Scratch text", command=lambda: catchtext(text1.get(1.0, END)), height=2, width=13)
    D = Button(top, text="Scratch text", command=lambda: catchtext(text11.get(1.0, END)), height=2, width=13)
    E = Button(top, text="Scratch text", command=lambda: catchtext(text111.get(1.0, END)), height=2, width=13)
    # text.pack()
    # text1.pack()
    # C.pack()
    # text2.pack()
    B.grid(row=1, column=1)
    text.grid(row=1, column=0)
    # text.bind("<Button-1>", callback)
    text1.grid(row=2, column=0)
    C.grid(row=2, column=1)
    text11.grid(row=3, column=0)
    D.grid(row=3, column=1)
    text111.grid(row=4, column=0)
    E.grid(row=4, column=1)
    text2.grid(row=5, column=0)
    # root = Tk()

#    text.insert(INSERT, "Hello.....")
#    text.insert(END, "Bye Bye.....")


    top.mainloop()
