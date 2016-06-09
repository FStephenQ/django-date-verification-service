from django.http import HttpResponse
from django.template import Template
from django.shortcuts import render_to_response,render
import gnupg



gpg = gnupg.GPG(homedir='/var/secret/gpg',ignore_homedir_permissions=False)
KEYID = gpg.list_keys()[0]['fingerprint']

# Create your views here.
def sign(request):
    if request.method == 'POST':
        return HttpResponse(gpg.sign(request.body))
    else:
        return ''

def verify(request):
    if request.method == 'POST':
        return HttpResponse(gpg.verify(request.body))
    elif request.method == 'GET':
        return HttpResponse(open('/var/secret/pub.key','rb').read())
