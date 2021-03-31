from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView, UpdateView, DeleteView
from .forms import Userform,InputForm


# from django.shortcuts import render
# from .forms import InputForm
# Create your views here.
class ContactUsView(View):

    # @transaction.atomic
    def get(self, request):
        form = Userform
        print("getttttttttt")
        print("getttttttttt")
        # form = Projectform
        return render(request, 'it_contact.html',{'form':form})

    # @transaction.atomic
    def post(self, request, **kwargs):
        # form = Userform
        form = Userform(request.POST)
        print("fffffff")
        print("email_id",request.POST.get('email_id'))
        print(request.POST)
        return render(request, 'it_contact.html')
        # pass
    
    
# @transaction.atomic
# def contact(request):
#     return render(request,'it_contact.html')

def term_condition(request):
    return render(request,'it_term_condition.html')

def privacy_policy(request):
    return render(request,'it_privacy_policy.html')

def news(request):
    return render(request,'it_news.html')

# def news(request):
#     return render(request,'it_news.html')


#def showdata(HttpRequest):
 #   web = HttpRequest.GET.get(

# Create your views here.
def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "it_contact.html", context)
