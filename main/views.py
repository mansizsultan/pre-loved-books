from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Norwegian Wood',
        'author': 'Haruki Murakami',
        'price': 100000,
        'description': 'Edisi ini menggunakan bahasa Inggris karena merupakan barang impor. Hanya dibaca oleh diri sendiri dan selalu tersimpan rapih. Tidak ada kerusakan apapun kecuali kertasnya yang mulai menguning.'
    }

    return render(request, "main.html", context)
