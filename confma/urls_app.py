from django.contrib.auth.decorators import login_required
from django.urls import path, include

from confma import static_methods
from confma.views import clients, cotizacion, client_coti, cloth, rental
from confma.views.registration import SignUp

api = 'api/v2/'
app_name = "confma"
urlpatterns = [
    path('', static_methods.HomePage, name="homepage"),
    # LOGIN , SIGNUP , LOGOUT
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name='signup'),

    # ROUTES API
    # ROUTES USERS
    path(api + 'clients/', login_required(clients.ListAllClients), name="list_all_clients"),
    path(api + 'clients/create/', login_required(clients.CreateClient.as_view()), name="create_clients"),
    path(api + 'clients/<int:id>/update/', login_required(clients.UpdateClient.as_view()), name="update_clients"),
    path(api + 'clients/<int:_id>/delete/', login_required(clients.DeleteClient), name="delete_clients"),
    path(api + 'clients/restore', login_required(clients.RestoreClientView), name="restore_clients_view"),
    path(api + 'clients/restored/<int:id>/', login_required(clients.RestoreClient), name="client_restored"),
    path(api + 'clients/search/', login_required(clients.FindClient), name="find_client"),
    # ROUTES COTIZACION
    path(api + 'cotizacion/'
         , login_required(cotizacion.ListAllCotizacionByCloth.as_view())
         , name="list_of_all_cotizaciones"),

    path(api + 'cotizacion/create/'
         , login_required(cotizacion.CreateCotizacion.as_view())
         , name="create_cotizaciones"),

    path(api + 'cotizacion/<int:id>/update/'
         , login_required(cotizacion.UpdateCotizacionById.as_view())
         , name="update_cotizaciones"),

    path(api + 'cotizacion/<int:id>/delete/'
         , login_required(cotizacion.DeleteCotizacion)
         , name="delete_cotizaciones"),

    path(api + 'cotizacion/restore'
         , login_required(cotizacion.RestoreCotizacionView)
         , name="restore_cotizaciones_view"),

    path(api + 'cotizacion/restored/<int:id>/'
         , login_required(cotizacion.RestoreCotizacionById)
         , name="cotizacion_restored"),

    # ROUTES COTIZACION-CLIENT
    path(api + 'cotizacion-client/<int:id_>/', login_required(client_coti.ClientCotizacionView),
         name="create_client_cotizacion_view"),

    path(api + 'cotizacion-client/', login_required(client_coti.CreateClientCotizacion.as_view()),
         name="create_client_cotizacion"),

    path(api + 'cotizacion-client/list/', login_required(client_coti.ListOfAllClientsAndCotizacion.as_view()),
         name="list_of_all_cotizacion_client"),

    path(api + 'cotizacion-client/delete/', login_required(client_coti.DeleteClientCotizacion),
         name="delete_cotizacion_client"),

    path(api + 'cotizacion-client/restore', login_required(client_coti.RestoreClientCotizacionView),
         name="restore_client_cotizacion_view"),

    path(api + 'cotizacion-client/restored', login_required(client_coti.RestoreClientCotizacion),
         name="client_cotizacion_restored"),

    # ROUTES CLOTH
    path(api + 'cloth/create/', login_required(cloth.ClothCreate.as_view()), name="create_cloth"),
    path(api + 'cloth/photo/', login_required(cloth.UploadPhotoFashion), name="upload_photo_to_cloth"),
    path(api + 'cloth/list/', login_required(cloth.ListOfAllCloth.as_view()), name="list_all_cloth"),
    path(api + 'cloth/details/<int:_id>', login_required(cloth.DetailsCloth), name="details_of_cloth"),
    path(api + 'cloth-cotizacion/find/', login_required(cotizacion.FindClothCotizacion), name="find_cloth_cotizacion"),
    path(api + 'cloth-rental/find/', login_required(rental.FindClothRental), name="find_of_cloth_rental"),

    # ROUTES RENTAL
    path(api + 'rental/create/', login_required(rental.CreateRental.as_view()), name="create_rental"),
    path(api + 'rental/details/all', login_required(rental.ListOfAllRental.as_view()), name="list_of_all_rental"),
    path(api + 'rental/refund/<int:_id>', login_required(rental.RefundRental), name="rental_refund"),

    path(api + 'error', static_methods.PossibleError, name="posible_error"),

]
# confma/ login/ [name='login']
# confma/ logout/ [name='logout']
# confma/ password_change/ [name='password_change']
# confma/ password_change/done/ [name='password_change_done']
# confma/ password_reset/ [name='password_reset']
# confma/ password_reset/done/ [name='password_reset_done']
# confma/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# confma/ reset/done/ [name='password_reset_complete']
