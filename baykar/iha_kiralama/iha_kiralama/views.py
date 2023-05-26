from django.shortcuts import render,redirect
from iha_kiralama.models import IHA
from iha_kiralama.models import IHAUSER
from django.contrib import messages
from iha_kiralama.forms import IhaForms

from django.contrib.auth import authenticate, login

from .models import MyUser


def showIha(request):
    showall=IHA.objects.all()
    return render(request, 'index.html', {"data": showall})

def insertIha(request):
    if request.method =="POST":
        if request.POST.get('marka') and request.POST.get('model') and request.POST.get('agirlik') and request.POST.get('kategori') :
            saveRecord = IHA()
            saveRecord.marka = request.POST.get('marka') 
            saveRecord.model = request.POST.get('model') 
            saveRecord.agirlik = request.POST.get('agirlik') 
            saveRecord.kategori = request.POST.get('kategori') 
            saveRecord.save()
            messages.success(request,'İha ' + saveRecord.model + 'Kaydedildi...')
            return render(request, 'insert.html')
    else:
            return render(request, 'insert.html')

def editIha(request,id):
    editIhaObj=IHA.objects.get(id=id)
    return render(request, 'edit.html', {"IHA": editIhaObj})

def updateIha(request,id):
    updateIha=IHA.objects.get(id=id)
    form=IhaForms(request.POST, instance=updateIha)
    if form.is_valid():
        form.save()
        messages.success(request,'Kayıt Güncellendi...')
        return render(request, 'edit.html',{"IHA":updateIha})
    
def deleteIha(request,id):
    deleteIhaObj=IHA.objects.get(id=id)
    deleteIhaObj.delete()
    showIha=IHA.objects.all()
    return render(request, 'index.html', {"data": deleteIha})

def registerIha(request):
    if request.method == 'POST':
        isim = request.POST.get('isim')
        soyisim = request.POST.get('soyisim')
        mail = request.POST.get('mail')
        telefon = request.POST.get('telefon')
        sifre = request.POST.get('sifre')
        kullanici_adi = request.POST.get('kullanici_adi')

        user = MyUser.objects.create_user(
            username=kullanici_adi,
            password=sifre,
            isim=isim,
            soyisim=soyisim,
            mail=mail,
            telefon=telefon
        )

        messages.success(request, 'Kullanıcı kaydı başarıyla oluşturuldu.')
        return redirect('loginView')  # Kayıt işlemi tamamlandıktan sonra yönlendirilecek sayfanın adını ayarlayın

    return render(request, 'register.html')   


def loginView(request):
    if request.method == 'POST':
        kullanici_adi = request.POST.get('kullanici_adi')
        sifre = request.POST.get('sifre')
        user = authenticate(request, username=kullanici_adi, password=sifre)

        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş başarılı!')
            return redirect('showIha')  # Giriş başarılıysa yönlendirilecek sayfanın adını ayarlayın
        else:
            messages.error(request, 'Geçersiz kullanıcı adı veya şifre!')

    return render(request, 'login.html')