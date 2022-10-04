# import packages
import PyPDF2
import re
import os.path

def textSearch(targetpath,wordlist,name,returnpath):
    x = len(targetpath)
    #differentiation between path with or without quotation marks
    if targetpath[0] == '"' or targetpath[0]== "'" : 
        object = PyPDF2.PdfFileReader(r"{}".format(targetpath[1:x-1]))
    else :
        object = PyPDF2.PdfFileReader(r"{}".format(targetpath))
    #create new PDF
    writer = PyPDF2.PdfWriter()
    # get number of pages
    NumPages = object.getNumPages()
    #PDF starting page 
    i = 0
    #Page visit marker
    VisitedPage = [0] * NumPages

    
    for i in range(0, NumPages):
        #Extract text
        PageObj = object.getPage(i)
        Text = PageObj.extractText() 
        #Search page for target words
        for x in wordlist:
            ResSearch = re.search(x, Text)
            #Add pages with target text and avoid duplicate additions
            if ResSearch != None and VisitedPage[i]==0:
                writer.addPage(object.getPage(i))
                VisitedPage[i] = 1

    #Save pdf file under name chosen by user
    with open(os.path.join(returnpath,name + ".pdf"), "wb") as f:
        writer.write(f)
