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

# 아동 정보 기입 (POST)
# /api/user/child/
"""
{
    "name":"김아동",
    "birthDate":"2020-12-06",
    "residence":1,
    "gender":"M",
    "kindergarden":"뫄뫄유치원",
    "testDate":"2022-12-06",
    "tester":1
}
"""
class ChildViewSet(ModelViewSet):
    serializer_class = ChildSerializer
    queryset = Child.objects.all()

class IncheonRegionViewSet(ModelViewSet):
    serializer_class = IncheonRegionSerializer
    queryset = IncheonRegion.objects.all()

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

# 인천광역시 **구 리스트
# /api/user/gulist
class GuList(APIView):
    def get(self, request):
        queryset = IncheonRegion.objects.distinct().values_list('gu')
        gu_list = []
        for q in queryset:
            gu_list.append(q[0])
        print(gu_list)
        return Response(gu_list)

# 인천광역시 **구 $$동 리스트
# ex) 인천광역시 남구에 있는 읍면동 리스트
# /api/user/emdlist?gu=남구
class Emdlist(APIView):
    def get(self, request):
        gu = self.request.query_params.get('gu')
        queryset = IncheonRegion.objects.filter(gu=gu)
        serializer_context = {'request': request}
        serializer_class = IncheonRegionSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer_class.data)