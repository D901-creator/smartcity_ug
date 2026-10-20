from django.urls import path

from . import views


app_name = "education"


urlpatterns = [

    # Education Home
    path(
        "",
        views.education_home,
        name="home"
    ),

    # Institutions
    path(
        "institution/<int:pk>/",
        views.institution_detail,
        name="institution_detail"
    ),

    # Programmes & Courses
    path(
        "programmes/",
        views.programmes,
        name="programmes"
    ),

    # Scholarships
    path(
        "scholarships/",
        views.scholarships,
        name="scholarships"
    ),

    # Teachers
    path(
        "teacher-services/",
        views.teacher_services,
        name="teacher_services"
    ),

    # School Administrators
    path(
        "administrator-services/",
        views.administrator_services,
        name="administrator_services"
    ),

    # Funding
    path(
        "funding/",
        views.education_funding,
        name="funding"
    ),

    # Examinations
    path(
        "examinations/",
        views.examinations,
        name="examinations"
    ),

    # Education Services
    path(
        "services/",
        views.education_services,
        name="services"
    ),

    # Government Programmes
    path(
        "government-programmes/",
        views.government_programmes,
        name="government_programmes"
    ),

    # Applications
    path(
        "application/",
        views.education_application,
        name="application"
    ),

    path(
        "application/success/",
        views.application_success,
        name="application_success"
    ),

    # Projects
    path(
        "projects/",
        views.education_projects,
        name="projects"
    ),

    # Notices
    path(
        "notices/",
        views.education_notices,
        name="notices"
    ),

    # Report Problem
    path(
        "report-problem/",
        views.report_education_problem,
        name="report_problem"
    ),

    path(
        "report-problem/success/",
        views.problem_report_success,
        name="problem_report_success"
    ),

    # General Request
    path(
        "request/",
        views.education_request,
        name="request"
    ),

    path(
        "request/success/",
        views.request_success,
        name="request_success"
    ),

    # Information & Guidance
    path(
        "information/",
        views.education_information,
        name="information"
    ),

    # Statistics
    path(
        "statistics/",
        views.education_statistics,
        name="statistics"
    ),
    path(
    "learning-sources/",
    views.learning_sources,
    name="learning_sources"
),

path(
    "learning-sources/<int:pk>/",
    views.learning_resource_detail,
    name="learning_resource_detail"
),
]