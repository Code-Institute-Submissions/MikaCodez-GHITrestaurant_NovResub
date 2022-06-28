from .models import Comment
from django import forms
from .models import Contact


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.Form):
    my_date_field = forms.DateField(widget=DateInput)



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'purpose', 'message']
        

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'input', 'placeholder' : 'Your Name'}),
            'email' : forms.EmailInput(attrs={'class': 'input', 'placeholder' : 'you@email.com'}),
            'message': forms.Textarea(attrs={'class': 'textarea', 'rows': 10, 'placeholder' : 'Your message...'}),
        }