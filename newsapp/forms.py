from django import forms

class NewsFilterForm(forms.Form):
    COUNTRIES = [
        ('us', 'United States'),
        ('gb', 'United Kingdom'),
        ('ca', 'Canada'),
        ('eg', 'Egypt'),
        ('ae', 'United Arab Emirates'),
        ('sa', 'Saudi Arabia'),
    ]

    CATEGORIES = [
        ('general', 'General'),
        ('business', 'Business'),
        ('health', 'Health'),
        ('technology', 'Technology'),
        ('science', 'Science'),
        ('sports', 'Sports'),
    ]

    country = forms.ChoiceField(
        choices=COUNTRIES,
        label='Select Country',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    category = forms.ChoiceField(
        choices=CATEGORIES,
        label='Select Category',
        widget=forms.Select(attrs={'class': 'form-select'})
    )