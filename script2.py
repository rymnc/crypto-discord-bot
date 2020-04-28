import discord
import json
import urllib.request
import config as cfg 	

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('crypto'):
		if message.content == "crypto help":
			embed = discord.Embed(title="Help",description="some useful commands")
			embed.add_field(name="crypto btc", value="returns the price of Bitcoin")
			embed.add_field(name="crypto eth", value="returns the price of Ethereum")
			embed.add_field(name="crypto xrp", value="returns the price of Ripple")
			embed.add_field(name="crypto xlm", value="returns the price of Stellar")
			embed.add_field(name="crypto xmr", value="returns the price of Monero")
			embed.add_field(name="crypto rep", value="returns the price of Augur")
			embed.add_field(name="crypto dash", value="returns the price of Dash")
			await message.channel.send(content=None, embed=embed)
		elif message.content == "crypto btc":
			url = "https://api.nomics.com/v1/currencies/ticker?key=09a28f4136aef7b18df8880d88838464&ids=BTC&interval=1d,30d&convert=USD"
			data = json.loads(urllib.request.urlopen(url).read())
			
			await message.channel.send('Rank: ' + data[0]['rank']+ '\nName: ' + data[0]['name'] + '\nSymbol: ' + data[0]['symbol'] +'\nPrice: ' +data[0]['price'] + ' Dollars')
		elif message.content == "crypto eth":
			url = "https://api.nomics.com/v1/currencies/ticker?key=09a28f4136aef7b18df8880d88838464&ids=ETH&interval=1d,30d&convert=USD"
			data = json.loads(urllib.request.urlopen(url).read())
			
			await message.channel.send('Rank: ' + data[0]['rank']+ '\nName: ' + data[0]['name'] + '\nSymbol: ' + data[0]['symbol'] +'\nPrice: ' +data[0]['price'] + ' Dollars')
		elif message.content == "crypto xrp":
			url = "https://api.nomics.com/v1/currencies/ticker?key=09a28f4136aef7b18df8880d88838464&ids=XRP&interval=1d,30d&convert=USD"
			data = json.loads(urllib.request.urlopen(url).read())
			
			await message.channel.send('Rank: ' + data[0]['rank']+ '\nName: ' + data[0]['name'] + '\nSymbol: ' + data[0]['symbol'] +'\nPrice: ' +data[0]['price'] + ' Dollars')
		elif message.content == "crypto xlm":
			url = "https://api.nomics.com/v1/currencies/ticker?key=09a28f4136aef7b18df8880d88838464&ids=XLM&interval=1d,30d&convert=USD"
			data = json.loads(urllib.request.urlopen(url).read())
			
			await message.channel.send('Rank: ' + data[0]['rank']+ '\nName: ' + data[0]['name'] + '\nSymbol: ' + data[0]['symbol'] +'\nPrice: ' +data[0]['price'] + ' Dollars')
		elif message.content == "crypto xmr":
			url = "https://api.nomics.com/v1/currencies/ticker?key=09a28f4136aef7b18df8880d88838464&ids=XMR&interval=1d,30d&convert=USD"
			data = json.loads(urllib.request.urlopen(url).read())
			
			await message.channel.send('Rank: ' + data[0]['rank']+ '\nName: ' + data[0]['name'] + '\nSymbol: ' + data[0]['symbol'] +'\nPrice: ' +data[0]['price'] + ' Dollars')
		elif message.content == "crypto rep":
			url = "https://api.nomics.com/v1/currencies/ticker?key=09a28f4136aef7b18df8880d88838464&ids=REP&interval=1d,30d&convert=USD"
			data = json.loads(urllib.request.urlopen(url).read())
			
			await message.channel.send('Rank: ' + data[0]['rank']+ '\nName: ' + data[0]['name'] + '\nSymbol: ' + data[0]['symbol'] +'\nPrice: ' +data[0]['price'] + ' Dollars')
		elif message.content == "crypto dash":
			url = "https://api.nomics.com/v1/currencies/ticker?key=09a28f4136aef7b18df8880d88838464&ids=DASH&interval=1d,30d&convert=USD"
			data = json.loads(urllib.request.urlopen(url).read())
			
			await message.channel.send('Rank: ' + data[0]['rank']+ '\nName: ' + data[0]['name'] + '\nSymbol: ' + data[0]['symbol'] +'\nPrice: ' +data[0]['price'] + ' Dollars')
		else:
			await message.channel.send('Unknown Command,\nPlease refer to "crypto help" for more information!')	

client.run(cfg.myToken["token"])