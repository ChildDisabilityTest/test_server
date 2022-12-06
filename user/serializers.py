from rest_framework import serializers
from .models import *

class TesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tester
        fields = ['url', 'id', 'name', 'birthDate', 'email', 'privacy_agree']

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['url', 'id', 'name', 'birthDate', 'residence', 'gender', 'kindergarden', 'testDate', 'tester']

class IncheonRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncheonRegion
        fields = ['url', 'id', 'si', 'gu', 'emd']