from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignUpSerializer
from django.contrib.auth import authenticate,login
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
import requests,json

# Create your views here.

class SignUpAPIView(APIView):

    def get(self,request):
        return Response({'Message':'This is get method of signup API'},status=status.HTTP_200_OK)

    def post(self,request):
        try:
            obj =  SignUpSerializer(data =  request.data)
            if obj.is_valid():
                obj.save()
                return Response({'Message':'Successfully Signed up'},status = status.HTTP_200_OK)

            return Response(obj.errors,status = status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Message':'Something Failed due to {}'.format(str(e))}, status = status.HTTP_400_BAD_REQUEST)

    
class TokenAuthenticationView(APIView):

    def post(self,request):
        try:
            input_data =  request.data
            username =  input_data.get('username')
            password =  input_data.get('password')

            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                
                url =  'http://localhost:8000'+reverse('get-token')
                data = {'username':username,'password':password}
                tokens =  requests.post(url,data=data)

                return Response({'Tokens':json.loads(tokens.content)},status = status.HTTP_200_OK)
            else:   
                return Response({'Message':'Invalid username and password combination'}, status =  status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Message':'Something went wrong due to {}'.format(str(e))}, status = status.HTTP_400_BAD_REQUEST)


class TestAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({'Message': 'This is a test API'}, status =  status.HTTP_200_OK)


        
    
        


