# I have created the file - Noman

from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse('''<h1>Hello Bhaiya</h1> <a href="https://fishcaring.com">Fish caring</a>''')

# def about(request):
#     return HttpResponse('Hello  About wale Bhaiya')

def index(request):
    params = {'name':'mastaan','place':'mumbai'}
    return render(request, 'index2.html')
def analyze(request):
    djtext=(request.POST.get('text','default'))
    removepunc=(request.POST.get('removepunc','off'))
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    print(removepunc)
    if removepunc =="on":
    # analyzed=djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for i in djtext:
            if i not in punctuations:
                analyzed=analyzed+i
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps == "on":
        analyzed= ""
        for i in djtext:
            analyzed= analyzed + i.upper()
        params = {'purpose':'Changed to Uppercadse', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)    

    if newlineremover == "on":
        analyzed= ""
        for i in djtext:
            if i !="\n" and i!="\r":
             analyzed= analyzed + i.upper()
        params = {'purpose':'removed new line', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params) 

    if extraspaceremover == "on":
        analyzed= ""
        for index,i in enumerate(djtext):
            if djtext[index] ==" " and djtext[index+1]==" ":
                pass
            else:
             analyzed= analyzed + i.upper()
        params = {'purpose':'removed new line', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)     
    return render (request, 'analyze.html', params) 
