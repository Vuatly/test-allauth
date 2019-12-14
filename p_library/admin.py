from django.contrib import admin
from p_library.models import Book, Author, Redaction, Friend


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Redaction)
class RedactionAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass