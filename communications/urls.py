from django.urls import path

from . import views


app_name = "communications"


urlpatterns = [

    # Community Chat
    path(
        "",
        views.chat,
        name="chat",
    ),

    # Send message
    path(
        "send/",
        views.send_message,
        name="send_message",
    ),

    # Get messages
    path(
        "messages/",
        views.message_list,
        name="message_list",
    ),

    # Online users
    path(
        "online/",
        views.online_users,
        name="online_users",
    ),
    path(
        "message/<int:message_id>/delete/",
        views.delete_message,
        name="delete_message",
    ),
    path(
        "settings/",
        views.chat_settings,
        name="chat_settings",
    ),

    path(
        "settings/update/",
        views.update_chat_settings,
        name="update_chat_settings",
    ),

    path(
        "clear/",
        views.clear_chat,
        name="clear_chat",
    ),

]