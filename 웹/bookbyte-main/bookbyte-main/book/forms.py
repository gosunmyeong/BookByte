from django import forms

# 리뷰폼
class ReviewForm(forms.Form):
    title = forms.CharField(min_length=1, label="제목")
    content = forms.CharField(widget=forms.Textarea, label="내용")

    grade_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    grade = forms.ChoiceField(
        label="평점",
        choices=grade_choices,
        widget=forms.RadioSelect,
        required=False, 
    )