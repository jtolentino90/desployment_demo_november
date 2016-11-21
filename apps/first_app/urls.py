# Now from within your newly created apps/first_app/urls.py file...
from django.conf.urls import url
from . import views


# Models -- Views -- Templates
# v



def index(request):
	print ("*"*100)
	print ("*"*100)
	print ("*"*100)
	print ("banana peel")
	print "Whatever route that was hit by an HTTP request (by the way) decided to invoke me!"
	print "By the way, here's the request object that Django automatically passes us:", request
	print "By the by, we still aren't delivering anything to the browser, so you should see 'ValueError at /'"

urlpatterns = [
	url(r'^$', views.index)
]
