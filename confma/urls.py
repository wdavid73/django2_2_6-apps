from django.urls import path

# from . import views2
# from .views2 import (UserUpdateView)

from .views             import users , general , cotizacion , user_coti
from .views.users       import (UserCreateView , UserUpdateView , UserListView ,UserDeleteView)
from .views.cotizacion  import (CotiCreateView , CotiUpdateView , CotiListView , CotiDeleteView)
from .views.user_coti   import (UCListView)

# app_name = 'users'
urlpatterns = [

	###ROUTES GENERAL###
	path('' , general.home_view , name="home"),

	### ROUTES USERS###
    path('users/'                       , users.home                , name="users_home"),
    path('users/details/'               , UserListView.as_view()    , name="user_details"),
    path('users/create/'                , UserCreateView.as_view()  , name="user_create2"),
    path('users/<int:id>/update/'       , UserUpdateView.as_view()  , name="user_update"),
    path('users/<int:id>/delete/'       , users.deletelog           , name="user_deletelog"),
    # path('users/<int:id>/delete/'     , UserDeleteView.as_view()  , name="user_delete"),
    path('users/restore'                , users.restoreview         , name="user_restore"),
    path('users/restored/<int:id>/'     , users.restore             , name="user_restore"),

    ### ROUTES COTIZACION ### 
    path('cotizacion/'                      , CotiListView.as_view()    , name ="coti_list"),
	path('cotizacion/create/'               , CotiCreateView.as_view()  , name ="coti_create"),
    path('cotizacion/<int:id>/update/'      , CotiUpdateView.as_view()  , name="coti_update"),
    # path('cotizacion/<int:id>/delete/'    , CotiDeleteView.as_view()  , name="coti_delete"),
    path('cotizacion/<int:id>/delete/'      , cotizacion.deletelog      , name="coti_deletelog"),
    path('cotizacion/restore'               , cotizacion.restoreview    , name="coti_restore"),
    path('cotizacion/restored/<int:id>/'    , cotizacion.restore        , name="coti_restored"),

    ### ROUTES COTIZACION-CLIENT
    #path('cotizacon-user/list/'             , UCListView.as_view()      , name="coti_user_list"),
    path('cotizacion-user/list/'            , user_coti.list_view       , name="coti_user_list"),
    path('cotizacion-user/<int:id>/'        , user_coti.create_view     , name="coti_user_create"),
    path('cotizacion-user/'                 , user_coti.create          , name="cu_create"),
    path('cotizacion_user/delete/'          , user_coti.deletelog       , name="cu_deletelog"),
    path('cotizacion_user/restore'          , user_coti.restore_view    , name="cu_restore_view"),
    path('cotizacion_user/restored'         , user_coti.restore         , name="cu_restore"),
    

]
