# -*- coding: utf-8 -*->
from classytags import models
from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView

# Create your views here.


def about(request):
    text_block_0 = ''
    return render(request, 'public_fulfillment/public_fulfillment_root.html', {
        'text_block_0': text_block_0,
        'rtl': 'dir="rtl"'
    })

    
    


def labs_root(request):
    
    text_block_0 = """
כמו סגרדה פמיליה בברצלונה, הבניה של האתר אף פעם לא תסתיים.
אז כרגע הגיעו לעבודה באתר שלשה פועלים ומיישרים את השטח לפני שיגיע האיש של הקידוחים.
ו.... בחפירה הראשונה כבר נתקלנו באוצר. 
פיתחנו גירסה אינטרנטית למשחק שעוזר לכל אחד לקדם כל יוזמה או לפתור כל בעיה בעזרתה של קבוצה. 
אז אנחנו מחברים את הסקופ, קולבות,פרובים, לוג'יק אנלייזר, מבחנות, קונדסטורים, (פה אפשר להוסיף כל מיני מילים מפוצצות ומיסתוריות ). מחברים גם צב"ד עוגיות. ולמה? כי אנחנו מתים מסקרנות לדעת אם ואיך כל אחד יעזר בכלי וכדי למדוד איך להמשיך בכיוון הכי נכון. 
אז בכניסתך למעבדה דע/י שכל הפעילות נמדדת ונרשמת !
אף אחד לא יודע איך זה יתפתח. אבל ככה (אנחנו מאמינים) כולנו ביחד נמשיך לבנות ולבנות ולבנות....

"""
    return render(request, 'public_fulfillment/labs_root.html', {
        'text_block_0': text_block_0,
        'rtl': 'dir="rtl"'
    })



class CreateUserView(CreateView):
    model = User
    template_name = 'public_fulfillment/user_form.html'
    

class AddTUserForm(forms.Form):
    user_name  = forms.CharField(max_length = 200)
    password1  = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2  = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    first_name = forms.CharField(max_length = 200)
    last_name  = forms.CharField(max_length = 200)
    email      = forms.EmailField()      


def sign_up(request):
    if request.user.is_authenticated():
        return render(request, 'coplay/message.html', 
                      {  'message'      :  'Already logged in',
                       'rtl': 'dir="rtl"'})

    if request.method == 'POST': # If the form has been submitted...
        form = AddTUserForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data# Process the data in form.cleaned_data
            if form.cleaned_data['password1'] != form.cleaned_data['password2']:
                return render(request, 'coplay/message.html', 
                      {  'message'      :  'Passwords not match',
                       'rtl': 'dir="rtl"'})
            user = User(username =  form.cleaned_data['user_name'] ,
                            first_name = form.cleaned_data['first_name'],
                            last_name =  form.cleaned_data['last_name'],
                            email     =  form.cleaned_data['email'])
            
            user.set_password(form.cleaned_data['password1'])
            
            user.save()
            return HttpResponseRedirect(reverse('home')) # Redirect after POST
        else:
            return render(request, 'coplay/message.html', 
                      {  'message'      :  'Please try again',
                       'rtl': 'dir="rtl"'})
            
        
    else:
        form = AddTUserForm() # An unbound form


    return render(request, 'public_fulfillment/new_user.html', {
        'form': form,
        'rtl': 'dir="rtl"'
    })
    
