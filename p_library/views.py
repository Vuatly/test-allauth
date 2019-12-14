from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from p_library.models import Book, Redaction, Author, Friend
from p_library.forms import AuthorForm, BookForm, FriendForm
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.utils import timezone


class RedactionDetailView(DetailView):

    model = Redaction
    template_name = "redaction_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context



class AuthorEdit(CreateView):  
    model = Author  
    form_class = AuthorForm  
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'  
  
  
class AuthorList(ListView):  
    model = Author  
    template_name = 'author_list.html'

#Работет, но в этой версии выглядит не очень. Если хотите проверить то перейдите по URL,
# который записан в p_library/urls.py
class FriendEdit(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'friend_edit.html'


def start(request):
    template = loader.get_template('base.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))


def redaction_info(request):
    template = loader.get_template('redaction.html')
    books = Book.objects.all()
    redactions = Redaction.objects.all()
    redactions_dict = dict()
    for redaction in redactions:
        for book in books:
            if book.redaction == redaction:
                if book.redaction not in redactions_dict:
                    redactions_dict[book.redaction] = list()
                    redactions_dict[book.redaction].append(book)
                else:
                    redactions_dict[book.redaction].append(book)
    redaction_data = {
        "redactions": redactions_dict,
    }
    return HttpResponse(template.render(redaction_data, request))

def library_info(request):
    template = loader.get_template('library.html')
    books = Book.objects.all()
    biblio_data = {
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))


def friend_info(request):
    template = loader.get_template('friends.html')
    friends = Friend.objects.all()
    friends_dict = dict()
    for friend in friends:
        for book in friend.borrowed_books.all():
            if friend not in friends_dict:
                friends_dict[friend] = list()
                friends_dict[friend].append(book)
            else:
                friends_dict[friend].append(book)
    friends_data = {
        "friends": friends_dict,
    }
    return HttpResponse(template.render(friends_data, request))





