from django.shortcuts import render
from pages.form import ContactForm

def home_pages_view(request):
    if request.method == "GET":
     return render(request,template_name='index_new.html')
    
    elif request.method == "POST":
       form =  ContactForm(request.POST)
       if form.is_valid():
          form.save()
       else:
          pass
       
    return render(request,template_name='index_new.html')
       
