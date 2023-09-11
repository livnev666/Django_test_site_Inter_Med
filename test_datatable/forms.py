from django import forms


class ProfileSearchForm(forms.Form):
    name = forms.CharField(label='Поле поиска', required=False)


