from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=60)

    # confirm_password = models.CharField(max_length=20)
    # phone_number = models.CharField(max_length=20)

    def sign_up(self):
        self.save()

    @staticmethod
    def get_customer(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def is_customer(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

    def __str__(self):
        return self.email
