from django.urls import path,include

# from .views import home
from .views import home,todo_list_create,todo_get_delete_update,Todos,TodosRUD,TodosMVS

from rest_framework import routers
router=routers.DefaultRouter()
router.register('todo',TodosMVS)


urlpatterns = [
    path('',home),
#     #fbv
#     path('list/',todo_list_create),
#     path('list/<int:id>',todo_get_delete_update)
      #cbv
    #   path('todo/',Todos.as_view()),
    #   path('todorud/<int:pk>',TodosRUD.as_view())
    #mvs
    path('',include(router.urls))
]

