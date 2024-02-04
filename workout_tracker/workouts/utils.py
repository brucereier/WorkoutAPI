from django.utils.dateparse import parse_datetime, parse_duration
from .models import Workout

def get_filtered_workouts(request):

        queryset = Workout.objects.all()
        min_id = request.query_params.get('min_id', None)
        max_id = request.query_params.get('max_id', None)
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)
        route_name = request.query_params.get('route_name', None)
        min_distance = request.query_params.get('min_distance', None)
        max_distance = request.query_params.get('max_distance', None)
        min_duration = request.query_params.get('min_duration', None)
        max_duration = request.query_params.get('max_duration', None)

        if min_id:
            queryset = queryset.filter(id__gte=min_id)

        if max_id:
            queryset = queryset.filter(id__lte=max_id)

        if start_date and end_date:
            start_datetime = parse_datetime(start_date)
            end_datetime = parse_datetime(end_date)
            if start_datetime and end_datetime:
                queryset = queryset.filter(date_time__range=[start_datetime, end_datetime])

        if route_name:
            queryset = queryset.filter(route_name__icontains=route_name)

        if min_distance:
            queryset = queryset.filter(distance__gte=min_distance)

        if max_distance:
            queryset = queryset.filter(distance__lte=max_distance)
        
        if min_duration:
            min_duration_obj = parse_duration(min_duration)
            if min_duration_obj:
                queryset = queryset.filter(duration__gte=min_duration_obj)

        if max_duration:
            max_duration_obj = parse_duration(max_duration)
            if max_duration_obj:
                queryset = queryset.filter(duration__lte=max_duration_obj)

        return queryset