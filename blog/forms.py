from django import forms
from .models import Post
forms.Form
forms.ModelForm
class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea,label='Content')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(max_length=11,label='Phone')

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError('Phone must be digit only!')
        if len(phone) != 11:
            raise forms.ValidationError('Phone must include 11 digits only!')
        if not phone.startswith('09'):
            raise forms.ValidationError('Phone must start by "09" only!')
        return phone

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']



















''' 

<div class="comment">
     <span><i class="fa fa-comments"></i>نظری برای این مطلب بنویسید</span>
     <form action="{% url 'blog:post_comment' post.slug %}" method="post">
         <div class="form-group col-md-6">
             {% csrf_token %}
             {{ form.as_p }}
         </div>
         <div class="form-group col-md-12">
             <button class="btn btn-default" type="submit">ارسال نظر</button>
         </div>
     </form>
 </div>
'''




'''
{% extends 'parent/base.html' %}
{% load static %}
{% block title %} ساخت پست {% endblock %}
{% block content %}
<div class="comment">

{% if post %}
    <h1> پست شما با موفقیت ثبت شد</h1>
    <h1>لطفا منتظر تایید ادمین باشید</h1>
    <a href="{% url 'blog:profile' %}" >  بازگشت به   پروفایل  </a>
{% else %}
     <span><i class="fa fa-comments"></i>              برای ایجاد پست فرم زیر را پر کنید  </span>
     <form method="post">
         {% csrf_token %}
         <div class="form-group col-md-6">
             {{ form.title.label }}
             <input class="form-control" type="text" name="title" placeholder="عنوان پست را وارد کنید"
                    value="{% if form.title.value %}{{ form.title.value }}{% endif %}">
             {{ form.title.errors}}
         </div>
         <div class="form-group col-md-12">
             {{ form.content.label }}
             <textarea class="form-control" name="content" placeholder="متن پست"
                       rows="7" >{% if form.content.value %}{{ form.content.value }}{% endif %}</textarea>
             {{ form.content.errors }}
         </div>
         <div class="form-group col-md-12">
             <button class="btn btn-default" type="submit">ارسال post</button>
         </div>
     </form>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
{% endif %}
 </div>
{% endblock %}

'''










'''{% load static %}
<link href="{% static 'css/bootstrap.css' %}" rel="stylesheet" type="text/css">
<link href="{% static 'css/font-awesome.css' %}" rel="stylesheet" type="text/css">
<link href="{% static 'css/style.css' %}" rel="stylesheet" type="text/css">
<div class="comment">
     <span><i class="fa fa-comments"></i>نظری برای این مطلب بنویسید</span>
     <form action="{% url 'blog:post_comment' post.slug %}" method="post">
         {% csrf_token %}
         <div class="form-group col-md-6">
             {{ form.phone.label }}
             <input class="form-control" type="text" name="phone" placeholder="شماره تماس خود  را وارد کنید"
                    value="{% if form.phone.value %}{{ form.phone.value }}{% endif %}" >
             {{ form.phone.errors}}
         </div>
         <div class="form-group col-md-6">
             {{ form.email.label }}
             <input class="form-control" type="email" name="email"
                    placeholder="ایمیل را واردکنید" value="{% if form.email.value %}{{ form.email.value }}{% endif %}" >
             {{ form.email.errors }}
         </div>
         <div class="form-group col-md-12">
             {{ form.body.label }}
             <textarea class="form-control" name="body" placeholder="متن نظر"
                       rows="7">{% if form.body.value %}{{ form.body.value }}{% endif %} </textarea>
             {{ form.body.errors }}
         </div>
         <div class="form-group col-md-12">
             <button class="btn btn-default" type="submit">ارسال نظر</button>
         </div>
     </form>
 </div>'''
