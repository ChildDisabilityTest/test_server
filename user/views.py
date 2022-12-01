from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
import os, csv
from rest_framework.views import APIView
from rest_framework.response import Response

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

class GuList(APIView):
    def get(self, request):
        queryset = IncheonRegion.objects.distinct().values_list('gu')
        gu_list = []
        for q in queryset:
            gu_list.append(q[0])
        print(gu_list)
        return Response(gu_list)

class EmdList(APIView):
    def get(self, request, gu):
        queryset = IncheonRegion.objects.filter(gu=gu)
        print(queryset)
        # serializer_context = {'request': request}
        # serializer_class = IncheonRegionSerializer(queryset, many=True, context=serializer_context)
        # return Response(serializer_class.data)
        return Response({"response":"test"})