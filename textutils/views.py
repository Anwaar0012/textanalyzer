# i have made this file myself anwaar
# for avoiding 'str' object has no attribute 'get'
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'anwaar', 'place':"Doaba"}
    # return "Hello";
    # return HttpResponse("Home")
    # rendering template
    return render(request,'index.html',params)

def analyze(request):
    # Get the text from text area
    myText_of_text_Area = request.POST.get('text','default')
    
    # get checkbox/switches value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charactercounter = request.POST.get('charactercounter','off')
    
 
   
    
    # check/see which check box is on
    if removepunc == "on":
        punctuationList = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for char in myText_of_text_Area:
            if char not in punctuationList:
                analyzed =analyzed+char
                
        params= {'purpose':'Remove Punctuation','analyzed_text':analyzed}
        myText_of_text_Area= analyzed
    if fullcaps == "on":
        analyzed=""
        for char in myText_of_text_Area:
            analyzed = analyzed + char.upper()
            
        params= {'purpose':'Change to upper case','analyzed_text':analyzed}
        myText_of_text_Area= analyzed
    if extraspaceremover == "on":
        analyzed=""
        for index,char in enumerate(myText_of_text_Area):
            if not (myText_of_text_Area[index] ==" " and myText_of_text_Area[index+1]==" "):
                analyzed = analyzed + char
                
        params= {'purpose':'New line remover','analyzed_text':analyzed}
        myText_of_text_Area= analyzed
    if newlineremover == "on":
        analyzed=""
        for char in myText_of_text_Area:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
                
        params= {'purpose':'New line remover','analyzed_text':analyzed}
        myText_of_text_Area= analyzed
        
    if charactercounter == "on":
        analyzed=""
        character=""
        # text=""
        for index,char in enumerate(myText_of_text_Area):
            character =+index+1
            # text=text+char
        analyzed =f"The total no of characters are {character}"
        params= {'purpose':'Character Counter','analyzed_text':analyzed}
        analyzed=myText_of_text_Area
        
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and charactercounter!="on"):
        return HttpResponse("please select any operation and try again")
    
    return render(request,'analyze.html',params)
    



