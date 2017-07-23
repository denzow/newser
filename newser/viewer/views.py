from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    context = {
        "user": request.user
    }
    return render(request, "viewer/contents/list.html", context=context)

