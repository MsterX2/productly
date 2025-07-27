from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto, Categoria


def index(request):
    productos = Producto.objects.all()
    return render(
        request,
        "index.html",
        context={"productos": productos}
    )
