from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact_view(request):
    submitted_data = None
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            submitted_data = form.cleaned_data  
    else:
        form = ContactForm(initial={"name":"default", "email":"default@mail.com", "message":"default message"})
    return render(request, "app_2/contact.html", {"form": form, "submitted_data": submitted_data})