from django.urls import path
from .views import WorkoutListCreate, WorkoutAggregatedData, WorkoutBulkDelete

urlpatterns = [
    path('api/workouts/', WorkoutListCreate.as_view(), name='workout-list-create'),
    path('api/workouts/aggregated/', WorkoutAggregatedData.as_view(), name='workout-aggregated-data'),
    path('api/workouts/delete/', WorkoutBulkDelete.as_view(), name='workout-bulk-delete'),
]
