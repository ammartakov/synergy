from django import forms
from .models import UserName

class UserNameForm(forms.ModelForm):
    class Meta:
        model = UserName
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите ваше имя...',
                'id': 'name-input'
            })
        }
        labels = {
            'name': 'Ваше имя'
        }
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or name.strip() == '':
            raise forms.ValidationError('Пожалуйста, введите ваше имя!')
        if len(name.strip()) < 2:
            raise forms.ValidationError('Имя должно содержать минимум 2 символа!')
        return name.strip()