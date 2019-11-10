#Users 

def create(request):
    form = UserForm(request.GET)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            #ingreso a la base de datos
            print(form.cleaned_data)
            User.objects.create(**form.cleaned_data)
            # form = UserForm()
            return redirect('../')
        else:
            print(form.errors)
            # error = form.errors

    context = {
        'form' : form
    }
    return render(request , "users/create.html" , context)


def delete(request , id):
    obj = get_object_or_404(User , id = id)
    if request.method == "POST":
        obj.delete()
        print("listo pa borrar")
        return redirect('../../')
    context = {
        'user' : obj
    }

    return render(request , "users/delete.html" , context)


##Cotizacion
def create(request):
    form = CotizacionFormModel(request.GET)
    if request.method == "POST":
        form = CotizacionFormModel(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Cotizacion.objects.create(**form.cleaned_data)
            return redirect('../')
        else:
            print(form.errors)

    context = {
        'form' : form
    }
    return render(request, "cotizacion/create.html" , context)

def delete(request , id):
    obj = get_object_or_404(Cotizacion , id = id)
    if request.method == "POST":
        obj.delete()
        print("listo pa borrar")
        return redirect('../../')
    context = {
        'c' : obj
    }

    return render(request , "cotizacion/delete.html" , context)


