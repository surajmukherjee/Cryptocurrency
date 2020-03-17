import requests


def coin_symbol_data(request):

    data = requests.get('https://api.coingecko.com/api/v3/coins/list')
    if request.method == "POST":
        symbol = request.POST['symbol']
        for dictionary in data.json():
            if dictionary.get('symbol') == symbol:
                form = CoinForm(request.POST)
                if form.is_valid():
                    f = form.save(commit=False)
                    f.symbol = dictionary['symbol']
                    f.name = dictionary['name']
                    f.save()
    return render(request, "coin_symbol.html")