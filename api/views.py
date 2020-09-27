from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets

# local imports
from .serializers import CustomUserSerializer
from .models import CustomUser
from .pagination import CustomPaginationClass


'''
	This view is responsible for all the actions on list of users or particular user.
'''

class UsersViewSet(viewsets.ModelViewSet):

	serializer_class = CustomUserSerializer
	queryset = CustomUser.objects.all()
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['first_name', 'last_name']
	ordering_fields = '__all__'							
	pagination_class = CustomPaginationClass			# Custom Pagination class (see pagination.py file).


	'''
		Overriding update method to overcome "Fields required error" 
		while updating user details (first_name, last_name and age)."
	'''

	def update(self, request, pk):
		serializer = CustomUserSerializer(instance=self.get_object(), data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

