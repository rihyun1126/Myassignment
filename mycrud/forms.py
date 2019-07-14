from django import forms
from .models import Blog

class NewBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']
        # 모델에 있는 모든 항목을 입력받고 싶은 경우에는
        # fields = '__all__' 이라고 작성
