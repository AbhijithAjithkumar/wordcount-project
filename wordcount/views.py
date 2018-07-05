from django.http import HttpResponse
from django.shortcuts import render


def Hello(request):
     return render(request, 'home.html')
def count(request):
    text= request.GET['fulltext']
    wordlist= text.split()
    worddictionary={}
    for word in wordlist :
        if word in worddictionary :
            # incrementing the existing value
            worddictionary[word] +=1
        else:
            #adding the word to dictionary
            worddictionary[word] =1
    wordcountlist= worddictionary.items()
    sortlist=wordcountlist.sort()

    return render(request,'count.html',{'fulltext':text,'words':len(wordlist),'wordcount': sortlist})
def about(request):
    return render(request,'about.html')
