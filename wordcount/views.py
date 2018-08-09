#import request from
from django.http  import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    str = request.GET['fulltext']
    wordlist = str.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':str,'count':len(wordlist),'sortedwords':sortedwords})
