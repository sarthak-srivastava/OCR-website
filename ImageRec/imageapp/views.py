from django.shortcuts import render
from django.http import HttpResponse,HttpResponseForbidden
from . import form
from .models import Images
def upload_pic(request):
	if request.method == 'POST':
		fo = form.ImageUpload(request.POST, request.FILES)
		if fo.is_valid():
			m = Images.objects.get(pk=m_id)
			m.image = fo.cleaned_data['image']
			m.save()
			return HttpResponse('image upload success')
	return HttpResponseForbidden('allowed only via POST')
# Create your views here.
def home(request):
	return render(request,'index.html')