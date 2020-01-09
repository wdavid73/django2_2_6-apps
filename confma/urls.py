from django.urls import path , include
from django.contrib.auth.decorators import login_required
from .views             import clients , general , cotizacion , client_coti , registration
from .views.clients       import (ClientCreateView , ClientUpdateView  ,ClientDeleteView)
from .views.cotizacion  import (CotiCreateView , CotiUpdateView , CotiListView , CotiDeleteView)
from .views.general     import (ClothCreateView , AlquilerCreateView, AlquilerListView)
from .views.client_coti   import (UCListView)
from .views.registration import (SignUp)

api = 'api/v1/'
urlpatterns = [
	###ROUTES GENERAL###
	path('' , general.home , name = "home"),
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

    ### ROUTES API
	### ROUTES USERS###
    path(api + 'clients/'                     , login_required(clients.home), name = "clients_home"),
    # path(api + 'clients/details/'             , login_required(ClientListView.as_view()), name = "client_details"),
    path(api + 'clients/create/'              , login_required(ClientCreateView.as_view()), name = "client_create"),
    path(api + 'clients/<int:id>/update/'     , login_required(ClientUpdateView.as_view()), name = "client_update"),
    path(api + 'clients/<int:id>/delete/'     , login_required(clients.deletelog), name = "client_deletelog"),
    path(api + 'clients/restore'              , login_required(clients.restoreview), name = "client_restore"),
    path(api + 'clients/restored/<int:id>/'   , login_required(clients.restore), name = "client_restored"),
    path(api + 'clients/search/'              , login_required(clients.search), name = "client_search"),
        ### ROUTES COTIZACION ### 
    path(api + 'cotizacion/'                  , login_required(CotiListView.as_view()),name = "coti_list"),
	path(api + 'cotizacion/create/'           , login_required(CotiCreateView.as_view()),name = "coti_create"),
    path(api + 'cotizacion/<int:id>/update/'  , login_required(CotiUpdateView.as_view()),name = "coti_update"),
    path(api + 'cotizacion/<int:id>/delete/'  , login_required(cotizacion.deletelog),name = "coti_deletelog"),
    path(api + 'cotizacion/restore'           , login_required(cotizacion.restoreview),name = "coti_restore"),
    path(api + 'cotizacion/restored/<int:id>/', login_required(cotizacion.restore),name = "coti_restored"),
        ### ROUTES COTIZACION-CLIENT
    path(api + 'cotizacion-client/<int:id>/'  , login_required(client_coti.create_view), name = "coti_user_create"),
    path(api + 'cotizacion-client/'           , login_required(client_coti.create), name = "cu_create"),
    path(api + 'cotizacion-client/list/'      , login_required(client_coti.list_view), name = "coti_user_list"),
    path(api + 'cotizacion-client/delete/'    , login_required(client_coti.deletelog), name = "cu_deletelog"),
    path(api + 'cotizacion-client/delete/temp', login_required(client_coti.temp), name = "cu_deletelog_temp"),
    path(api + 'cotizacion-client/restore'    , login_required(client_coti.restore_view), name = "cu_restore_view"),
    path(api + 'cotizacion-client/restored' , login_required(client_coti.restore), name = "cu_restore"),
        ### ROUTES CLOTH
    path(api + 'cloth/create/'                , login_required(ClothCreateView.as_view())  , name = "cloth_create"),
        ### ROUTES ALQUILER
    path(api + 'alquiler/create/'             , login_required(AlquilerCreateView.as_view())  , name = "alquiler_create"),
    path(api + 'alquiler/details/all'         , login_required(AlquilerListView.as_view())  , name = "alquiler_details_all"),
]
