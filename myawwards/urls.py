from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.signup, name='registration'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('upload/',views.project,name='add_project'),
    path('project_details/', views.project_view, name='projectdetails'),
    path('review/', views.review_project, name='review'),
    path('search/', views.search_project, name='search'),
    path('api/projects',views.ProjectList.as_view(),name='projectsEndpoint'),
    path('api/profiles',views.ProfileList.as_view(),name='profilesEndpoint'),
    ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)