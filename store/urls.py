from django.contrib import admin
from django.urls import path
from .views.index import Index
# from .views.home import store
from .views.signup import SignUp
from .views.signin import SignIn
from .views.signout import SignOut
# from .views.cart import Cart
# from .views.checkout import CheckOut
# from .views.orders import OrderView
# from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='main'),
    # path('store', store, name='store'),

    path('signup', SignUp.as_view(), name='signup'),
    path('signin', SignIn.as_view(), name='signin'),
    path('signout', SignOut.as_view(), name='signout'),
    # path('cart/', auth_middleware(Cart.as_view()), name='cart'),
    # path('checkout/', CheckOut.as_view(), name='checkout'),
    # path('orders/', auth_middleware(OrderView.as_view()), name='orders'),
]
