from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


def calc(request):
    c=""
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')

            if opr =="+":
                c=n1+n2

            elif opr=="-":
                c=n1-n2

            elif opr=="*":
                c=n1*n2

            elif opr=="/":
                c=n1/n2

    except:
        c="invlid input"
    print(c)

    return render(request, "calc.html",{'c':c})