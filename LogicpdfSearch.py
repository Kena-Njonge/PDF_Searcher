# import packages
import PyPDF2
import re
import os.path

def textSearch(target_path,word_list,name,return_path):
    x = len(target_path)
    #differentiation between Target path with or without quotation marks
    if target_path[0] == '"' or target_path[0]== "'" : 
        object = PyPDF2.PdfFileReader(r"{}".format(target_path[1:x-1]))
    else :
        object = PyPDF2.PdfFileReader(r"{}".format(target_path))
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
        for x in word_list:
            #Two regular expression searches for possible types of quoations
            ResSearch = re.search(x.replace("'",""), Text)
            ResSearch2 = re.search(x.replace('"',''), Text)
            print(x)
            #Add pages with target text and avoid duplicate additions
            if (ResSearch != None or ResSearch2 != None)  and VisitedPage[i]==0:
                writer.addPage(object.getPage(i))
                VisitedPage[i] = 1
    #Remove quotation marks from name
    name = name.replace("'","")
    name = name.replace('"','')
    #differentiation between Return path with or without quotation marks
    if return_path[0] == '"' or return_path[0]== "'" : 
        return_path= return_path.replace("'",'')
        return_path= return_path.replace('"','')
    with open(os.path.join(return_path,name + ".pdf"), "wb") as f:
            writer.write(f)
