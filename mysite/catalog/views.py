from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
import requests
from .decorators import handle_view_exception

# Create your views here.


def get_page_obj_from_result(request_result, page_number):
    current_page = int(request_result.headers["x-pagination-current-page"])
    page_count = int(request_result.headers["x-pagination-page-count"])
    per_page = int(request_result.headers["x-pagination-per-page"])

    extended_result_for_paginator = [None] * (current_page-1)*per_page + \
        request_result.json() + [None] * (page_count - current_page)*per_page
    p = Paginator(extended_result_for_paginator, per_page)
    return p.get_page(page_number)


def clean_int_input(number: str, default_result=1) -> int:
    if not number.isnumeric():
        return default_result
    return int(number)


@handle_view_exception
def index(request):
    page_number = clean_int_input(request.GET.get('page', '1'))
    per_page = clean_int_input(request.GET.get('per-page', '5'), 5)
    target_url = f'https://faktury.mzcr.cz/rest/organizations/?page={page_number}&per-page={per_page}'
    result = requests.get(target_url)
    result.raise_for_status()

    if per_page < 1 or int(result.headers["x-pagination-page-count"]) < page_number or page_number < 1:
        raise Http404()
    organizations = get_page_obj_from_result(result, page_number)

    context = {"organizations": organizations, "per_page": per_page}
    return render(request, 'catalog/index.html', context)
