from django.shortcuts import render

def agenda(request):
    listadoclientes = [
        {
            'Nombre': 'Alberto',
            'Apellido': 'Guimenez'
        },
        {
            'Nombre': 'Ana',
            'Apellido': 'Martin'
        },
        {
            'Nombre': 'Julian',
            'Apellido': 'Garcia'
        },
        {
            'Nombre': 'Maria',
            'Apellido': 'Fernandez'
        },
        {
            'Nombre': 'Teresa',
            'Apellido': 'Gomez'
        }
    ]

    context = {
        'listado_clientes' : listadoclientes
    }
    return render(request,'clientes/clientes.html', context)