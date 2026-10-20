
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


app_name = "accounts"

urlpatterns = [
    path("register/", views.register, name="register"),

    path("login/", views.login_view, name="login"),

    path(
    "logout/",
    auth_views.LogoutView.as_view(next_page="public_home"),
    name="logout",
),

    path(
        "verification-pending/",
        views.verification_pending,
        name="verification_pending",
    ),

    path(
        "verification/submit/",
        views.verification_submit,
        name="verification_submit",
    ),

    path(
        "verification-status/",
        views.verification_status,
        name="verification_status",
    ),

    path(
        "cities/",
        views.cities_by_district,
        name="cities_by_district",
    ),

    path("profile/", views.my_profile, name="profile"),

    path("settings/", views.settings_view, name="settings"),

    path(
        "change-password/",
        views.change_password,
        name="change_password",
    ),

    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset.html",
            email_template_name="accounts/password_reset_email.html",
            subject_template_name="accounts/password_reset_subject.txt",
            success_url="/accounts/password-reset/done/",
        ),
        name="password_reset",
    ),

    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html",
        ),
        name="password_reset_done",
    ),

    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",
            success_url="/accounts/reset/done/",
        ),
        name="password_reset_confirm",
    ),

    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
    
]
