from django.contrib import admin
from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('boards', views.BoardViewSet, basename='boards')

urlpatterns = [
    
    # path('', views.BoardList.as_view(), name='home'), # Home page
    # path('boards/<int:board_id>/',views.BoardTopic.as_view(), name='board_topics'),
    # path('board_detail/<int:id>/',views.BoardDetails.as_view(), name='board_details'),
    # path('boards/<int:board_id>/new/', views.new_topic, name = 'new_topic'),
    # path('boards/<int:board_id>/topics/<int:topic_id>', views.topic_posts, name='topic_posts'),
    # path('boards/<int:board_id>/stopics/<int:topic_id>/reply/', views.reply_topic, name='reply_topic'),
    # path('boards/<int:board_id>/topics/<int:topic_id>/posts/<int:post_id>/edit/', views.PostUpdateView.as_view(),
    #      name='edit_post'),

]

urlpatterns = urlpatterns +router.urls