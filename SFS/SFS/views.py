from django.http import HttpResponse, Http404
import datetime
def hello(request):
	return HttpResponse("Hello World")
def current_time(request):
	current= datetime.datetime.now()
	html = "<html><body> It is now %s</body> </html>" % current
	return HttpResponse(html)
def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	later = datetime.datetime.now() + datetime.timedelta(hours = offset)
	html = "<html><body> In %s hours it will be %s</body> </html>" % (offset,later)
	return HttpResponse(html)



