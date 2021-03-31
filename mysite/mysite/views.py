from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView, UpdateView, DeleteView
# from .forms import Userform

def homehtml(request):
    return render(request,'it_home.html')

def index(request):
    return render(request,'index.html')
	
def make_appointment(request):
    return render(request,'make_appointment.html')

def home_dark(request):
    return render(request,'it_home_dark.html')

def about(request):
    return render(request,'it_about.html')

def service(request):
    return render(request,'it_service.html')

def service_list(request):
    return render(request,'it_service_list.html')

def service_detail(request):
    return render(request,'it_service_detail.html')

def blog(request):
    return render(request,'it_blog.html')

def blog_grid(request):
    return render(request,'it_blog_grid.html')

def blog_detail(request):
    return render(request,'it_blog_detail.html')

def career(request):
    return render(request,'it_career.html')

def price(request):
    return render(request,'it_price.html')

def faq(request):
    return render(request,'it_faq.html')

def shop_detail(request):
    return render(request,'it_shop_detail.html')

# class ContactUsView(View):

#     # @transaction.atomic
#     def get(self, request):
#         form = Userform
#         print("getttttttttt")
#         print("getttttttttt")
#         # form = Projectform
#         return render(request, 'it_contact.html',{'form':form})

#     # @transaction.atomic
#     def post(self, request, **kwargs):
#         # form = Userform
#         form = Userform(request.POST)
#         print("fffffff")
#         print("email_id",request.POST.get('email_id'))
#         print(request.POST)
#         return render(request, 'it_contact.html')
#         pass
    
    
# # @transaction.atomic
# # def contact(request):
# #     return render(request,'it_contact.html')

def term_condition(request):
    return render(request,'it_term_condition.html')

def privacy_policy(request):
    return render(request,'it_privacy_policy.html')

def news(request):
    return render(request,'it_news.html')

# def news(request):
#     return render(request,'it_news.html')


# #def showdata(HttpRequest):
#  #   web = HttpRequest.GET.get(

