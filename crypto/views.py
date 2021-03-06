from django.shortcuts import render

def home(request):
	import requests
	import json
	# GrabCrypto Graph
	Price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
	Price = json.loads(Price_request.content)
	# GrabCrypto News
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request, 'home.html', {'api': api, 'Price': Price})

def prices(request):
	if request.method == 'POST':
		import requests
		import json  
		quote = request.POST['quote']
		quote = quote.upper()
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="  + quote + "&tsyms=USD")
		crypto = json.loads(crypto_request.content)
		return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})
	else:
		notfound = "Enter a crypto currency symbol into the search bar..."
		return render(request, 'prices.html', {'notfound': notfound})

