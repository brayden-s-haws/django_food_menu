from django import forms
from food.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']
        widgets = {
            'item_name': forms.TextInput(attrs={"placeholder":"e.g. Bacon Burger","required": True}),
            'item_desc': forms.TextInput(attrs={"placeholder":"e.g. This is a burger with bacon","required": True}),
            'item_price': forms.NumberInput(attrs={"placeholder":"e.g. $100","required": True}),
            'item_image': forms.URLInput(attrs={"placeholder":"https://sample.com", "required":False}),
        }
    def clean_item_price(self):
        price = self.cleaned_data['item_price']
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

    def clean(self):
        cleaned = super().clean()
        name = cleaned.get('item_name')
        desc = cleaned.get('item_desc')
        if name and desc and name.lower() in desc.lower():
            self.add_error('item_desc', "Description contain info beyond the name of the item.")
        return cleaned