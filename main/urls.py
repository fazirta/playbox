from django.urls import path
from main.views import (
    landing,
    create,
    create_ajax,
    create_mood_flutter,
    edit,
    delete,
    show_xml,
    show_json,
    show_xml_by_id,
    show_json_by_id,
    profile,
    signup,
    signin,
    signout,
)

app_name = "main"

urlpatterns = [
    path("", landing, name="landing"),
    path("create", create, name="create"),
    path("create-ajax", create_ajax, name="create_ajax"),
    path("create-flutter/", create_mood_flutter, name="create-flutter"),
    path("edit/<uuid:id>", edit, name="edit"),
    path("delete/<uuid:id>", delete, name="delete"),
    path("xml/", show_xml, name="show_xml"),
    path("json/", show_json, name="show_json"),
    path("xml/<uuid:id>/", show_xml_by_id, name="show_xml_by_id"),
    path("json/<uuid:id>/", show_json_by_id, name="show_json_by_id"),
    path("profile/", profile, name="profile"),
    path("signup/", signup, name="signup"),
    path("signin/", signin, name="signin"),
    path("signout/", signout, name="signout"),
]
