from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from . import forms

def index(request):
        
    form = forms.ContactForm()
    
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        
        if form.is_valid():
            
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            full_name = first_name + " " + last_name 
            
            send_mail(subject,"Name: " + full_name + "\n\nEmail: " + email + "\n\nSubject: " + subject + "\n\nMessage: " + message, email, ['mact792@gmail.com'],)
            
            print('email sent')
            
            messages.success(request, "Your message has been sent!")
            
            return redirect("/")
            
    else:
        form = forms.ContactForm()
    
    return render(request, 'index.html', context={
        "form":form,
    })
    
def about(request):
    
    return render(request, 'about.html', context={

    })
    
def faq(request):
    
    return render(request, "FAQ.html", context={
        
    })
    
def become(request):
    
    form = forms.becomeForm()
    
    if request.method == "POST":
        form = forms.becomeForm(request.POST)
        
        if form.is_valid():
            
            subject = "Enrollment Form"
            
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            age = form.cleaned_data['age']
            laptop = form.cleaned_data['laptop']
            agreement = str(form.cleaned_data['agreement'])
            
            full_name = first_name + " " + last_name 
            
            if agreement == "True":
                agreement = "Yes. I, " + full_name + ", agree to be an Independent Contractor and not an Employee."
                
            if age == "Yes":
                age = "Yes. I, " + full_name + ", certify that I am 18 years old."
            else:
                age = "No. I, " + full_name + ", certify that I am not 18 years old."
                
            if laptop == "Yes":
                laptop = "Yes. I have a laptop."
            else:
                laptop = "No. I do not have a laptop."
            
            message = full_name + "\nEmail: " + email + "\nPhone Number: " + phone +  "\nLaptop: " + laptop + "\nAge: " + age + "\nAgreement: " + agreement
            
            send_mail(subject, message, email, ['mact792@gmail.com'],)
            
            print('email sent')
            
            messages.success(request, "Your Enrollment Form has been submitted!", extra_tags="become")
            
            return redirect(".")
            
    else:
        form = forms.becomeForm()
    
    return render(request, "become.html", context={
        "form":form,
    })
