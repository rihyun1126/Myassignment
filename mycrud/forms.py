from django import forms
from .models import Blog, Comment

class NewBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']
        # 모델에 있는 모든 항목을 입력받고 싶은 경우에는
        # fields = '__all__' 이라고 작성
class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
    
        fields = ['comment_user', 'comment_textfield']
        widgets = {
            'comment_textfield' : forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40})
        }