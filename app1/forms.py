from django import forms


class ALogin(forms.Form):
    username = forms.CharField(error_messages={'request':"sdf",'invalid':'wer'})
    email = forms.EmailField(required=True)
    ip = forms.GenericIPAddressField(error_messages={'request':"woaini",'invalid':'nicuole'})

