from django import forms

class BasePhoneForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'phone' in self.fields:
            self.fields['phone'].initial = '+995'
