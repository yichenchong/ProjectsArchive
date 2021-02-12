# Import Tkinter
import sys
if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as tk
    from Tkinter import *
else:
    # Python 3
    import tkinter as tk
    from tkinter import *

# Receive Input through Tinkter
class takeInput(object):
    def __init__(self,requestMessage):
        self.root = Tk()
        self.string = ''
        self.frame = Frame(self.root)
        self.frame.pack()        
        self.acceptInput(requestMessage)
    def acceptInput(self,requestMessage):
        r = self.frame
        k = Label(r,text=requestMessage)
        k.pack(side='left')
        self.e = Entry(r,text='Name')
        self.e.pack(side='left')
        self.e.focus_set()
        b = Button(r,text='Solve!',command=self.gettext)
        b.pack(side='right')
    def gettext(self):
        self.string = self.e.get()
        self.root.destroy()
    def getString(self):
        return self.string
    def waitForInput(self):
        self.root.mainloop()
def getText(requestMessage):
    msgBox = takeInput(requestMessage)
    #loop until the user makes a decision and the window is destroyed
    msgBox.waitForInput()
    return msgBox.getString()


# Receives original input
word = getText('Enter the letters').lower()
wordSet = set(list(word))
wordSetDict = {i:word.count(i) for i in wordSet}

# Sets up dictionary
import os
currentPath = sys.path[0]
currentPath = currentPath.replace("/lib/python36.zip","")
pathToDictionary = os.path.join(currentPath,"corncob_lowercase.txt")
handle=open(pathToDictionary,'r+')
dictionaryText = handle.read()

# Loads the corncob word list into a list
dictionaryWords = dictionaryText.split("\r\n")
print(dictionaryWords)
wordList = []

def isPermutation(eachWord):
    # creates a dictionary for the letter frequencies of each word
    eachWordSet = set(list(eachWord))
    eachWordDict = {i:eachWord.count(i) for i in eachWordSet}
    # makes sure theres enough letters for each letter in the dictionary word, in the input word
    for i in eachWordDict:
        if wordSetDict[i] < eachWordDict[i]:
            return False
    return True

# Simplifies dictionary so that "long" words don't exist
# "Long" words are defined as words that have any letters that don't exist in the input word
# This first sweep through the dictionary creates a much shorter word list, and so decreases the
# time complexity of the spell check function later
finalList = filter(isPermutation, dictionaryWords)

# Removes weird double glitch, and sorts
finalList = list(set(finalList))
finalList.sort()
finalList.sort(key = len)

# Final output
finalString = "\n".join(str(e) for e in finalList)
print(finalString)

#Output window
window = Tk()
window.title("Solved!")
scrollbar = Scrollbar(window)
scrollbar.pack( side = RIGHT, fill = Y )
mylist = Listbox(window, yscrollcommand = scrollbar.set )
for i in range(len(finalList)):
   mylist.insert(END, finalList[i])
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )
window.mainloop()

import tkinter.scrolledtext as tkst

win = tk.Tk()
win.title("Solved!")
frame1 = tk.Frame(
    master = win,
    bg = '#808000'
)
frame1.pack(fill='both', expand='yes')
editArea = tkst.ScrolledText(
    master = frame1,
    wrap   = tk.WORD,
    width  = 20,
    height = 10
)

editArea.pack(padx=0, pady=0, fill=tk.BOTH, expand=True)
editArea.insert(tk.INSERT,
finalString)
win.mainloop()