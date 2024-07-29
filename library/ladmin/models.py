from django.db import models
from cust.models import customer
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    book_id = models.CharField(max_length=100, unique=True, null=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class BookPurchase(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True)
    purchase_date = models.DateField(auto_now_add=True)
    supplier_name = models.CharField(max_length=100)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Purchase of {self.book.title} on {self.purchase_date}"

class Borrowing(models.Model):
    user = models.ForeignKey(customer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    returned_date = models.DateTimeField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Only decrease quantity when creating a new borrowing
            if self.book.quantity > 0:
                self.book.quantity -= 1
                self.book.save()
            else:
                raise ValueError('Book quantity cannot be less than 0.')
        elif self.returned_date and not Borrowing.objects.get(pk=self.pk).returned_date:
            self.book.quantity += 1
            self.book.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} borrowed {self.book}"
