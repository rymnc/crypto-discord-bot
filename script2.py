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
			embed.add_field(name="crypto btc", value="Returns The Price of Bitcoin.")
			embed.add_field(name="crypto eth", value="Returns The Price of Ethereum")
			embed.add_field(name="crypto xrp", value="Returns The Price of Ripple")
			embed.add_field(name="crypto xlm", value="Returns The Price of Stellar")
			embed.add_field(name="crypto xmr", value="Returns The Price of Monero")
			embed.add_field(name="crypto rep", value="Returns The Price of Augur")
			embed.add_field(name="crypto dash", value="Returns The Price of Dash")
			embed.add_field(name="crypto top10 volume", value="Returns The Top 10 Cryptocurrencies(Volume)")
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
		elif message.content == "crypto top10 volume":
			await message.channel.send('Please wait for Computation to occur!')
			url = "https://api.nomics.com/v1/currencies/ticker?key=09a28f4136aef7b18df8880d88838464"
			data=json.loads(urllib.request.urlopen(url).read())
			top_10_names = [x["name"] for x in data[:10]]
			top_10_price = [x["price"] for x in data[:10]]
			embed = discord.Embed(title="Ranking of Cryptocurrencies(Volume)",description="")
			embed.add_field(name="1.", value=top_10_names[0]+"\nValue: "+top_10_price[0]+"$")
			embed.add_field(name="2.", value=top_10_names[1]+"\nValue: "+top_10_price[1]+"$")
			embed.add_field(name="3.", value=top_10_names[2]+"\nValue: "+top_10_price[2]+"$")
			embed.add_field(name="4.", value=top_10_names[3]+"\nValue: "+top_10_price[3]+"$")
			embed.add_field(name="5.", value=top_10_names[4]+"\nValue: "+top_10_price[4]+"$")
			embed.add_field(name="6.", value=top_10_names[5]+"\nValue: "+top_10_price[5]+"$")
			embed.add_field(name="7.", value=top_10_names[6]+"\nValue: "+top_10_price[6]+"$")
			embed.add_field(name="8.", value=top_10_names[7]+"\nValue: "+top_10_price[7]+"$")
			embed.add_field(name="9.", value=top_10_names[8]+"\nValue: "+top_10_price[8]+"$")
			embed.add_field(name="10.", value=top_10_names[9]+"\nValue: "+top_10_price[9]+"$")
			await message.channel.send(content=None, embed=embed)

		else:
			await message.channel.send('Unknown Command,\nPlease refer to "crypto help" for more information!')	

client.run(cfg.myToken["token"])