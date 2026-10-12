from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate,login
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class LoginView(APIView):

    def post(self,request,*args,**kwargs):

        username=request.data.get('username')

        password=request.data.get('password')

        user= authenticate(username=username,password=password)

        if user:

            refresh_token=RefreshToken.for_user(user)

            access_token=refresh_token.access_token

        

            data={'access_token':str(access_token),'refresh_token':str(refresh_token)}

            return Response(data,status=200)

        data={'msg':'invalid credentials'}
        
        return Response(data,status=400)