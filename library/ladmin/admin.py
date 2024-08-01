from django.contrib import admin
from ladmin.models import Category,Book, Borrowing, BookPurchase



@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display= ['name']


@admin.register(Book)
class bookAdmin(admin.ModelAdmin):
    list_display= ['book_id','title','author','category','quantity']
    
@admin.register(Borrowing)
class borrowingAdmin(admin.ModelAdmin):
    list_display= ['user','category','book','borrowed_date','due_date','returned_date']
    
@admin.register(BookPurchase)
class bookpurchaseAdmin(admin.ModelAdmin):
    list_display= ['book','quantity','purchase_date','supplier_name','cost_per_unit']
