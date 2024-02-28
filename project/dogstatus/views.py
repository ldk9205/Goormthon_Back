# 데이터 처리
from .models import Dog
from .serializers import DogSerializer

# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Dog의 목록을 보여주는 역할
class DogList(APIView):
    # Dog list를 보여줄 때
    def get(self, request):
        Dogs = Dog.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = DogSerializer(Dogs, many=True)
        return Response(serializer.data)

    # 새로운 Dog 글을 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        temp = request.data
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Dog의 detail을 보여주는 역할
class DogDetail(APIView):
    # Dog 객체 가져오기
    def get_object(self, pk):
        try:
            return Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            raise Http404
    
    # Dog의 detail 보기
    def get(self, request, pk, format=None):
        Dog = self.get_object(pk)
        serializer = DogSerializer(Dog)
        return Response(serializer.data)

    # Dog 수정하기
    def put(self, request, pk, format=None):
        Dog = self.get_object(pk)
        serializer = DogSerializer(Dog, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Dog 삭제하기
    def delete(self, request, pk, format=None):
        Dog = self.get_object(pk)
        Dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  