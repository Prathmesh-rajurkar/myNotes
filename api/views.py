from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def getRoutes(request):
    return Response('Our API')


@api_view(['GET', 'POST'])
def getNotes(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes,many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def getNote(request,pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request,pk):
    data = request.data 
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note,data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted')

@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body = data['body']
    )
    serializer = NoteSerializer(note , many=False)
    return Response(serializer.data)




# https://github.com/divanov11/Django-React-NotesApp
# username = prathmsh199
#  password = Pr@thu
#  email = prathmeshrajurkar199@gmail.com