from django.shortcuts import render_to_response
from django.template import RequestContext
from openshift.app.models import ImageFile
from django import forms

def upload_form(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            data = ImageFile()
            data.image = request.FILES['image']
            data.save()
    else:
        form = UploadForm()

    return render_to_response('home/view.html', {'items':items},
                              context_instance=RequestContext(request))