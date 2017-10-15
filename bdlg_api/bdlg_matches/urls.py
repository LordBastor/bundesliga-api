from django.conf.urls import url
from bdlg_matches import views

urlpatterns = [
    url(r'^upcoming_matches$', views.UpcomingMatchView.as_view()),
    url(r'^upcoming_matches/(?P<team_id>[0-9]+)$', views.UpcomingMatchTeamView.as_view()),
    url(r'^all_matches$', views.AllMatchView.as_view()),
]
