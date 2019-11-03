from django.urls import path

# from . import views2
# from .views2 import (UserUpdateView)

from .views import users , general , cotizacion
from .views.users import (UserUpdateView)
from .views.cotizacion import (CotiUpdateView)

app_name = 'users'
urlpatterns = [

	###ROUTES GENERAL###
	path('' , general.home_view , name="home"),

	### ROUTES USERS###
    path('users/' , users.home , name="users_home"),
    path('users/details/' , users.details , name="user_details"),
    path('users/create/' , users.create , name="user_create"),
    path('users/<int:id>/update/' , UserUpdateView.as_view() , name="user_update"),
    path('users/<int:id>/deletelog/' , users.deletelog, name="user_deletelog"),
    path('users/<int:id>/delete/' , users.delete, name="user_delete"),
    path('users/restore' , users.restoreview, name="user_restore"),
    path('users/restored/<int:id>/' , users.restore, name="user_restore"),

    ### ROUTES COTIZACION ### 
    path('cotizacion/' , cotizacion.home , name ="coti_home"),
	path('cotizacion/create/' , cotizacion.create , name ="coti_create"),
    path('cotizacion/<int:id>/update/' , CotiUpdateView.as_view() , name="coti_update"),
    path('cotizacion/<int:id>/deletelog/' , cotizacion.deletelog, name="coti_deletelog"),
    path('cotizacion/<int:id>/delete/' , cotizacion.delete, name="coti_delete"),
    path('cotizacion/restore' , cotizacion.restoreview, name="coti_restore"),
    path('cotizacion/restored/<int:id>/' , cotizacion.restore, name="coti_restored")
	# path('users/<int:id>/cotizacion/create' , cotizacion.create , name ="coti_create")
    # path('coti/' , cotizacion.coti_view, name = "coti_home")

]
