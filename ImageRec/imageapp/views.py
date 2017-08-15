from django.shortcuts import render
from django.http import HttpResponse,HttpResponseForbidden
from . import form
import tensorflow as tf
from .models import Images
def upload_pic(request):
	if request.method == 'POST':
		fo = form.ImageUpload(request.POST, request.FILES)
		if fo.is_valid():
			m = Images(image=request.FILES['image']) 
			m.image = fo.cleaned_data['image']
			m.save()
			return HttpResponse('image upload success')
	return HttpResponseForbidden('allowed only via POST')
# Create your views here.
def home(request):
	return render(request,'index.html')
def prediction(request):
	img = Images.objects.latest("id")
	with tf.Session() as sess:
		saver = tf.train.import_meta_graph('/tmp/model.ckpt.meta')
		saver.restore(sess, "/tmp/model.ckpt")
		feed_dict = {x:np.asarray(img)}
		y = sess.run(pred,feed_dict)
		return HttpResponse(y)
