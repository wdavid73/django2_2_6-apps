from django.shortcuts import render ,redirect , get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

# # Models
# from ..models import User
# #Forms
# from ..forms import UserForm , UserFormModel
# # Create your views here.
# from django.views.generic import (UpdateView)


def home_view(request , *args, **kwargs):
    return render(request , "home.html" , {})


def handler404(request, *args, **argv):
    response = render_to_response(
    			'404.html', {},
                context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response