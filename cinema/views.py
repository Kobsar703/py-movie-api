from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from cinema.models import Movie
from cinema.serializers import MovieSerializer


def movie_list(request):
    if request.method == "GET":
        buses = Movie.objects.all()
        serializer = MovieSerializer(buses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
