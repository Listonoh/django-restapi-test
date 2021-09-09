from django.shortcuts import render
from numpy import result_type
from django.core.paginator import Paginator
import requests

# Create your views here.


def get_page_obj_from_result(request_result, page_number):
    current_page = int(request_result.headers["x-pagination-current-page"])
    page_count = int(request_result.headers["x-pagination-page-count"])
    per_page = int(request_result.headers["x-pagination-per-page"])
    print(current_page, page_count, per_page)
    extended_result = [None] * (current_page-1)*per_page + \
        request_result.json() + [None] * (page_count - current_page)*per_page
    print(extended_result)
    p = Paginator(extended_result, per_page)
    return p.get_page(page_number)


def index(request):
    page_number = request.GET.get('page')
    target_url = f'https://faktury.mzcr.cz/rest/organizations/?page={page_number}&per-page=5'
    result = requests.get(target_url)
    organizations = get_page_obj_from_result(result, page_number)

    context = {"organizations": organizations}
    return render(request, 'catalog/index.html', context)
