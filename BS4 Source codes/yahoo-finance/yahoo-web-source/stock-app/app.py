from flask import Flask, request, redirect, render_template, url_for
from matplotlib.pyplot import xlim
import yfinance as yf
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return 'Welcome %s!' % name


@app.route('/info/', methods =["GET", "POST"])
def display_quote():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        x = request.form['text']
    
        symbol = request.args.get('symbol', x)

        quote = yf.Ticker(symbol)

        return quote.info
        #return redirect(url_for("datas",  x=x))
    else:
        return render_template("form.html")

@app.route("/data/<x>")
def datas(x):
    #x = request.form['text']
    symbol = request.args.get('symbol', x)
 
    quote = yf.Ticker(symbol)
    return quote.info


@app.route("/history", methods =["GET", "POST"])
def display_history():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        text = request.form['text']

        symbol = request.args.get('symbol', text)
        period = request.args.get('period', default="1y")
        interval = request.args.get('interval', default="1mo")        
        quote = yf.Ticker(symbol)   
        hist = quote.history(period=period, interval=interval)
        data = hist.to_json()
        return data
    return render_template("history.html")

@app.route("/historydata/<x>")
def history(x):
    #x = request.form['text']
    symbol = request.args.get('symbol', x)
    period = request.args.get('period', default="1y")
    interval = request.args.get('interval', default="1mo")        
    quote = yf.Ticker(symbol)   
    hist = quote.history(period=period, interval=interval)
    data = hist.to_json()
    return data

@app.route("/stockdata", methods =["GET", "POST"])
def display_data():
     if request.method == "POST":
        # getting input with name = fname in HTML form
        text = request.form['text']
        symbol = request.args.get('symbol', text)
        quote = yf.Ticker(symbol)
#start = datetime.datetime(2018,1,1)
#end = datetime.datetime(2019,7,17)
#data = yf.download(stocks, start=start, end=end)
   # a = quote.info['shortName']
    #b = quote.info['symbol']
   # c = quote.info['currentPrice']
   # d = quote.info['profitMargins']
   # e = quote.info['volume']
   # f = quote.info['averageVolume']
   # g = quote.info['marketCap']
    #h = quote.info['trailingPE']
    #i = (a, b, c, d, e, f, g, h)
        return {
   "a": quote.info['shortName'],
   "b": quote.info['symbol'],
   "c": quote.info['currentPrice'],
   "d": quote.info['profitMargins'],
   "e": quote.info['volume'],
   "f": quote.info['averageVolume'],
   "g": quote.info['marketCap'],
    }
     return render_template("data.html")

@app.route("/stock/<x>")
def invidual(x):
    #x = request.form['text']
    #text = request.form['text']
    symbol = request.args.get('symbol', x)
    quote = yf.Ticker(symbol)
    return {
   "a": quote.info['shortName'],
   "b": quote.info['symbol'],
   "c": quote.info['currentPrice'],
   "d": quote.info['profitMargins'],
   "e": quote.info['volume'],
   "f": quote.info['averageVolume'],
   "g": quote.info['marketCap'],
    }

if __name__ == '__main__':
   app.run(debug = True)