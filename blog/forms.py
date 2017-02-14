from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='姓名')
    email = forms.EmailField(required=False,label='邮箱')
    content = forms.CharField(widget=forms.Textarea,label='评论内容')