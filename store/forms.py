# forms.py
from django import forms

from category.models import Category
from store.models import Products
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']  # Only include fields that the user needs to input

    def __init__(self, *args, **kwargs):
        product = kwargs.pop('product', None)
        super(OrderForm, self).__init__(*args, **kwargs)

        # Ensure that product is set correctly
        if product:
            self.fields['product'] = forms.ModelChoiceField(
                queryset=Products.objects.filter(id=product.id),
                initial=product,
                widget=forms.HiddenInput()
            )
        else:
            # If no product is provided, the product field should be required
            self.fields['product'] = forms.ModelChoiceField(
                queryset=Products.objects.all(),
                required=True
            )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'description', 'image', 'stock', 'category']  # Include the category field

        # Optional: Customize the widgets for a better user experience
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
