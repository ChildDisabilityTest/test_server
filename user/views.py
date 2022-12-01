from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
import os, csv

# Create your views here.
class TesterViewSet(ModelViewSet):
    serializer_class = TesterSerializer
    queryset = Tester.objects.all()

class ChildViewSet(ModelViewSet):
    serializer_class = ChildSerializer
    queryset = Child.objects.all()

def upload_incheon():
    f_path = os.path.abspath(os.path.join(
        '인천광역시_법정동.csv'
    ))

    with open(f_path, 'r', encoding='euc-kr') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print(row)

    return