# <!-- Made By - Asmita Kumari -->

from rest_framework.views import APIView
from .serializers import KrisshakSerializer,UserSerializer
from django.http.response import JsonResponse
from .models import Krisshak
from django.http import Http404
from rest_framework.response import Response

from django.contrib.auth.models import User
from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.

# class KrisshakView(APIView):

#     def get_krisshak(self , pk):
#         try:
#             krisshak= Krisshak.objects.get(krisshakId=pk)
#             return krisshak
#         # except Krisshak.DoesNotExist():
#             # raise Http404
#         except Krisshak.DoesNotExist():    
#             return JsonResponse("Krisshak Does not Exists", safe=False)
        
#     def get(self,request,pk=None):
#         if pk:
#             data=self.get_krisshak(pk)
#             serializer=KrisshakSerializer(data)
#         else:
#             data=Krisshak.objects.all()
#             serializer=KrisshakSerializer(data ,many=True)
#         return Response(serializer.data)
        
#     def post(self, request):
#         data=request.data
#         serializer=KrisshakSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Krisshak Created Successfully" , safe=False)
#         return JsonResponse("Failed To Create Krisshak", safe=False)
    
#     def put(self, request,pk=None):
#         krisshak_to_update=Krisshak.objects.get(krisshakId=pk)
#         serializer=KrisshakSerializer(instance=krisshak_to_update, data=request.data, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Krisshak Updated Successfully" , safe=False)
#         return JsonResponse("Failed To Update Krisshak", safe=False)
    
#     def delete(self, request,pk=None):
#         krisshak_to_delete=Krisshak.objects.get(krisshakId=pk)
#         krisshak_to_delete.delete()
#         return JsonResponse("Krisshak Deleted Successfully", safe=False)

    
class KrisshakView(APIView):
    serializer_class = KrisshakSerializer
    permission_classes = [IsAuthenticated]
    
    def get_krisshak(self, pk):
        try:
            return Krisshak.objects.get(krisshakId=pk, author=self.request.user)
        except Krisshak.DoesNotExist:
            return JsonResponse("Krisshak Does not Exists", safe=False)
    
    def get(self, request, pk=None):
        if pk:
            # Retrieve a specific Krisshak for the authenticated user
            krisshak = self.get_krisshak(pk)
            serializer = KrisshakSerializer(krisshak)
        else:
            # Retrieve all Krisshaks for the authenticated user
            krisshaks = Krisshak.objects.filter(author=request.user)
            serializer = KrisshakSerializer(krisshaks, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        # Create a new Krisshak for the authenticated user
        data = request.data
        serializer = KrisshakSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save(author=request.user)
            return JsonResponse("Krisshak Created Successfully" , safe=False)
        return JsonResponse("Failed To Create Krisshak", safe=False)
    
    def put(self, request, pk=None):
        # Update an existing Krisshak for the authenticated user
        krisshak = self.get_krisshak(pk)
        serializer = KrisshakSerializer(instance=krisshak, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Krisshak Updated Successfully" , safe=False)
        return JsonResponse("Failed To Update Krisshak", safe=False)
    
    def delete(self, request, pk=None):
        # Delete an existing Krisshak for the authenticated user
        krisshak = self.get_krisshak(pk)
        krisshak.delete()
        return JsonResponse("Krisshak Deleted Successfully", safe=False)
    

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserDetailView(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
        })