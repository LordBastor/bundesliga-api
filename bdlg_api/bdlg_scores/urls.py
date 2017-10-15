from django.conf.urls import url
from bdlg_scores import views

urlpatterns = [
    url(r'^scores$', views.TeamScoreListView.as_view()),
    url(r'^scores/(?P<team_id>[0-9]+)$', views.TeamScoreDetailView.as_view()),
]
