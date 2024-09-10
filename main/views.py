from django.shortcuts import render

def landing(request):
    context = {
        'npm' : '2306274983',
        'name': 'Muhammad Fazil Tirtana',
        'class': 'PBP D',
        'products': [
            {
                'name': 'Rexus Bluetooth Gamepad Gladius GX300',
                'price': 409000,
                'image': 'https://i.imgur.com/nVgWSZm.png'
            }.copy() for _ in range(10)
        ],
    }

    return render(request, "landing/index.html", context)
