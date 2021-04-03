from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from apps.steganography.allPixels import enhanced_hide, enhanced_retr, rgb2hex
from apps.steganography.models import StatusTracker
from apps.steganography.utils.status import createStatus, getProgress, deleteStatus, temp
from apps.steganography.utils.others import JSONEncoder
# Create your views here.
from PIL import Image
from django import forms
import json

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def statusId(request):
    status = createStatus()
    a = JSONEncoder().encode({"id": status._id}) 
    return HttpResponse(a)

def decode(request, id):
    image = request.FILES.get("image")

    decoded_text = enhanced_retr(image, id)
    filename = "message.txt"
    response = HttpResponse(decoded_text, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
    return response


def encode(request, id):
    """
    Turn on CSRF middleware in settings.py later
    """

    if request.method == "GET":
        return JsonResponse({"Success": False})

    text = request.POST.get("text")
    text = text.encode()
    
    txtFile = request.FILES.get("txtFile")
    if txtFile:
        text  = txtFile.read()
    
    image = request.FILES.get("image")

    img = enhanced_hide(image, text, id)

    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="myImg.png"'
    img.save(response, "PNG")
    return(response)


def homePage(request):
    return render(request, "steganography/index.html")
    
def hide(request):
    return render(request, "steganography/hide.html")

def retrieve(request):
    return render(request, "steganography/retrieve.html")

def statusMeter(request, id):
    progress = getProgress(id)
    a = JSONEncoder().encode({"progress": progress}) 
    return HttpResponse(a)