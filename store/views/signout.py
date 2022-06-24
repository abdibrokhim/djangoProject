from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View


class SignOut(View):
    def logout(self, request):
        request.session.clear()
        return redirect('html/index.html')
