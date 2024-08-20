# <!-- Made By - Asmita Kumari -->

from rest_framework.views import APIView
from .serializers import KrisshakSerializer
from django.http.response import JsonResponse
from .models import Krisshak
from django.http import Http404
from rest_framework.response import Response

# Create your views here.

class KrisshakView(APIView):

    def get_krisshak(self , pk):
        try:
            krisshak= Krisshak.objects.get(krisshakId=pk)
            return krisshak
        # except Krisshak.DoesNotExist():
            # raise Http404
        except Krisshak.DoesNotExist():    
            return JsonResponse("Krisshak Does not Exists", safe=False)
        
    def get(self,request,pk=None):
        if pk:
            data=self.get_krisshak(pk)
            serializer=KrisshakSerializer(data)
        else:
            data=Krisshak.objects.all()
            serializer=KrisshakSerializer(data ,many=True)
        return Response(serializer.data)
        
    def post(self, request):
        data=request.data
        serializer=KrisshakSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Krisshak Created Successfully" , safe=False)
        return JsonResponse("Failed To Create Krisshak", safe=False)
    
    def put(self, request,pk=None):
        krisshak_to_update=Krisshak.objects.get(krisshakId=pk)
        serializer=KrisshakSerializer(instance=krisshak_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Krisshak Updated Successfully" , safe=False)
        return JsonResponse("Failed To Update Krisshak", safe=False)
    
    def delete(self, request,pk=None):
        krisshak_to_delete=Krisshak.objects.get(krisshakId=pk)
        krisshak_to_delete.delete()
        return JsonResponse("Krisshak Deleted Successfully", safe=False)

    