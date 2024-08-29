from django import forms
from store.models import Products
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']  # Only include fields that the user needs to input

    def __init__(self, *args, **kwargs):
        product = kwargs.pop('product', None)
        super(OrderForm, self).__init__(*args, **kwargs)

        # If product is provided, set it in the form as a hidden field
        if product:
            self.fields['product'] = forms.ModelChoiceField(
                queryset=Products.objects.filter(id=product.id),
                initial=product,
                widget=forms.HiddenInput()
            )
        else:
            # If no product provided, the product field must be specified manually
            self.fields['product'] = forms.ModelChoiceField(queryset=Products.objects.all())


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'description', 'image', 'stock']  # Include the relevant fields

        # Optional: Customize the widgets for a better user experience
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
