"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from pybo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/',include('pybo.urls')),
    path('common/',include('common.urls')), # 이러면 이제 http://localhost:8000/common/ 으로 시작하는 URL은 모두 common/urls.py 파일을 참조할 것이다.
    path('', views.index, name='index'),  # '/' 에 해당되는 path
]
