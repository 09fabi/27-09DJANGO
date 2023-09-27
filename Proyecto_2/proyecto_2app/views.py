from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'webproyecto_2/index.html')


def electronica(request):
    data = {"titulo": "Electronica",
            "foto1": "electronica1.jpg",
            "foto2": "electronica2.jpg",
            "foto3": "electronica3.jpg",
            "producto1": "Mouse Gamer Wireless",
            "producto2": "Led Sobrepuesto",
            "producto3": "Tester"}
    return render(request, 'webproyecto_2/producto.html', data)


def juguete(request):
    data = {"titulo": "Juguetes",
            "foto1": "juguete1.jpg",
            "foto2": "juguete2.jpg",
            "foto3": "juguete3.jpg",
            "producto1": "Juego Didactico",
            "producto2": "Autos",
            "producto3": "Muñeca Grande"}
    return render(request, 'webproyecto_2/producto.html', data)


def ropa(request):
    data = {"titulo": "Ropa",
            "foto1": "prenda1.jpg",
            "foto2": "prenda2.jpg",
            "foto3": "prenda3.jpg",
            "producto1": "Short",
            "producto2": "Polera",
            "producto3": "Pantalon"}
    return render(request, 'webproyecto_2/producto.html', data)
