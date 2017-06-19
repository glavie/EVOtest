# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from operator import attrgetter

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from lucky.forms import NamesForm
from lucky.models import Names


def main_page(request):
    return render(request, 'lucky/main.html', {'form': NamesForm()})


def names_list(request):
    return render(
        request,
        'lucky/names_list.html',
        {
            'form': NamesForm(),
            'names': Names.objects.all()},
    )


@require_POST
def add_name(request):
    form = NamesForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['name']
        if Names.objects.filter(name=username).exists():
            return JsonResponse(
                {'errors': 'name is already in db'},
                status=400
            )
        form.save()
        return JsonResponse(
            {'done': 'name successfully added to db!'},
            status=200
        )
    else:
        return JsonResponse({'errors': form.errors}, status=400)


@require_POST
def del_name(request):
    form = NamesForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['name']
        if not Names.objects.filter(name=username).exists():
            print JsonResponse({'errors': 'name missed in db'}, status=400)
            return JsonResponse({'errors': 'name missed in db'}, status=400)
        Names.objects.filter(name=username).delete()
        print(JsonResponse(
            {'names': map(attrgetter('name'), Names.objects.all())},
        ))
        return JsonResponse(
            {'names': map(attrgetter('name'), Names.objects.all())},
        )
    return JsonResponse({'errors': form.errors}, status=400)


def rand_names(request):
    luckers = Names.objects.all()
    len_names = len(luckers)
    if len_names == 0:
        return HttpResponse('No any names in db')
    return HttpResponse(
            'luckers: {}'.format(
                ', '.join(
                    Names.objects.all().order_by(
                        '?'
                    )[:3].values_list('name', flat=True))
            )
    )
