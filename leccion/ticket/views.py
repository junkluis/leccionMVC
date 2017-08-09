# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from datetime import date


def index(request):
	template = loader.get_template('ticket/index.html')
	tickets = ticket.objects.all()
	context = {
		'ticket':tickets,
	}
	return HttpResponse(template.render(context, request))


def updateTicket(request, Id):
	tick = ticket.objects.get(id=Id)
	template = loader.get_template('ticket/actTicket.html')
	emision = tick.fechaEmision
	fechaF = date(emision.year, emision.month, emision.day)
	context = {
		'id_tick': Id,
		'Precio': tick.Precio,
		'action': 'Actualizar',
		'Titulo': 'Actualizar Ticket',
		'Adquiriente': fact.Adquiriente,
		'Puesto': fact.Puesto,
		'fechaEmision': fechaF.strftime("%Y-%m-%d"),
		'Origen': fact.Origen,
		'Destino': fact.Destino,
	}
	return HttpResponse(template.render(context, request))

def update(request):
	return HttpResponse("ya mismo")