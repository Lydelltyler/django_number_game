from django.shortcuts import render, HttpResponse, redirect
import random


def index(request):
    request.session['random'] = (random.randint(1, 100))
    return render(request, "index.html")


def check(request):

    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 0

    if request.session['counter'] == 6:
        return redirect('/los e')

    print("show me the SESSSION >>>>>>>>>>>>>>>>")
    print(request.session['counter'])

    answer = request.session['random']
    guess = request.POST['number']

    request.session['guess'] = request.POST['number']

    print(f"THEIR GUESS => {guess}")
    print(f"THE ANSWER => {answer}")

    if answer == int(guess):
        return redirect('/correct')
    elif answer < int(guess):
        return redirect('/to_high')
    elif answer > int(guess):
        return redirect('/to_low')


def low(request):
    return render(request, "low.html")


def high(request):
    return render(request, "high.html")


def correct(request):
    context = {
        'correct_num': request.session['guess']
    }
    return render(request, "correct.html", context)


def lose(request):
    return render(request, "lost.html")


def end(request):
    del request.session['counter']
    return redirect('/')


