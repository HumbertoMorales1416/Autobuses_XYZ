from django.shortcuts import render

def catalog_home(request):
  return render(request, 'catalog_home.html', {})