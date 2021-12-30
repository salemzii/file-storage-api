"""simplstorage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from storageapp import views
from frontend import views as frontendviews
from accounts import views as accountViews

from rest_framework import routers
from storageapp.views import AuthViewSet
from django.contrib.auth import views as auth_views

from graphene_django.views import GraphQLView
from graphQL_Apis.schema import schema


urlpatterns = [
    path(r'^admin/', admin.site.urls),

    path('home', frontendviews.home, name= 'home'),
    path('upload_file', frontendviews.upload_file, name='uploadFILE'),
    path('upload_image', frontendviews.upload_image, name='uploadIMAGE'),
    path('my_images', frontendviews.my_images, name='myimages'),
    path('my_files', frontendviews.my_files, name='myfiles'),

    path('signup', accountViews.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('api/upload_file', views.upload_file, name='upload_file'),
    path('api/files', views.get_files, name='get_files'),
    path('api/file/<slug:fileId>', views.get_file, name='get_file'),

    path('api/upload_image', views.upload_image, name='upload_image'),
    path('api/images', views.get_images, name='get_images'),
    path('api/image/<slug:imageId>', views.get_image, name='get_image'),

    path("api/graphql", GraphQLView.as_view(graphiql=True, schema=schema)),

]

router = routers.DefaultRouter(trailing_slash=False)
router.register('api/auth', AuthViewSet, basename='auth')

urlpatterns += router.urls