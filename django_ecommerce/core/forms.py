from django import forms

class AddProductToCartForm(forms.Form):
    quantity = forms.ChoiceField(initial=1, choices=[(num, num) for num in xrange(1,11)])
    sku = forms.CharField(widget=forms.HiddenInput)
