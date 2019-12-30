from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_email(self, *args, **kwargs):

        email = self.cleaned_data.get('email')
        if not email.endswith('.com'):
            raise forms.ValidationError("Please Use a COM email!")

        print(email)
        return email  # email cleaned
