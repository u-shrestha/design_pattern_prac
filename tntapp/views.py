from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import *
from .models import *
from .forms import *


import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from .tasks import new_order

import requests, logging, time



# Client Views


class ProductListView(ListView):
    template_name = "clienttemplates/packagelist.html"
    queryset = Product.objects.all().order_by('-id')
    context_object_name = "itemlist"
    paginate_by = 6



class ProductDetailView(DetailView):
    template_name = "clienttemplates/packagedetail.html"
    model = Product
    context_object_name = "item"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_form'] = OrderForm

        return context         
                    
            

class ProductOrderView(SuccessMessageMixin, CreateView):
    template_name = "clienttemplates/packagedetail.html"
    form_class = OrderForm
    success_message = "Thank you for ordering. Your order has been placed."

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        phone = form.cleaned_data["phone"]

        new_order.delay(name, phone)

        account_sid = "AC3674f215ceab484f4e49dab3256a5525"
        auth_token = "a744e96a268f0465ebb6b8a3719eafd4"
        client = Client(account_sid, auth_token)

        try:
            message = client.messages.create(to="+977"+phone, from_="+14804850113",
                                   body="Hello there! Your order has been placed.")
        except TwilioRestException as e:
            print(e)

        return super().form_valid(form)
    

    def get_success_url(self):

        return "/product/" + str(self.kwargs['pk']) + "/order"



