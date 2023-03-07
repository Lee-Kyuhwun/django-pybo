from django.urls import path

from . import views

app_name = 'pybo'
# 네임스페이스를 의미하는 app_name이다.
# 이럴경우 pybo앱 이외의 다른 앱이 프로젝트에 추가 될 수 도 있는데
# 이런경우 다른 앱에서 동일한 url 별칭을 사용하면 중복이 발생할 수 있다.
# 이를 위해 app_name를 설정해둔다.

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('answer/creaste/<int:question_id>/', views.answer_create , name ='answer_create'),
    path('question/create', views.question_create,name ='question_create'),
]