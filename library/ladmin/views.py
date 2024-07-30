from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ladmin.models import Book, Category, Borrowing, BookPurchase
from ladmin.forms import CategoryForm, BookForm, BorrowingForm, BookPurchaseForm
from cust.models import customer
from django.db.models import Sum,F

def ahome(request):
    total_books = Book.objects.count()
    total_users = customer.objects.count()
    total_borrowings = Borrowing.objects.count()

    context = {
        'total_books': total_books,
        'total_users': total_users,
        'total_borrowings': total_borrowings,
    }
    return render(request, 'ladmin/ahome.html', context)

def admin_add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_categories')
    else:
        form = CategoryForm()
    return render(request, 'ladmin/aaddcategory.html', {'form': form})

def admin_add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book_id = form.cleaned_data['book_id']
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']

            book, created = Book.objects.get_or_create(
                book_id=book_id,
                defaults={'title': title, 'author': author, 'category': category}
            )

            if not created:
                book.title = title
                book.author = author
                book.category = category
                book.save()
                messages.success(request, 'Book information updated successfully.')
            else:
                messages.success(request, 'New book added successfully.')
                
            return redirect('admin_books')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = BookForm()
    return render(request, 'ladmin/aaddbook.html', {'form': form})

def admin_add_purchase(request):
    if request.method == 'POST':
        form = BookPurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save()
            
            # Update book quantity in stock
            book = purchase.book
            book.quantity += purchase.quantity
            book.save()
            
            messages.success(request, 'Book purchase recorded and stock updated successfully.')
            return redirect('admin_purchases')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = BookPurchaseForm()
    return render(request, 'ladmin/aaddpurchase.html', {'form': form})

def admin_categories(request, category_id=None):
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        books = Book.objects.filter(category=category)
    else:
        category = None
        books = Book.objects.all()
    categories = Category.objects.all()
    return render(request, 'ladmin/acategory.html', {'category': category, 'books': books, 'categories': categories})

def admin_books(request):
    categories = Category.objects.all()
    books = Book.objects.all()
    return render(request, 'ladmin/abooks.html', {'books': books, 'categories': categories})

def custuser(request):
    cust = customer.objects.all()
    return render(request, 'ladmin/acustuser.html', {'cust': cust})

def admin_borrowings(request):
    borrowings = Borrowing.objects.all()
    return render(request, 'ladmin/aborrowing.html', {'borrowings': borrowings})

"""def admin_add_borrowing(request):
    if request.method == 'POST':
        form = BorrowingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_borrowings')
    else:
        form = BorrowingForm()
    return render(request, 'ladmin/aaddborrow.html', {'form': form})"""
def admin_add_borrowing(request):
    category_id = request.GET.get('category', None)
    user_id = request.GET.get('user', None)
    
    user = None
    if user_id:
        user = get_object_or_404(customer, id=user_id)

    if request.method == 'POST':
        category_id = request.POST.get('category')
        form = BorrowingForm(request.POST, category_id=category_id)
        if form.is_valid():
            borrowing = form.save(commit=False)
            
           
            
            borrowing.save()
            return redirect('admin_borrowings')
    else:
        form = BorrowingForm(category_id=category_id)
    
    context = {
        'form': form,
        'category_id': category_id,
        'user': user,
    }
    return render(request, 'ladmin/aaddborrow.html', context)
def admin_edit_borrowing(request, borrowing_id):
    borrowing = get_object_or_404(Borrowing, id=borrowing_id)
    category_id = borrowing.category_id  # Get the category ID for initializing the form
    
    if request.method == 'POST':
        form = BorrowingForm(request.POST, instance=borrowing, category_id=category_id)
        if form.is_valid():
            form.save()
            return redirect('admin_borrowings')
        else:
            print("Form errors:", form.errors)  # Debug output for form errors
            print("POST data:", request.POST)  # Debug output for POST data
    else:
        form = BorrowingForm(instance=borrowing, category_id=category_id)
    
    context = {
        'form': form,
        'borrowing': borrowing,
    }
    return render(request, 'ladmin/aeditborrow.html', context)


    




from django.shortcuts import render
from django.db.models import Sum, F
from .models import BookPurchase, Book

def admin_purchases(request):
    search_query = request.GET.get('search', '')

    if search_query:
        purchases = BookPurchase.objects.filter(book__book_id__icontains=search_query)
    else:
        purchases = BookPurchase.objects.all()
    
    # Calculate the total quantity purchased and available quantity for each book
    total_purchases = BookPurchase.objects.values('book__book_id', 'book__title').annotate(
        total_quantity=Sum('quantity'),
        available_quantity=F('book__quantity')
    ).order_by('book__title')

    context = {
        'purchases': purchases,
        'total_purchases': total_purchases,
        'search_query': search_query,
    }
    
    return render(request, 'ladmin/apurchase.html', context)
