from django.shortcuts import render

def catalogo_home(request):
  return render(request, 'catalogo_home.html', {})