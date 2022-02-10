
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from idea.views import (
  IdeaListView, IdeaDetailView, IdeaUpdateView,
  IdeaDeleteView, IdeaCreateView
)
from user.views import CustomLoginView, register, profile
from django.contrib.auth.views import (
  PasswordResetView, PasswordResetDoneView,
  PasswordResetConfirmView, PasswordResetCompleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', IdeaListView.as_view(), name='ideas'),
    path('idea/<int:pk>/', IdeaDetailView.as_view(), name='idea-detail'),
    path('idea/<int:pk>/update', IdeaUpdateView.as_view(), name='idea-update'),
    path('idea/<int:pk>/delete', IdeaDeleteView.as_view(), name='idea-delete'),
    path('new/', IdeaCreateView.as_view(), name='idea-new'),
    path('profile/', profile, name='profile'),
    # reset password
    path('password-reset/', PasswordResetView.as_view(
      template_name='user/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(
      template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
      template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(
      template_name='user/password_reset_complete.html'), name='password_reset_complete')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
