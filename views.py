from django.shortcuts import render

import json
from django.http import HttpResponse

from management.models import Books, Patron, Borrowing
# Create your views here.

def Borrowing_Date(request, membership_id):
    borrowing_date = Borrowing.objects.get(id = membership_id)
    return_date = Borrowing.objects.filter(id = membership_id) 
    date_list = []
    for date in Borrowing_Date:
        date_list.append({'date': date.borrowing_date})
    context = {
        'borrowing_date': str(date.borrowing_date),
        'return_date': str(date.return_date),
    }
    return render(request, "library/borrow_date.html", context)
