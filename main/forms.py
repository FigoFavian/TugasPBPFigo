from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

    def clean_product(self):
        product = self.cleaned_data["name"]
        return strip_tags(product)
        
    def clean_feelings(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)