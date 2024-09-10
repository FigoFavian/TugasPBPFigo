from django.shortcuts import render

def ingfo(request):
    context = {
        'nama': 'Figo Favian Ragazo',  # nama
        'kelas': 'PBP F'  # kelas 
    }
    return render(request, 'main.html', context)