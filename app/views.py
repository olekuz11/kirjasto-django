from django.shortcuts import render, redirect
from .models import Kirja, Kirjailija, Laina
from django.contrib.auth import authenticate, login, logout

def kirjalistview(request):
    kirjat = Kirja.objects.all()
    kirjailijat = Kirjailija.objects.all()
    context = {'kirjat': kirjat, 'kirjailijat': kirjailijat}
    return render(request, 'kirjalist.html', context)

def addkirja(request):
    if not request.user.is_authenticated:
        return redirect(loginview)
    nimi = request.POST['nimi']
    genre = request.POST['genre']
    julkaisuvuosi = request.POST['julkaisuvuosi']
    sivut = request.POST['sivut']
    kirjailija_id = request.POST['kirjailija']

    Kirja(
        nimi=nimi,
        genre=genre,
        julkaisuvuosi=julkaisuvuosi,
        sivut=sivut,
        kirjailija=Kirjailija.objects.get(id=kirjailija_id)
    ).save()

    return redirect(kirjalistview)

def deletekirja(request, id):
    if not request.user.is_authenticated:
        return redirect(loginview)
    Kirja.objects.get(id=id).delete()
    return redirect(kirjalistview)

def loginview(request):
    return render(request, 'loginpage.html')

def login_action(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return redirect(kirjalistview)
    else:
        return render(request, 'loginpage.html', {'error': 'Väärä käyttäjätunnus tai salasana'})

def logout_action(request):
    logout(request)
    return redirect(loginview)

def edit_kirja_get(request, id):
    if not request.user.is_authenticated:
        return redirect(loginview)
    kirja = Kirja.objects.get(id=id)
    kirjailijat = Kirjailija.objects.all()
    context = {'kirja': kirja, 'kirjailijat': kirjailijat}
    return render(request, 'edit_kirja.html', context)

def edit_kirja_post(request, id):
    if not request.user.is_authenticated:
        return redirect(loginview)
    kirja = Kirja.objects.get(id=id)
    kirja.nimi = request.POST['nimi']
    kirja.genre = request.POST['genre']
    kirja.julkaisuvuosi = request.POST['julkaisuvuosi']
    kirja.sivut = request.POST['sivut']
    kirja.kirjailija = Kirjailija.objects.get(id=request.POST['kirjailija'])
    kirja.save()
    return redirect(kirjalistview)

def lainalistview(request):
    lainat = Laina.objects.all()
    kirjat = Kirja.objects.all()
    context = {'lainat': lainat, 'kirjat': kirjat}
    return render(request, 'lainalist.html', context)

def addlaina(request):
    if not request.user.is_authenticated:
        return redirect(loginview)
    kirja_id = request.POST['kirja']
    lainaaja = request.POST['lainaaja']
    Laina(
        kirja=Kirja.objects.get(id=kirja_id),
        lainaaja=lainaaja
    ).save()
    return redirect(lainalistview)

def update_laina_status(request, id):
    if not request.user.is_authenticated:
        return redirect(loginview)
    laina = Laina.objects.get(id=id)
    laina.status = request.POST['status']
    laina.save()
    return redirect(lainalistview)

def etusivu(request):
    return render(request, 'etusivu.html')