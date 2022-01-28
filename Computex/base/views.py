from django.db.models import Avg
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView, DeleteView

from .models import Stands, Supplier, Media, Application
from .forms import applicationForm, supplierForm, mediaForm


def index(request):
    data = {
        'title': 'Главная страница',

    }
    return render(request, 'base/index.html', data)


def stands(request):
    stand = Stands.objects.all()
    return render(request, 'base/stands.html', {'stands': stand})


class standsDetailView(DetailView):
    model = Stands
    template_name = 'base/stand_detail.html'
    context_object_name = 'st'


def suppliers(request):
    supplier = Supplier.objects.all()
    return render(request, 'base/suppliers.html', {'supplier': supplier})

class suppliers_update(UpdateView):
    model = Supplier
    template_name = 'base/create.html'
    form_class = supplierForm


def suppliers_create(request):
    return Create(request, supplierForm, 'suppliers')

def suppliers_delete(request, pk):
    supplier = get_object_or_404(Supplier, id=pk)
    supplier.delete()
    return redirect('suppliers')

def media(request):
    media = Media.objects.all()
    return render(request, 'base/media.html', {'media': media})

class media_update(UpdateView):
    model = Media
    template_name = 'base/create.html'
    form_class = mediaForm

def media_create(request):
    return Create(request, mediaForm, 'media')

def media_delete(request, pk):
    media = get_object_or_404(Media, id=pk)
    media.delete()
    return redirect('media')


def applications(request):
    application = Application.objects.all()
    return render(request, 'base/applications.html', {'application': application})

def applications(request, filter):
    application = Application.objects.order_by(filter)
    avg = 0
    if 'search' in request.GET:
        search = request.GET['search']
        if search:
            nord = Application.objects.filter(Q(name__icontains=search) | Q(date__icontains=search))
            return render(request, 'base/applications.html', {'application': nord, 'search': search})
    return render(request, 'base/applications.html', {'application': application})


def application_create(request, pk):
    error = ''
    stand = get_object_or_404(Stands, id=pk)
    if request.method == 'POST':
        form = applicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stands')
        else:
            error = 'Неверная форма'
    form = applicationForm(initial={
        "stand": stand
    })

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'base/appcreate.html', data)


# __creator__
def Create(request, myform, redirector):
    error = ''
    if request.method == 'POST':
        form = myform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirector)
        else:
            error = 'Неверная форма'
    form = myform()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'base/create.html', data)
