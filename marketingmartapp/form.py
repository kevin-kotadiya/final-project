from django import forms
from .models import user,noted,feedback


class signupform(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'

class updateprofile(forms.ModelForm):
    class Meta:
        model = user
        fields = ['fname','lname','uname','city','state','password']

class noteform(forms.ModelForm):
    class Meta:
        model = noted
        fields = '__all__'

class feedbackform(forms.ModelForm):
    class Meta:
        model = feedback
        fields = '__all__'