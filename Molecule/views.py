from django.forms import ModelChoiceField
from django.http import JsonResponse
from .models import Molecule
from .serializers import MoleculeSerialiser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def Molecule_list(request, format=None):

    if request.method == 'GET':
        molecules = Molecule.objects.all()
        serializer = MoleculeSerialiser(molecules, many=True)
        return Response(serializer.data)                   #updated    
        #return JsonResponse(serializer.data, safe=False)  #old

    if request.method == 'POST':
        serializer = ModelChoiceField(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def Molecule_detail(request, id, format=None):

    try:
        molecules = Molecule.objects.get(pk=id)
    except Molecule.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = MoleculeSerialiser(molecules)
        return Response(serializer.data)

    elif request.method =='PUT':
        serializer = MoleculeSerialiser(molecules, data=request.data)
        if serializer.is_valid():
            serializer.dave()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        molecules.delete()
        return Response(status.HTTP_204_NO_CONTENT)