from django.urls import path
from .views             import users , general , cotizacion , user_coti
from .views.users       import (UserCreateView , UserUpdateView , UserListView ,UserDeleteView)
from .views.cotizacion  import (CotiCreateView , CotiUpdateView , CotiListView , CotiDeleteView)
from .views.general     import (ClothCreateView , AlquilerCreateView, AlquilerListView)
from .views.user_coti   import (UCListView)

api = 'api/v1/'
urlpatterns = [
	###ROUTES GENERAL###
	path(''                                   , general.home_view         , name = "home"),
    path( api                                 , general.home_api          , name = "home_api"),
	### ROUTES USERS###
    path(api + 'users/'                       , users.home                , name = "users_home"),
    path(api + 'users/details/'               , UserListView.as_view()    , name = "user_details"),
    path(api + 'users/create/'                , UserCreateView.as_view()  , name = "user_create"),
    path(api + 'users/<int:id>/update/'       , UserUpdateView.as_view()  , name = "user_update"),
    path(api + 'users/<int:id>/delete/'       , users.deletelog           , name = "user_deletelog"),
    path(api + 'users/restore'                , users.restoreview         , name = "user_restore"),
    path(api + 'users/restored/<int:id>/'     , users.restore             , name = "user_restore"),
    ### ROUTES COTIZACION ### 
    path(api + 'cotizacion/'                  , CotiListView.as_view()    , name = "coti_list"),
	path(api + 'cotizacion/create/'           , CotiCreateView.as_view()  , name = "coti_create"),
    path(api + 'cotizacion/<int:id>/update/'  , CotiUpdateView.as_view()  , name = "coti_update"),
    path(api + 'cotizacion/<int:id>/delete/'  , cotizacion.deletelog      , name = "coti_deletelog"),
    path(api + 'cotizacion/restore'           , cotizacion.restoreview    , name = "coti_restore"),
    path(api + 'cotizacion/restored/<int:id>/', cotizacion.restore        , name = "coti_restored"),
    ### ROUTES COTIZACION-CLIENT
    path(api + 'cotizacion-user/list/'        , user_coti.list_view       , name = "coti_user_list"),
    path(api + 'cotizacion-user/<int:id>/'    , user_coti.create_view     , name = "coti_user_create"),
    path(api + 'cotizacion-user/'             , user_coti.create          , name = "cu_create"),
    path(api + 'cotizacion_user/delete/'      , user_coti.deletelog       , name = "cu_deletelog"),
    path(api + 'cotizacion_user/restore'      , user_coti.restore_view    , name = "cu_restore_view"),
    path(api + 'cotizacion_user/restored'     , user_coti.restore         , name = "cu_restore"),
    ### ROUTES CLOTH
    path(api + 'cloth/create/'                , ClothCreateView.as_view()     , name = "cloth_create"),
    ### ROUTES ALQUILER
    path(api + 'alquiler/create/'             , AlquilerCreateView.as_view()  , name = "alquiler_create"),
    path(api + 'alquiler/details/all'         , AlquilerListView.as_view()    , name = "alquiler_details_all"),
]
