from rest_framework import serializers
from .models import Realtor

class RealtorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Realtor
        #fields =['name','photo','desc','email','is_mvp','phone','message','contact_date']

        # to get all attribute
        fields = '__all__'
        