from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator

def books_view(request):
    template = "books/books_list.html"
    books_list = Book.objects.all()
    context = {"books": books_list}
    return render(request, template, context)


def book_view(request, pub_date):
    template = "books/book.html"
    pag = []
    books = Book.objects.all().order_by("pub_date")

    for book in books.values():
        pag.append(str(book["pub_date"]))

    paginat = Paginator(pag, 1)
    page = paginat.get_page(pag.index(pub_date) + 1)
    page_next = paginat.get_page(pag.index(pub_date) + 2).object_list
    page_previous = paginat.get_page(pag.index(pub_date)).object_list
    context = {
        "page": page,
        "book": Book.objects.get(pub_date=pub_date),
        "page_next": page_next[0],
        "page_previous": page_previous[0],
    }
    return render(request, template, context)
