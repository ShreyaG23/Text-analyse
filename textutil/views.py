# Ihave Created This File -- Shreya Gupta
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def analyse(request):
    #  check box
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', "off")
    spaceremover = request.POST.get('spaceremover', "off")
    charcounter = request.POST.get('charcounter', "off")
    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        djtext = analysed

        params = {'purpose':'removed punctuation', 'analysed_text': analysed}
        #return render(request, 'analyse.html', params)
    if fullcaps == "on":
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()
        djtext = analysed
        params = {'purpose':'Capital form ', 'analysed_text': analysed}
        #return render(request, 'analyse.html', params)
    if newlineremover == "on":
        analysed = ""
        for char in djtext:
            if char != '\n'and char != '\r':
                analysed = analysed + char
        djtext = analysed
        params = {'purpose':'new line removed ', 'analysed_text': analysed}
        return render(request, 'analyse.html', params)
    if spaceremover == "on":
        analysed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analysed = analysed + char
        djtext = analysed
        params = {'purpose':' space removed form ', 'analysed_text': analysed}
        #return render(request, 'analyse.html', params)
    if charcounter == "on":
        analysed = len(djtext)
        params = {'purpose':' char counted ', 'analysed_text': analysed}
    return render(request, 'analyse.html', params)












