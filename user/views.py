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

# 인천 지역정보 업로드
def upload_incheon():
    f_path = os.path.abspath(os.path.join(
        '인천광역시_법정동.csv'
    ))

    bulk_list = []

    with open(f_path, 'r', encoding='euc-kr') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            # print(row)
            bulk_list.append(
                IncheonRegion(
                    si = row[0],
                    gu = row[1],
                    emd = row[2]
                )
            )

    I = IncheonRegion.objects.bulk_create(bulk_list)
    print("!!Incheon Region upload success!!")
    return