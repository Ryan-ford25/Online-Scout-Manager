from . import views
from django.urls import path

urlpatterns = [
    path('blog/', views.PostList.as_view(), name = 'blog'),
    path('posts/<slug:slug>/', views.post_detail, name="post_detail"),
    path('posts/<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('posts/<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]