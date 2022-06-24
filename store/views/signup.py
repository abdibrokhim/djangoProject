from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class SignUp(View):
    def get(self, request):
        return render(request, 'html/index.html')

    def post(self, request):
        postdata = request.POST
        firstname = postdata.get('firstname')
        lastname = postdata.get('lastname')
        # phone = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')
        # confirm_password = password

        # validation
        value = {
            'firstname': firstname,
            'lastname': lastname,
            # 'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(firstname=firstname,
                            lastname=lastname,
                            # phone=phone,
                            email=email,
                            password=password,
                            # confirm_password=password
                            )
        error_message = self.valid(customer)

        if not error_message:
            print(firstname, lastname, email, password)
            customer.password = make_password(customer.password)
            customer.sign_up()
            return redirect('main')
        else:
            data = {
                'error_signup': error_message,
                'values': value
            }
            return render(request, 'html/index.html', data)

    def valid(self, customer):
        error_message = None
        if not customer.firstname:
            error_message = "Please Enter your First Name"
        elif len(customer.firstname) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not customer.lastname:
            error_message = 'Please Enter your Last Name'
        elif len(customer.lastname) < 3:
            error_message = 'Last Name must be 3 char long or more'
        # elif not customer.phone:
        #     error_message = 'Enter your Phone Number'
        # elif len(customer.phone) < 10:
        #     error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 8:
            error_message = 'Password must be 8 char long'
        # elif customer.password != confirm_password:
        #     error_message = 'Password does not match'
        elif len(customer.email) < 10:
            error_message = 'Invalid Email Address'
        elif customer.is_customer():
            error_message = 'Email Address Already Registered'
        return error_message
