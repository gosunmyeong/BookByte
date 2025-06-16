from django.contrib import admin
from book.models import BookInfo
from book.models import Review
from book.models import Favor

# Register your models here.
@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(Favor)
class ReviewAdmin(admin.ModelAdmin):
    pass