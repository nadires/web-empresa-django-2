from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):

    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            mail = request.POST.get('mail','')
            content = request.POST.get('content','')
            #enviamos el correro y redireccionamos
            email = EmailMessage(
                "la cafie no se que cosa: nuevo mensaje de contacto",
                "De {} <{}> \n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrop.io",
                ["nadiresfirts@gmail.com"],
                reply_to = [email]
            )
            try:
                email.send()
                # todo ha ido bien
                return redirect(reverse('contact'),"?ok")
            except:
                #algo salio mal
                return redirect(reverse('contact'),"?fail") 

            return redirect(reverse('contact')+ "?ok")
    return render(request,"contact/contact.html",{'form': contact_form})

