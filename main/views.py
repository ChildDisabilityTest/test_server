from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
import os
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# 질문 CRUD viewset
class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

# 질문 업로드
def upload_questions():

    f_path = os.path.abspath(os.path.join(
        'question.txt'
    ))

    bulk_list = []

    f = open(f_path, 'r', encoding='UTF-8')
    while True:
        line = f.readline()
        if not line: break
        # print(line)
        l = line.strip().split('|')
        bulk_list.append(
            Question(
                number = int(l[0]),
                content = l[3],
                test_column = l[2],
                group = l[1]
            )
        )
        
    Q = Question.objects.bulk_create(bulk_list)
    print("!!question upload success!!")
    return

# 그룹별(A/B/C)로 질문 리스트 반환
# ex) 그룹A
# /api/main/questionlistbygroup?group=A
class QuestionListByGroup(APIView):
    def get(self, request):
        group = self.request.query_params.get('group')
        queryset = Question.objects.filter(group=group)
        serializer_context = {'request': request}
        serializer_class = QuestionSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer_class.data)

# 번호 범위대로 질문 리스트 반환
# ex) 11번 ~ 15번
# /api/main/questionlistbynumber?min=11&max=15
class QuestionListByNumber(APIView):
    def get(self, request):
        min = self.request.query_params.get('min')
        max = self.request.query_params.get('max')
        queryset = Question.objects.filter(number__range=[min, max])
        serializer_context = {'request': request}
        serializer_class = QuestionSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer_class.data)