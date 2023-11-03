from django.urls import path
from .views import HomepageView, RegisterBoardView, ShowBoardsView, ChangeStatusView, ClearDefectView, AddDefectView
urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('register', RegisterBoardView.as_view(), name='register'),
    path('show', ShowBoardsView.as_view(), name='show'),
    path('change_status/<int:pk>', ChangeStatusView.as_view(), name='change_status'),
    path('clear_defect/<int:pk>', ClearDefectView.as_view(), name = 'clear_defect'),
    path('add_defect/<int:pk>/', AddDefectView.as_view(), name='add_defect')
]