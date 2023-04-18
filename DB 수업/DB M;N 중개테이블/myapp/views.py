from django.shortcuts import render
from django.db import connection
from django.db import reset_queries

from .models import PetSitter, Pet
# Create your views here.

def get_sql_queries(origin_func):
    def wrapper(*args, **kwargs):
        reset_queries()

        origin_func()

        query_info = connection.queries
        for query in query_info:
            print(query['sql'])
    
    return wrapper

@get_sql_queries
# 함수 만들기 (요청하는 거 아님)
def get_pet_data():
    pets = Pet.objects.all()
    for pet in pets: 
        print(f'{pet.name} | 집사 {pet.pet_sitter.first_name}')

    
    # query_info = connection.queries
    # for query in query_info:
    #     print(query['sql'])