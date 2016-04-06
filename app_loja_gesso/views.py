from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import *


def fornecedor(request):
    if request.method == "POST":
        form = FormFornecedor(request.FILES, request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormFornecedor()
    return render_to_response("fornecedor.html", {"form": form}, RequestContext(request))


def produtos(request):
    if request.method == "POST":
        form = FormProduto(request.FILES, request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormProduto()
    return render_to_response("produtos.html", {"form": form}, RequestContext(request))