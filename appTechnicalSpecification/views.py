from django.shortcuts import render, redirect
from .forms import EquipmentForm
from apiTechnicalSpecification.models import Equipment
from django.views.generic import UpdateView, DeleteView


class EquipmentUpdate(UpdateView):
    model = Equipment
    template_name = 'addPage.html'
    fields = ['equipment_type', 'serial_number', 'note']


class EquipmentDelete(DeleteView):
    model = Equipment
    success_url = '/'
    template_name = 'searchPage.html'


def mainPage(request):
    data = Equipment.objects.all()
    context = {'data': data}
    return render(request=request, template_name='mainPage.html', context=context)


def searchPage(request):
    return render(request=request, template_name='searchPage.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма не прошла валидацию'
    form = EquipmentForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'addPage.html', data)
