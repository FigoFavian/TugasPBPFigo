from django.shortcuts import render

# Create your views here.
def app_info(request):
    # Replace 'YourName' and 'YourClass' with your actual name and class.
    context = {
        'app_name': 'Main',  # Application name
        'nama': 'Figo Favian Ragazo',  # nama
        'kelas': 'PBP F'  # kelas 
    }
    return render(request, 'main/main.html', context)