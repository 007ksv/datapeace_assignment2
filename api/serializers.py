from .models import CustomUser
from rest_framework import serializers

'''
	CustomUserSerializer
'''


class CustomUserSerializer(serializers.ModelSerializer):

	class Meta:

		model = CustomUser
		fields = '__all__'
