from django.urls import path , include
from .views             import clients , general , cotizacion , client_coti , registration
from .views.clients       import (ClientCreateView , ClientUpdateView , ClientListView ,ClientDeleteView)
from .views.cotizacion  import (CotiCreateView , CotiUpdateView , CotiListView , CotiDeleteView)
from .views.general     import (ClothCreateView , AlquilerCreateView, AlquilerListView)
from .views.client_coti   import (UCListView)
from .views.registration import (SignUp)

api = 'api/v1/'
urlpatterns = [
	###ROUTES GENERAL###
	path('' , general.home_view , name = "home"),
    ### LOGIN AND LOGOUT

    path('', include('django.contrib.auth.urls')),
        # confma/ login/ [name='login']
        # confma/ logout/ [name='logout']
        # confma/ password_change/ [name='password_change']
        # confma/ password_change/done/ [name='password_change_done']
        # confma/ password_reset/ [name='password_reset']
        # confma/ password_reset/done/ [name='password_reset_done']
        # confma/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
        # confma/ reset/done/ [name='password_reset_complete'] 

    path('signup/' ,SignUp.as_view(), name="signup"),
        
    # path('logged/' ,registration.iniciar_sesion, name="iniciar_sesion"),
    



    ### ROUTES API
    path( api                                 , general.home_api          , name = "home_api"),
	   ### ROUTES USERS###
    path(api + 'clients/'                     , clients.home                , name = "clients_home"),
    path(api + 'clients/details/'             , ClientListView.as_view()    , name = "client_details"),
    path(api + 'clients/create/'              , ClientCreateView.as_view()  , name = "client_create"),
    path(api + 'clients/<int:id>/update/'     , ClientUpdateView.as_view()  , name = "client_update"),
    path(api + 'clients/<int:id>/delete/'     , clients.deletelog           , name = "client_deletelog"),
    path(api + 'clients/restore'              , clients.restoreview         , name = "client_restore"),
    path(api + 'clients/restored/<int:id>/'   , clients.restore             , name = "client_restored"),
        ### ROUTES COTIZACION ### 
    path(api + 'cotizacion/'                  , CotiListView.as_view()    , name = "coti_list"),
	path(api + 'cotizacion/create/'           , CotiCreateView.as_view()  , name = "coti_create"),
    path(api + 'cotizacion/<int:id>/update/'  , CotiUpdateView.as_view()  , name = "coti_update"),
    path(api + 'cotizacion/<int:id>/delete/'  , cotizacion.deletelog      , name = "coti_deletelog"),
    path(api + 'cotizacion/restore'           , cotizacion.restoreview    , name = "coti_restore"),
    path(api + 'cotizacion/restored/<int:id>/', cotizacion.restore        , name = "coti_restored"),
        ### ROUTES COTIZACION-CLIENT
    path(api + 'cotizacion-client/list/'      , client_coti.list_view       , name = "coti_user_list"),
    path(api + 'cotizacion-client/<int:id>/'  , client_coti.create_view     , name = "coti_user_create"),
    path(api + 'cotizacion-client/'           , client_coti.create          , name = "cu_create"),
    path(api + 'cotizacion-client/delete/'    , client_coti.deletelog       , name = "cu_deletelog"),
    path(api + 'cotizacion-client/restore'    , client_coti.restore_view    , name = "cu_restore_view"),
    path(api + 'cotizacion-client/restored'   , client_coti.restore         , name = "cu_restore"),
        ### ROUTES CLOTH
    path(api + 'cloth/create/'                , ClothCreateView.as_view()     , name = "cloth_create"),
        ### ROUTES ALQUILER
    path(api + 'alquiler/create/'             , AlquilerCreateView.as_view()  , name = "alquiler_create"),
    path(api + 'alquiler/details/all'         , AlquilerListView.as_view()    , name = "alquiler_details_all"),
]
