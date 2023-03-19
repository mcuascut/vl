from django import forms 

class ContactForm(forms.Form):
    
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message= forms.CharField(widget=forms.Textarea())
    
class becomeForm(forms.Form):
    
    answers = [
        
               ("yes", "Yes"),
               ("no", "No"),
               
               ]
    
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=25, required=False, label="Phone: (###) ###-####", widget=forms.TextInput
                            (attrs={"type":"tel",
                                    }))
    age = forms.ChoiceField(choices=answers, required=True, label="Are you at least 18 years old?")
    laptop = forms.ChoiceField(choices=answers, required=True, label="Do you have a laptop/desktop?")
    agreement = forms.BooleanField(required=True, label="I understand that I would be an Independent Contractor and not an Employee.", widget=forms.CheckboxInput())
    
    
    