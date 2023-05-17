from django import forms
from .models import Theme,Message

class Form_theme(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ["Newchat"]

class Form_message(forms.ModelForm):
    #message = forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 750px; height: 30px; overflow-y: scroll;'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 750px;'}))

    class Meta:
        model = Message
        fields = ["message"]
