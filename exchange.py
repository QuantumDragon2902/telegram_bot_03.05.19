import requests
import DataBase

global db
db = DataBase.DB()

def get_btc_usd():
  url = 'https://api.exmo.com/v1/ticker'
  response = requests.get(url).json()
  message = 'Buy: ' + str(response['BTC_USD']['buy_price']) + ' $' +'\n' + 'Sell: ' + str(response['BTC_USD']['sell_price']) + ' $' +'\n' + 'High: ' + str(response['BTC_USD']['high']) + ' $' +'\n'
  global db
  db.insert_data('Dollar', response['BTC_USD']['buy_price'], response['BTC_USD']['sell_price'], response['BTC_USD']['high'])

  return message


def get_btc_eur():
  url = 'https://api.exmo.com/v1/ticker'
  response = requests.get(url).json()
  message = 'Buy: ' + str(response['BTC_EUR']['buy_price']) + ' €' +'\n' + 'Sell: ' + str(response['BTC_EUR']['sell_price']) + ' €' +'\n' + 'High: ' + str(response['BTC_EUR']['high']) + ' €' +'\n'
  global db
  db.insert_data('Euro', response['BTC_EUR']['buy_price'], response['BTC_EUR']['sell_price'], response['BTC_EUR']['high'])

  return message

def get_btc_rub():
  url = 'https://api.exmo.com/v1/ticker'
  response = requests.get(url).json()
  message = 'Buy: ' + str(response['BTC_RUB']['buy_price']) + ' ₽' +'\n' + 'Sell: ' + str(response['BTC_RUB']['sell_price']) + ' ₽' +'\n' + 'High: ' + str(response['BTC_RUB']['high']) + ' ₽' +'\n'

  return message
