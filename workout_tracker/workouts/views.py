from django.shortcuts import render
from django.utils.dateparse import parse_datetime, parse_duration
from django.db.models import Avg, Sum
from rest_framework import generics, views, response, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Workout
from .serializers import WorkoutSerializers
from .utils import get_filtered_workouts

class WorkoutListCreate(generics.ListCreateAPIView):
    serializer_class = WorkoutSerializers


    def list(self, request, *args, **kwargs):
        queryset = get_filtered_workouts(request)


        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return response.Response({
            'workouts': serializer.data,
        })

class WorkoutAggregatedData(APIView):
    def get(self, request, *args, **kwargs):
        queryset = get_filtered_workouts(request)
        aggregated_data = self.get_aggregated_data(queryset)
        return Response(aggregated_data)
    
    def get_aggregated_data(self, queryset):
        average_duration = queryset.aggregate(Avg('duration'))['duration__avg']
        average_distance = queryset.aggregate(Avg('distance'))['distance__avg']
        average_heart_rate = queryset.aggregate(Avg('heart_rate'))['heart_rate__avg']
        total_duration = queryset.aggregate(Sum('duration'))['duration__sum']
        total_distance = queryset.aggregate(Sum('distance'))['distance__sum']

        total_duration_in_minutes = total_duration.total_seconds() / 60 if total_duration else 0

        average_pace = total_duration_in_minutes / total_distance if total_distance else 0
        return {
            'total_duration' : total_duration,
            'average_duration': average_duration,
            'total_distance': total_distance, 
            'average_distance': average_distance, 
            'average_heart_rate': average_heart_rate,  
            'average_pace' : average_pace
        }
    
class WorkoutBulkDelete(APIView):
    def delete(self, request, *args, **kwargs):
        queryset = get_filtered_workouts(request)
        queryset.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)