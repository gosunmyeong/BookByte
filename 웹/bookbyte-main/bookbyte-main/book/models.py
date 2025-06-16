from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookInfo(models.Model):
    title = models.CharField(max_length=100, null=False) #책제목
    isbn = models.CharField(max_length=20, null=False) #국제표준도서번호(13자리)
    cover_image = models.CharField(max_length=2000, null=True) #책표지
    genre = models.CharField(max_length=20, null=True) #장르
    page = models.IntegerField(null=True) #쪽수
    bookbinding_method = models.CharField(max_length=10, null=True) #제본방식
    weight = models.FloatField(null=True) #무게
    size = models.CharField(max_length=30, null=True) #크기
    author = models.CharField(max_length=50, null=True) #지은이
    translator = models.CharField(max_length=50, null=True) #옮긴이
    publisher = models.CharField(max_length=30, null=True) #출판사
    book_explanation = models.TextField(null=True) #책소개

    def __str__(self):
        return self.isbn


class Review(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.CASCADE) #아이디_User
    book_id = models.ForeignKey(BookInfo, on_delete = models.CASCADE) #아이디_BookInfo
    title = models.CharField(max_length=100, null=True) #제목
    content = models.TextField(null=False) #내용
    grade = models.FloatField(null=True) #평점
    is_bookbyte = models.BooleanField(default=False, null=False) #bookbyte에서 생성여부

    def __str__(self):
        return self.title

class Favor(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.CASCADE) #아이디_User
    genre = models.CharField(max_length=30, null=True) # 선호하는 장르