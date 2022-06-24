from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View


class SignIn(View):
    return_url = None

    def get(self, request):
        SignIn.return_url = request.GET.get('return_url')
        return render(request, 'html/index.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if SignIn.return_url:
                    return HttpResponseRedirect(SignIn.return_url)
                else:
                    SignIn.return_url = None
                    return redirect('signin')
            else:
                error_message = 'Invalid'
        else:
            error_message = 'Invalid'

        print(email, password)
        return render(request, 'html/index.html', {'error_signin': error_message})


# def logout(request):
#     request.session.clear()
#     return redirect('login')
