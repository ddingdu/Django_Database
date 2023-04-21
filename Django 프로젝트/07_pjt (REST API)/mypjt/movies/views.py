from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Actor, Movie, Review
from .serializers import ActorSerializer, MovieSerializer, ReviewSerializer
from .serializers import MovieListSerializer, ActorListSerializer, ReviewListSerializer
# Create your views here.

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def actor_detail(request, actor_id):
    actor = Actor.objects.get(pk=actor_id)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)


@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_id):
    review = Review.objects.get(pk=review_id)

    if request.method == 'GET':
      serializer = ReviewSerializer(review)
      return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        review.delete()
        review_delete = {'delete' : f'review {review_id} is deleted'}
        return Response(review_delete, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
def create_review(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)