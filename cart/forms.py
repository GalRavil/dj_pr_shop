from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        cchoice=PRODUCT_QUANTITY_CHOICES,
        coerce=int)  # to convert the input into an integer
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
