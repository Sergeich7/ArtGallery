from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(
        required=False, max_length=20, label='',
        widget=forms.TextInput(attrs={"class": "n-action-search"})
    )
