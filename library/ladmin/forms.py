from django import forms
from ladmin.models import Category, Book, Borrowing, BookPurchase

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_id', 'title', 'author', 'category']

class BookPurchaseForm(forms.ModelForm):
    class Meta:
        model = BookPurchase
        fields = ['book', 'quantity', 'supplier_name', 'cost_per_unit']

"""class BorrowingForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
    borrowed_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    due_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    returned_date = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    

    class Meta:
        model = Borrowing
        fields = ['user', 'category', 'book', 'borrowed_date', 'due_date', 'returned_date']
        widgets = {
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }
"""
class BorrowingForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
    book = forms.ModelChoiceField(queryset=Book.objects.none(), required=True)
    borrowed_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=True)
    due_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=True)
    returned_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=False)

    class Meta:
        model = Borrowing
        fields = ['user', 'category', 'book', 'borrowed_date', 'due_date', 'returned_date']

    def __init__(self, *args, **kwargs):
        category_id = kwargs.pop('category_id', None)
        super(BorrowingForm, self).__init__(*args, **kwargs)
        
        if category_id:
            self.fields['book'].queryset = Book.objects.filter(category_id=category_id)
        else:
            self.fields['book'].queryset = Book.objects.none()

