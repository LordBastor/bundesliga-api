from django.conf.urls import url
from bdlg_alive import views

urlpatterns = [
    url(r'^alive$', views.AliveView.as_view()),
]
