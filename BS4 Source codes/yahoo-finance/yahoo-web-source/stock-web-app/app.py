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
import requests
import schedule
import pandas as pd
import time
from fake_useragent import UserAgent

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

@app.route("/ygainers/page-1", methods =["GET", "POST"])
def ygainers():
  if request.method == "POST":
        # getting input with name = fname in HTML form
        ua = UserAgent()
        url = request.form['text']
        #url = 'https://finance.yahoo.com/gainers?count=100&offset=0'
        headers = {'User-Agent': ua.random }
        html = requests.get(url, headers=headers).content
        soup = BeautifulSoup(html, 'lxml')
        #html = requests.get(url).content
        #soup = BeautifulSoup(html, 'lxml')
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
        spreadsheet_key = '1m-mrYAqoUvm5OTN1dq8rRr3sLtDuEh8bxVzQCYi2q44'
        wks_name = 'Sheet1'
        cell_of_start_df = 'A2'
        d2g.upload(df,
        spreadsheet_key,
        wks_name,
        credentials=creds,
        col_names=False,
        row_names=False,
        start_cell = cell_of_start_df,
        clean=False)
        schedule.every(15).minutes.do(ygainers)
        #requests.get("https://stocks.desss-portfolio.com/yahoo/yahoo_gainers")
        while 1:
            schedule.run_pending()
            time.sleep(1)
        return 'ok'
  else:
        return render_template("gainers.html")

@app.route("/ygainers/page-2", methods =["GET", "POST"])
def ygainerspage():
  if request.method == "POST":
                # getting input with name = fname in HTML form
        ua = UserAgent()
        url = request.form['text']
        #url = 'https://finance.yahoo.com/gainers?count=100&offset=0'
        headers = {'User-Agent': ua.random }
        html = requests.get(url, headers=headers).content
        soup = BeautifulSoup(html, 'lxml')
        #html = requests.get(url).content
        #soup = BeautifulSoup(html, 'lxml')
        aa = soup.find_all('a', attrs={'data-test': 'quoteLink'})
        ba = soup.find_all('td', attrs={'aria-label': 'Name'})
        ca = soup.find_all('td', attrs={'aria-label': 'Price (Intraday)'})
        da = soup.find_all('td', attrs={'aria-label': 'Change'})
        ea = soup.find_all('td', attrs={'aria-label': '% Change'})
        fa = soup.find_all('td', attrs={'aria-label': 'Volume'})
        ga = soup.find_all('td', attrs={'aria-label': 'Avg Vol (3 month)'})
        ha = soup.find_all('td', attrs={'aria-label': 'Market Cap'})
        ia = soup.find_all('td', attrs={'aria-label': 'PE Ratio (TTM)'})
  

        aa_ = []
        ba_ = []
        ca_ = []
        da_ = []
        ea_ = []
        fa_ = []
        ga_ = []
        ha_ = []
        ia_ = []
        for title in aa:
            aa_.append(title.text.strip())
        for title in ba:
            ba_.append(title.text.strip())
        for title in ca:
            ca_.append(title.text.strip())
        for title in da:
            da_.append(title.text.strip())
        for title in ea:
            ea_.append(title.text.strip())
        for title in fa:
            fa_.append(title.text.strip())
        for title in ga:
            ga_.append(title.text.strip())
        for title in ha:
            ha_.append(title.text.strip())
        for title in ia:
            ia_.append(title.text.strip())
  # dataframe Name and Age columns
        df = pd.DataFrame({'Symbol': aa_, 'Name': ba_, 'Price': ca_, 'Change': da_, 'Change %': ea_, 'Volume': fa_, 'Avg volume': ga_, 'Market cap': ha_, 'Ration': ia_,})
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
        creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
        client = gspread.authorize(creds)
        spreadsheet_key = '1m-mrYAqoUvm5OTN1dq8rRr3sLtDuEh8bxVzQCYi2q44'
        wks_name = 'Sheet2'
        cell_of_start_df = 'A2'
        d2g.upload(df,
        spreadsheet_key,
        wks_name,
        credentials=creds,
        col_names=False,
        row_names=False,
        start_cell = cell_of_start_df,
        clean=False)
        schedule.every(20).minutes.do(ygainerspage)
        requests.get("https://stocks.desss-portfolio.com/yahoo/yahoo_gainers")
        while 1:
            schedule.run_pending()
            time.sleep(1)
        return 'ok'
  else:
        return render_template("gainers2.html")

@app.route("/ygainers/page-3", methods =["GET", "POST"])
def gainerspage():
  if request.method == "POST":
         # getting input with name = fname in HTML form
        ua = UserAgent()
        url = request.form['text']
        #url = 'https://finance.yahoo.com/gainers?count=100&offset=0'
        headers = {'User-Agent': ua.random }
        html = requests.get(url, headers=headers).content
        soup = BeautifulSoup(html, 'lxml')
        #html = requests.get(url).content
        #soup = BeautifulSoup(html, 'lxml')
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
        spreadsheet_key = '1m-mrYAqoUvm5OTN1dq8rRr3sLtDuEh8bxVzQCYi2q44'
        wks_name = 'Sheet3'
        cell_of_start_df = 'A2'
        d2g.upload(df,
        spreadsheet_key,
        wks_name,
        credentials=creds,
        col_names=False,
        row_names=False,
        start_cell = cell_of_start_df,
        clean=False)
        schedule.every(25).minutes.do(gainerspage)
        #requests.get("https://stocks.desss-portfolio.com/yahoo/yahoo_gainers")
        while 1:
            schedule.run_pending()
            time.sleep(1)
        return 'ok'
  else:
        return render_template("gainers3.html")


@app.route("/ganiers-file/<url>", methods =["GET", "POST"])
def gainersdatas():
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