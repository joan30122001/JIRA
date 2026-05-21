from django.urls import path
from . import views

urlpatterns = [
    path("testrail/projects/", views.testrail_projects, name="testrail_projects"),
    path("testrail/projects/create/", views.testrail_create_project, name="testrail_create_project"),

    path("testrail/projects/<int:project_id>/milestones/create/", views.testrail_create_milestone, name="testrail_create_milestone"),
    path("testrail/projects/<int:project_id>/suites/", views.testrail_suites, name="testrail_suites"),
    path("testrail/projects/<int:project_id>/sections/create/", views.testrail_create_section, name="testrail_create_section"),
    path("testrail/projects/<int:project_id>/runs/create/", views.testrail_create_run, name="testrail_create_run"),
    path("testrail/projects/<int:project_id>/plans/create/", views.testrail_create_plan, name="testrail_create_plan"),

    path("testrail/sections/<int:section_id>/cases/create/", views.testrail_create_case, name="testrail_create_case"),
    path("testrail/cases/<int:case_id>/update/", views.testrail_update_case, name="testrail_update_case"),

    path("testrail/statuses/", views.testrail_statuses, name="testrail_statuses"),

    path("testrail/runs/<int:run_id>/close/", views.testrail_close_run, name="testrail_close_run"),
    path("testrail/runs/<int:run_id>/results/bulk/", views.testrail_add_bulk_results, name="testrail_add_bulk_results"),
    path("testrail/runs/<int:run_id>/cases/<int:case_id>/result/", views.testrail_add_result, name="testrail_add_result"),

    path("testrail/plans/<int:plan_id>/entries/create/", views.testrail_add_plan_entry, name="testrail_add_plan_entry"),
]