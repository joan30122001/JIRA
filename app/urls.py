from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('jira', views.create_project_view, name='create_project'),
    path('jira-projects/', views.list_jira_projects, name='jira-projects'),
    path('projects/<int:project_id>/upload-steps/', views.upload_steps_view, name='upload_steps'),
    path('projects/<int:project_id>/', views.project_detail_view, name='project_detail'),
    path("run-test/", views.run_test, name="test-page"),
    path('update-step-status/', views.update_step_status, name='update_step_status'),
    path('test-cases', views.test_cases_view, name='test_cases'),
    path('update-step-status/', views.update_step_status, name='update_step_status'),

    path('upload_project_with_steps/',
        views.upload_project_with_steps_view,
        name='upload_project_with_steps'),
]
