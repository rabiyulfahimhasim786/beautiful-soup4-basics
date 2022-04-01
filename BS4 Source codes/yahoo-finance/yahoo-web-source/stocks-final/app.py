# importing Flask and other modules
#from email.policy import default
from flask import Flask, request, render_template
import yfinance as yf
# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        first_name = request.form.get("fname")
        # getting input with name = lname in HTML form
        last_name = request.form.get("lname")
        return "Your name is "+first_name + last_name
    return render_template("index.html")


@app.route('/info/', methods =["GET", "POST"])
def display_quote():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        text = request.form['text']
    
        symbol = request.args.get('symbol', text)

        quote = yf.Ticker(symbol)

        return quote.info
    return render_template("form.html")

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

@app.route("/data", methods =["GET", "POST"])
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

if __name__=='__main__':
    app.run() 
