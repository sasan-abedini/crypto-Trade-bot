import ccxt
import time

# وارد کردن اطلاعات API
api_key = 'YOUR_API_KEY'
secret_key = 'YOUR_SECRET_KEY'

# اتصال به صرافی
exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': secret_key,
})

# تابع برای گرفتن قیمت کنونی
def get_current_price(symbol):
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

# تابع برای خرید
def buy(symbol, amount):
    order = exchange.create_market_buy_order(symbol, amount)
    return order

# تابع برای فروش
def sell(symbol, amount):
    order = exchange.create_market_sell_order(symbol, amount)
    return order

# نمونه‌ای از یک استراتژی ساده
def strategy(symbol, amount, buy_price, sell_price):
    while True:
        current_price = get_current_price(symbol)
        if current_price <= buy_price:
            print("خرید در قیمت: ", current_price)
            buy(symbol, amount)
        elif current_price >= sell_price:
            print("فروش در قیمت: ", current_price)
            sell(symbol, amount)
        time.sleep(5)  # توقف به مدت 5 ثانیه

# اجرای استراتژی
symbol = 'BTC/USDT'
amount = 0.001  # مقدار خرید یا فروش
buy_price = 30000  # قیمت خرید
sell_price = 35000  # قیمت فروش

strategy(symbol, amount, buy_price, sell_price)
