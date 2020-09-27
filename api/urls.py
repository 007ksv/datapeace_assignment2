from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter

'''
	Defining router, so that we do not have to explicitly define all the urlpatterns. 
'''

router = SimpleRouter()
router.register('users', UsersViewSet, basename='users')
urlpatterns = router.urls
