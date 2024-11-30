from django import forms

class WineForm(forms.Form):
    alcohol = forms.FloatField(label='Alcohol')
    malic_acid = forms.FloatField(label='Malic Acid')
    ash = forms.FloatField(label='Ash')
    alcalinity_of_ash = forms.FloatField(label='Alcalinity of Ash')
    magnesium = forms.FloatField(label='Magnesium')
    total_phenols = forms.FloatField(label='Total Phenols')
    flavanoids = forms.FloatField(label='Flavanoids')
    nonflavanoid_phenols = forms.FloatField(label='Nonflavanoid Phenols')
    proanthocyanins = forms.FloatField(label='Proanthocyanins')
    color_intensity = forms.FloatField(label='Color Intensity')
    hue = forms.FloatField(label='Hue')
    od280_od315_of_diluted_wines = forms.FloatField(label='OD280/OD315 of Diluted Wines')
    proline = forms.FloatField(label='Proline')
