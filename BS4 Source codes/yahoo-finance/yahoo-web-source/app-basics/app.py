from flask import Flask, request, redirect, render_template, url_for
from matplotlib.pyplot import xlim
import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from df2gspread import df2gspread as d2g

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

@app.route("/info/<x>", methods =["GET", "POST"])
def datas(x):
    #x = request.form['text']
    symbol = request.args.get('symbol', x)
 
    quote = yf.Ticker(symbol)
    return quote.info

@app.route("/gainers/<url>", methods =["GET", "POST"])
def ygainers(url):
  if request.method == "POST":
        # getting input with name = fname in HTML form
        url = request.form['text']
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'lxml')
        a = soup.find_all('a', attrs={'data-test': 'quoteLink'})
        b = soup.find_all('td', attrs={'aria-label': 'Name'})
        c = soup.find_all('td', attrs={'aria-label': 'Price (Intraday)'})
        d = soup.find_all('td', attrs={'aria-label': 'Change'})
        e = soup.find_all('td', attrs={'aria-label': '% Change'})
        f = soup.find_all('td', attrs={'aria-label': 'Volume'})
        g = soup.find_all('td', attrs={'aria-label': 'Avg Vol (3 month)'})
        h = soup.find_all('td', attrs={'aria-label': 'Market Cap'})
        i = soup.find_all('td', attrs={'aria-label': 'PE Ratio (TTM)'})
  

        a_ = []
        b_ = []
        c_ = []
        d_ = []
        e_ = []
        f_ = []
        g_ = []
        h_ = []
        i_ = []
        for title in a:
            a_.append(title.text.strip())
        for title in b:
            b_.append(title.text.strip())
        for title in c:
            c_.append(title.text.strip())
        for title in d:
            d_.append(title.text.strip())
        for title in e:
            e_.append(title.text.strip())
        for title in f:
            f_.append(title.text.strip())
        for title in g:
            g_.append(title.text.strip())
        for title in h:
            h_.append(title.text.strip())
        for title in i:
            i_.append(title.text.strip())
  # dataframe Name and Age columns
        df = pd.DataFrame({'Symbol': a_, 'Name': b_, 'Price': c_, 'Change': d_, 'Change %': e_, 'Volume': f_, 'Avg volume': g_, 'Market cap': h_, 'Ration': i_,})
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
        creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
        client = gspread.authorize(creds)
        spreadsheet_key = '1NbMXC3uHlK0sxcHCzA7WLjh1gYnEl3D8U3N6VdJ0pYQ'
        wks_name = 'Sheet4'
        cell_of_start_df = 'A2'
        d2g.upload(df,
        spreadsheet_key,
        wks_name,
        credentials=creds,
        col_names=False,
        row_names=False,
        start_cell = cell_of_start_df,
        clean=False)
        return 'ok'
  else:
        return render_template("gainers.html")

@app.route("/ganiers-file/<url>", methods =["GET", "POST"])
def gainersdatas(url):
    if request.method == "POST":
        url = request.form['text']
        # getting input with name = fname in HTML form
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'lxml')
        a = soup.find_all('a', attrs={'data-test': 'quoteLink'})
        b = soup.find_all('td', attrs={'aria-label': 'Name'})
        c = soup.find_all('td', attrs={'aria-label': 'Price (Intraday)'})
        d = soup.find_all('td', attrs={'aria-label': 'Change'})
        e = soup.find_all('td', attrs={'aria-label': '% Change'})
        f = soup.find_all('td', attrs={'aria-label': 'Volume'})
        g = soup.find_all('td', attrs={'aria-label': 'Avg Vol (3 month)'})
        h = soup.find_all('td', attrs={'aria-label': 'Market Cap'})
        i = soup.find_all('td', attrs={'aria-label': 'PE Ratio (TTM)'})
  

        a_ = []
        b_ = []
        c_ = []
        d_ = []
        e_ = []
        f_ = []
        g_ = []
        h_ = []
        i_ = []
        for title in a:
            a_.append(title.text.strip())
        for title in b:
            b_.append(title.text.strip())
        for title in c:
            c_.append(title.text.strip())
        for title in d:
            d_.append(title.text.strip())
        for title in e:
            e_.append(title.text.strip())
        for title in f:
            f_.append(title.text.strip())
        for title in g:
            g_.append(title.text.strip())
        for title in h:
            h_.append(title.text.strip())
        for title in i:
            i_.append(title.text.strip())
  # dataframe Name and Age columns
        df = pd.DataFrame({'Symbol': a_, 'Name': b_, 'Price': c_, 'Change': d_, 'Change %': e_, 'Volume': f_, 'Avg volume': g_, 'Market cap': h_, 'Ration': i_,})
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
        creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
        client = gspread.authorize(creds)
        spreadsheet_key = '1NbMXC3uHlK0sxcHCzA7WLjh1gYnEl3D8U3N6VdJ0pYQ'
        wks_name = 'Sheet4'
        cell_of_start_df = 'A2'
        d2g.upload(df,
        spreadsheet_key,
        wks_name,
        credentials=creds,
        col_names=False,
        row_names=False,
        start_cell = cell_of_start_df,
        clean=False)
        return 'ok'
    else:
        return render_template("gainers.html")

if __name__ == '__main__':
   app.run(debug = True)