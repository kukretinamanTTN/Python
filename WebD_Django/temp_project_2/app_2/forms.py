from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    gender = forms.ChoiceField(
        choices=[("Male", "Male"), ("Female", "Female")],
        widget=forms.RadioSelect  # Renders as radio buttons
    )