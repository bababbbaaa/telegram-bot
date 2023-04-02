from pycoingecko import CoinGeckoAPI
from moralis import evm_api
import keys
import items
import requests
import random
from datetime import datetime


coingecko = CoinGeckoAPI()
cg = coingecko.get_price(ids=',x7r,x7dao,x7101,x7102,x7103,x7104,x7105', vs_currencies='usd',
                         include_24hr_change='true', include_24hr_vol='true')

# noinspection PyTypeChecker
def get_liquidity(pair):
    amount = evm_api.defi.get_pair_reserves(api_key=keys.moralis, params={"chain": "eth", "pair_address": pair})
    return amount

def get_today():
    currentday = str(datetime.now().day)
    currentmonth = str(datetime.now().month)
    url = f'http://history.muffinlabs.com/date/{currentmonth}/{currentday}'
    response = requests.get(url)
    data = response.json()
    return data

def get_nft(slug):
    slug = slug
    headers = {"X-API-KEY": keys.os}
    url = "https://api.opensea.io/api/v1/collection/" + slug
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def get_gas(chain):
    if chain == "eth":
        url = 'https://api.etherscan.io/api?module=gastracker&action=gasoracle' + keys.ether
        response = requests.get(url)
        data = response.json()
        return data
    if chain == "poly":
        url = 'https://api.polygonscan.com/api?module=gastracker&action=gasoracle' + keys.poly
        response = requests.get(url)
        data = response.json()
        return data
    if chain == "bsc":
        url = 'https://api.bscscan.com/api?module=gastracker&action=gasoracle' + keys.bsc
        response = requests.get(url)
        data = response.json()
        return data

def get_holders(token):
    url = 'https://api.ethplorer.io/getTokenInfo/' + token + keys.ethplorer
    response = requests.get(url)
    data = response.json()
    amount = data["holdersCount"]
    return amount

def get_quote():
    quoteresponse = requests.get('https://type.fit/api/quotes')
    quotedata = quoteresponse.json()
    quoteraw = (random.choice(quotedata))
    quote = quoteraw["text"] + quoteraw["author"]
    quote = f'`"{quoteraw["text"]}"\n\n-{quoteraw["author"]}`'
    return quote

def get_holders_nft_eth(nft):
    url = 'https://api.blockspan.com/v1/collections/contract/' + nft + '?chain=eth-main'
    response = requests.get(url, headers={"accept": "application/json", "X-API-KEY": keys.blockspan})
    data = response.json()
    amount = data["total_tokens"]
    return amount

def get_holders_nft_arb(nft):
    url = 'https://api.blockspan.com/v1/collections/contract/' + nft + '?chain=arbitrum'
    response = requests.get(url, headers={"accept": "application/json", "X-API-KEY": keys.blockspan})
    data = response.json()
    amount = data["total_tokens"]
    return amount

def get_holders_nft_poly(nft):
    url = 'https://api.blockspan.com/v1/collections/contract/' + items.dexca + '?chain=poly-main'
    response = requests.get(url, headers={"accept": "application/json", "X-API-KEY": keys.blockspan})
    data = response.json()
    amount = data["total_tokens"]
    return amount

def get_holders_nft_opti(nft):
    url = 'https://api.blockspan.com/v1/collections/contract/' + nft + '?chain=optimism-main'
    response = requests.get(url, headers={"accept": "application/json", "X-API-KEY": keys.blockspan})
    data = response.json()
    amount = data["total_tokens"]
    return amount

def get_native_price(token):
    if token == "eth":
        url = 'https://api.etherscan.io/api?module=stats&action=ethprice&' + keys.ether
        response = requests.get(url)
        data = response.json()
        value = float(data["result"]["ethusd"])
        return value
    if token == "bnb":
        url = 'https://api.bscscan.com/api?module=stats&action=bnbprice&' + keys.bsc
        response = requests.get(url)
        data = response.json()
        value = float(data["result"]["ethusd"])
        return value
    if token == "matic":
        url = 'https://api.polygonscan.com/api?module=stats&action=maticprice&' + keys.poly
        response = requests.get(url)
        data = response.json()
        value = float(data["result"]["ethusd"])
        return value

def get_token_balance(wallet, chain, token):
    if chain == "eth":
        url = 'https://api.etherscan.io/' \
              'api?module=account&action=tokenbalance&contractaddress='
        key = keys.ether
        response = requests.get(url + token + '&address=' + wallet + '&tag=latest' + key)
        data = response.json()
        amount = int(data["result"][:-18])
        return amount
    if chain == "bsc":
        url = 'https://api.bscscan.com/' \
              'api?module=account&action=tokenbalance&contractaddress='
        key = keys.bsc
        response = requests.get(url + token + '&address=' + wallet + '&tag=latest' + key)
        data = response.json()
        amount = int(data["result"][:-18])
        return amount
    if chain == "opti":
        url = 'https://api-optimistic.etherscan.io/' \
              'api?module=account&action=tokenbalance&contractaddress='
        key = keys.opti
        response = requests.get(url + token + '&address=' + wallet + '&tag=latest' + key)
        data = response.json()
        amount = int(data["result"][:-18])
        return amount
    if chain == "poly":
        url = 'https://api.polygonscan.com/' \
              'api?module=account&action=tokenbalance&contractaddress='
        key = keys.poly
        response = requests.get(url + token + '&address=' + wallet + '&tag=latest' + key)
        data = response.json()
        amount = int(data["result"][:-18])
        return amount
    if chain == "arb":
        url = 'https://api.arbiscan.io/' \
              'api?module=account&action=tokenbalance&contractaddress='
        key = keys.arb
        response = requests.get(url + token + '&address=' + wallet + '&tag=latest' + key)
        data = response.json()
        amount = int(data["result"][:-18])
        return amount

def get_balance(wallet, chain):
    if chain == "opti":
        key = keys.opti
        link = 'https://api-optimistic.etherscan.io/' \
               'api?module=account&action=balancemulti&address='
        response = requests.get(link + wallet + '&tag=latest' + key)
        data = response.json()
        amountraw = float(data["result"][0]["balance"])
        amount = str(amountraw / 10 ** 18)
        return amount
    if chain == "eth":
        key = keys.ether
        link = 'https://api.etherscan.io/' \
               'api?module=account&action=balancemulti&address='
        response = requests.get(link + wallet + '&tag=latest' + key)
        data = response.json()
        amountraw = float(data["result"][0]["balance"])
        amount = str(amountraw / 10 ** 18)
        return amount
    if chain == "arb":
        key = keys.arb
        link = 'https://api.arbiscan.io/' \
               'api?module=account&action=balancemulti&address='
        response = requests.get(link + wallet + '&tag=latest' + key)
        data = response.json()
        amountraw = float(data["result"][0]["balance"])
        amount = str(amountraw / 10 ** 18)
        return amount
    if chain == "bsc":
        key = keys.bsc
        link = "https://api.bscscan.com/" \
               "api?module=account&action=balancemulti&address="
        response = requests.get(link + wallet + '&tag=latest' + key)
        data = response.json()
        amountraw = float(data["result"][0]["balance"])
        amount = str(amountraw / 10 ** 18)
        return amount
    if chain == "poly":
        key = keys.poly
        link = "https://api.polygonscan.com/" \
               "api?module=account&action=balancemulti&address="
        response = requests.get(link + wallet + '&tag=latest' + key)
        data = response.json()
        amountraw = float(data["result"][0]["balance"])
        amount = str(amountraw / 10 ** 18)
        return amount
