from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def machine_learning(request):
  return render(request,'Mechine_Learning/machine_learning.html'
  )


