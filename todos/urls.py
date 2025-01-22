from django.urls import path
from . import views
urlpatterns = [
    path("list/", views.list_todo_items, name= "List"),
    path("insert_todo/", views.insert_todo_items, name= "insert_todo_items"),
    path("delete_todo/<int:todo_id>", views.delete_todo_items, name= "delete_todo_items")
]