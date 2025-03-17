from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserList, PostListCreate, CommentListCreate, LikeListCreate

urlpatterns = [
    path('users/', UserList.as_view()),
    path('posts/', PostListCreate.as_view()),
    path('comments/', CommentListCreate.as_view()),
    path('likes/', LikeListCreate.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]