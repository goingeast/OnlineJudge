from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic


def defaultView(request):
    context= {}
    return render(request, "base.html",context)
