
from django.urls import path

from . import views


app_name = "jobs"


urlpatterns = [

    # 18.1
    path(
        "",
        views.home,
        name="home"
    ),

    # 18.2
    path(
        "opportunities/",
        views.opportunities,
        name="opportunities"
    ),

    path(
        "opportunities/<int:job_id>/",
        views.opportunity_detail,
        name="opportunity_detail"
    ),

    # 18.3
    path(
        "skills/",
        views.skills,
        name="skills"
    ),

    path(
        "skills/<int:skill_id>/",
        views.skill_detail,
        name="skill_detail"
    ),

    # 18.4
    path(
        "career-guidance/",
        views.career_guidance,
        name="career_guidance"
    ),

    path(
        "employment-information/",
        views.employment_information,
        name="employment_information"
    ),

    # 18.5
    path(
        "statistics/",
        views.statistics,
        name="statistics"
    ),
]
