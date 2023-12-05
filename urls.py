from django.urls import path
from management.views import borrowing_date

# from management.views import *
# from management import views
#from management import views as management_view

urlpatterns=[
    path('date/<int:membership_id>', borrowing_date),

]