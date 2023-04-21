from rest_framework import serializers
from .models import Actor, Movie, Review

# [ movies ]
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview',)

# actors의 name
class ActorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name',)

# reviews의 title, content
class ReviewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)

# movie 상세 (actors의 name / reviews의 title, content 가져오기)
class MovieSerializer(serializers.ModelSerializer):
    actors = ActorNameSerializer(many=True, read_only=True)
    review_set = ReviewSetSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'



# [ actors ]
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

# movies의 title
class MovieTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)

# actor 상세 (movies의 title 가져옴)
class ActorSerializer(serializers.ModelSerializer):
    movies = MovieTitleSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = ('id', 'movies', 'name',)



# [ reviews ]
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)

# review 상세
class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'movie', 'title', 'content',)
