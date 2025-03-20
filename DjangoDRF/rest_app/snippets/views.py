from rest_framework import generics
from rest_framework import viewsets
from snippets.serializers import SnippetSerializer
from snippets.models import Snippet
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#for routers
class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({'message': 'Logged in successfully'})
        return JsonResponse({'error': 'Invalid credentials'}, status=400)

def user_logout(request):
    logout(request)
    return JsonResponse({'message': 'Logged out successfully'})


# for generic urlpattern definition
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


#custom class based views to handle all requests
class SnippetAPIView(APIView):
    def get(self, request):
        return Response({'message': 'GET request received'}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({'message': 'POST request received'}, status=status.HTTP_201_CREATED)

    def put(self, request):
        return Response({'message': 'PUT request received'}, status=status.HTTP_200_OK)

    def delete(self, request):
        return Response({'message': 'DELETE request received'}, status=status.HTTP_204_NO_CONTENT)



#function based views

# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)



# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)