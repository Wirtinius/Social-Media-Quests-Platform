from django.shortcuts import render


def game_1(request):
    return render(request, 'Games/index.html')
