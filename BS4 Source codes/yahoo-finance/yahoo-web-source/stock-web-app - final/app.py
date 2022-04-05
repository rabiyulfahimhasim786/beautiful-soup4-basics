import cffi
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

@app.route('/')
def home_page():
   return 'Welcome to desss!'

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
        return render_template("forms.html")

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
        ab = soup.find_all('a', attrs={'data-test': 'quoteLink'})
        bb = soup.find_all('td', attrs={'aria-label': 'Name'})
        cb = soup.find_all('td', attrs={'aria-label': 'Price (Intraday)'})
        db = soup.find_all('td', attrs={'aria-label': 'Change'})
        eb = soup.find_all('td', attrs={'aria-label': '% Change'})
        fb = soup.find_all('td', attrs={'aria-label': 'Volume'})
        gb = soup.find_all('td', attrs={'aria-label': 'Avg Vol (3 month)'})
        hb = soup.find_all('td', attrs={'aria-label': 'Market Cap'})
        ib = soup.find_all('td', attrs={'aria-label': 'PE Ratio (TTM)'})
  

        ab_ = []
        bb_ = []
        cb_ = []
        db_ = []
        eb_ = []
        fb_ = []
        gb_ = []
        hb_ = []
        ib_ = []
        for title in ab:
            ab_.append(title.text.strip())
        for title in bb:
            bb_.append(title.text.strip())
        for title in cb:
            cb_.append(title.text.strip())
        for title in db:
            db_.append(title.text.strip())
        for title in eb:
            eb_.append(title.text.strip())
        for title in fb:
            fb_.append(title.text.strip())
        for title in gb:
            gb_.append(title.text.strip())
        for title in hb:
            hb_.append(title.text.strip())
        for title in ib:
            ib_.append(title.text.strip())
  # dataframe Name and Age columns
        df = pd.DataFrame({'Symbol': ab_, 'Name': bb_, 'Price': cb_, 'Change': db_, 'Change %': eb_, 'Volume': fb_, 'Avg volume': gb_, 'Market cap': hb_, 'Ration': ib_,})
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

@app.route("/ylosers/page-1", methods =["GET", "POST"])
def ylosers():
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
        ad = soup.find_all('a', attrs={'data-test': 'quoteLink'})
        bd = soup.find_all('td', attrs={'aria-label': 'Name'})
        cd = soup.find_all('td', attrs={'aria-label': 'Price (Intraday)'})
        dd = soup.find_all('td', attrs={'aria-label': 'Change'})
        ed = soup.find_all('td', attrs={'aria-label': '% Change'})
        fd = soup.find_all('td', attrs={'aria-label': 'Volume'})
        gd = soup.find_all('td', attrs={'aria-label': 'Avg Vol (3 month)'})
        hd = soup.find_all('td', attrs={'aria-label': 'Market Cap'})
        id = soup.find_all('td', attrs={'aria-label': 'PE Ratio (TTM)'})
  

        ad_ = []
        bd_ = []
        cd_ = []
        dd_ = []
        ed_ = []
        fd_ = []
        gd_ = []
        hd_ = []
        id_ = []
        for title in ad:
            ad_.append(title.text.strip())
        for title in bd:
            bd_.append(title.text.strip())
        for title in cd:
            cd_.append(title.text.strip())
        for title in dd:
            dd_.append(title.text.strip())
        for title in ed:
            ed_.append(title.text.strip())
        for title in fd:
            fd_.append(title.text.strip())
        for title in gd:
            gd_.append(title.text.strip())
        for title in hd:
            hd_.append(title.text.strip())
        for title in id:
            id_.append(title.text.strip())
  # dataframe Name and Age columns
        df = pd.DataFrame({'Symbol': ad_, 'Name': bd_, 'Price': cd_, 'Change': dd_, 'Change %': ed_, 'Volume': fd_, 'Avg volume': gd_, 'Market cap': hd_, 'Ration': id_,})
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
        creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
        client = gspread.authorize(creds)
        spreadsheet_key = '1X7APg9YH6ndu2lEhYDjMrWGwE1mQZlIh3G-XbzV_8zA'
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
        schedule.every(35).minutes.do(ylosers)
        requests.get("https://stocks.desss-portfolio.com/yahoo/yahoo_losers")
        while 1:
            schedule.run_pending()
            time.sleep(1)
        return 'ok'
  else:
        return render_template("losers.html")

@app.route("/ylosers/page-2", methods =["GET", "POST"])
def yloserspage():
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
        ae = soup.find_all('a', attrs={'data-test': 'quoteLink'})
        be = soup.find_all('td', attrs={'aria-label': 'Name'})
        ce = soup.find_all('td', attrs={'aria-label': 'Price (Intraday)'})
        de = soup.find_all('td', attrs={'aria-label': 'Change'})
        ee = soup.find_all('td', attrs={'aria-label': '% Change'})
        fe = soup.find_all('td', attrs={'aria-label': 'Volume'})
        ge = soup.find_all('td', attrs={'aria-label': 'Avg Vol (3 month)'})
        he = soup.find_all('td', attrs={'aria-label': 'Market Cap'})
        ie = soup.find_all('td', attrs={'aria-label': 'PE Ratio (TTM)'})
  

        ae_ = []
        be_ = []
        ce_ = []
        de_ = []
        ee_ = []
        fe_ = []
        ge_ = []
        he_ = []
        ie_ = []
        for title in ae:
            ae_.append(title.text.strip())
        for title in be:
            be_.append(title.text.strip())
        for title in ce:
            ce_.append(title.text.strip())
        for title in de:
            de_.append(title.text.strip())
        for title in ee:
            ee_.append(title.text.strip())
        for title in fe:
            fe_.append(title.text.strip())
        for title in ge:
            ge_.append(title.text.strip())
        for title in he:
            he_.append(title.text.strip())
        for title in ie:
            ie_.append(title.text.strip())
  # dataframe Name and Age columns
        df = pd.DataFrame({'Symbol': ae_, 'Name': be_, 'Price': ce_, 'Change': de_, 'Change %': ee_, 'Volume': fe_, 'Avg volume': ge_, 'Market cap': he_, 'Ration': ie_,})
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
        creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
        client = gspread.authorize(creds)
        spreadsheet_key = '1X7APg9YH6ndu2lEhYDjMrWGwE1mQZlIh3G-XbzV_8zA'
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
        schedule.every(35).minutes.do(yloserspage)
        #requests.get("https://stocks.desss-portfolio.com/yahoo/yahoo_losers")
        while 1:
            schedule.run_pending()
            time.sleep(1)
        return 'ok'
  else:
        return render_template("losers-page2.html")

@app.route("/ylosers/page-3", methods =["GET", "POST"])
def loserspage():
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
        ag = soup.find_all('a', attrs={'data-test': 'quoteLink'})
        bg = soup.find_all('td', attrs={'aria-label': 'Name'})
        cg = soup.find_all('td', attrs={'aria-label': 'Price (Intraday)'})
        dg = soup.find_all('td', attrs={'aria-label': 'Change'})
        eg = soup.find_all('td', attrs={'aria-label': '% Change'})
        fg = soup.find_all('td', attrs={'aria-label': 'Volume'})
        gg = soup.find_all('td', attrs={'aria-label': 'Avg Vol (3 month)'})
        hg = soup.find_all('td', attrs={'aria-label': 'Market Cap'})
        ig = soup.find_all('td', attrs={'aria-label': 'PE Ratio (TTM)'})
  

        ag_ = []
        bg_ = []
        cg_ = []
        dg_ = []
        eg_ = []
        fg_ = []
        gg_ = []
        hg_ = []
        ig_ = []
        for title in ag:
            ag_.append(title.text.strip())
        for title in bg:
            bg_.append(title.text.strip())
        for title in cg:
            cg_.append(title.text.strip())
        for title in dg:
            dg_.append(title.text.strip())
        for title in eg:
            eg_.append(title.text.strip())
        for title in fg:
            fg_.append(title.text.strip())
        for title in gg:
            gg_.append(title.text.strip())
        for title in hg:
            hg_.append(title.text.strip())
        for title in ig:
            ig_.append(title.text.strip())
  # dataframe Name and Age columns
        df = pd.DataFrame({'Symbol': ag_, 'Name': bg_, 'Price': cg_, 'Change': dg_, 'Change %': eg_, 'Volume': fg_, 'Avg volume': gg_, 'Market cap': hg_, 'Ration': ig_,})
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
        creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
        client = gspread.authorize(creds)
        spreadsheet_key = '1X7APg9YH6ndu2lEhYDjMrWGwE1mQZlIh3G-XbzV_8zA'
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
        schedule.every(35).minutes.do(loserspage)
        #requests.get("https://stocks.desss-portfolio.com/yahoo/yahoo_losers")
        while 1:
            schedule.run_pending()
            time.sleep(1)
        return 'ok'
  else:
        return render_template("losers-page3.html")

@app.route("/ymostactive/page-1", methods =["GET", "POST"])
def ymostactive():
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
        ah = soup.find_all('a', attrs={'data-test': 'quoteLink'})
        bh = soup.find_all('td', attrs={'aria-label': 'Name'})
        ch = soup.find_all('td', attrs={'aria-label': 'Price (Intraday)'})
        dh = soup.find_all('td', attrs={'aria-label': 'Change'})
        eh = soup.find_all('td', attrs={'aria-label': '% Change'})
        fh = soup.find_all('td', attrs={'aria-label': 'Volume'})
        gh = soup.find_all('td', attrs={'aria-label': 'Avg Vol (3 month)'})
        hh = soup.find_all('td', attrs={'aria-label': 'Market Cap'})
        ih = soup.find_all('td', attrs={'aria-label': 'PE Ratio (TTM)'})
  

        ah_ = []
        bh_ = []
        ch_ = []
        dh_ = []
        eh_ = []
        fh_ = []
        gh_ = []
        hh_ = []
        ih_ = []
        for title in ah:
            ah_.append(title.text.strip())
        for title in bh:
            bh_.append(title.text.strip())
        for title in ch:
            ch_.append(title.text.strip())
        for title in dh:
            dh_.append(title.text.strip())
        for title in eh:
            eh_.append(title.text.strip())
        for title in fh:
            fh_.append(title.text.strip())
        for title in gh:
            gh_.append(title.text.strip())
        for title in hh:
            hh_.append(title.text.strip())
        for title in ih:
            ih_.append(title.text.strip())
  # dataframe Name and Age columns
        df = pd.DataFrame({'Symbol': ah_, 'Name': bh_, 'Price': ch_, 'Change': dh_, 'Change %': eh_, 'Volume': fh_, 'Avg volume': gh_, 'Market cap': hh_, 'Ration': ih_,})
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
        creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
        client = gspread.authorize(creds)
        spreadsheet_key = '1hVc3A_XjDt4zYwtEb5YEzQbyyjCn7LcPOQlx03dsHvs'
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
        schedule.every(15).minutes.do(ymostactive)
        requests.get("https://stocks.desss-portfolio.com/yahoo/most_active")
        while 1:
            schedule.run_pending()
            time.sleep(1)
        return 'ok'
  else:
        return render_template("mostactive.html")

@app.route("/ymostactive/page-2", methods =["GET", "POST"])
def ymostactivepage():
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
        ai = soup.find_all('a', attrs={'data-test': 'quoteLink'})
        bi = soup.find_all('td', attrs={'aria-label': 'Name'})
        ci = soup.find_all('td', attrs={'aria-label': 'Price (Intraday)'})
        di = soup.find_all('td', attrs={'aria-label': 'Change'})
        ei = soup.find_all('td', attrs={'aria-label': '% Change'})
        fi = soup.find_all('td', attrs={'aria-label': 'Volume'})
        gi = soup.find_all('td', attrs={'aria-label': 'Avg Vol (3 month)'})
        hi = soup.find_all('td', attrs={'aria-label': 'Market Cap'})
        ii = soup.find_all('td', attrs={'aria-label': 'PE Ratio (TTM)'})
  

        ai_ = []
        bi_ = []
        ci_ = []
        di_ = []
        ei_ = []
        fi_ = []
        gi_ = []
        hi_ = []
        ii_ = []
        for title in ai:
            ai_.append(title.text.strip())
        for title in bi:
            bi_.append(title.text.strip())
        for title in ci:
            ci_.append(title.text.strip())
        for title in di:
            di_.append(title.text.strip())
        for title in ei:
            ei_.append(title.text.strip())
        for title in fi:
            fi_.append(title.text.strip())
        for title in gi:
            gi_.append(title.text.strip())
        for title in hi:
            hi_.append(title.text.strip())
        for title in ii:
            ii_.append(title.text.strip())
  # dataframe Name and Age columns
        df = pd.DataFrame({'Symbol': ai_, 'Name': bi_, 'Price': ci_, 'Change': di_, 'Change %': ei_, 'Volume': fi_, 'Avg volume': gi_, 'Market cap': hi_, 'Ration': ii_,})
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
        creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
        client = gspread.authorize(creds)
        spreadsheet_key = '1hVc3A_XjDt4zYwtEb5YEzQbyyjCn7LcPOQlx03dsHvs'
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
        schedule.every(15).minutes.do(ymostactivepage)
        #requests.get("https://stocks.desss-portfolio.com/yahoo/most_active")
        while 1:
            schedule.run_pending()
            time.sleep(1)
        return 'ok'
  else:
        return render_template("mostactive-page2.html")

@app.route("/ymostactive/page-3", methods =["GET", "POST"])
def mostactivepage():
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
        aj = soup.find_all('a', attrs={'data-test': 'quoteLink'})
        bj = soup.find_all('td', attrs={'aria-label': 'Name'})
        cj = soup.find_all('td', attrs={'aria-label': 'Price (Intraday)'})
        dj = soup.find_all('td', attrs={'aria-label': 'Change'})
        ej = soup.find_all('td', attrs={'aria-label': '% Change'})
        fj = soup.find_all('td', attrs={'aria-label': 'Volume'})
        gj = soup.find_all('td', attrs={'aria-label': 'Avg Vol (3 month)'})
        hj = soup.find_all('td', attrs={'aria-label': 'Market Cap'})
        ij = soup.find_all('td', attrs={'aria-label': 'PE Ratio (TTM)'})
  

        aj_ = []
        bj_ = []
        cj_ = []
        dj_ = []
        ej_ = []
        fj_ = []
        gj_ = []
        hj_ = []
        ij_ = []
        for title in aj:
            aj_.append(title.text.strip())
        for title in bj:
            bj_.append(title.text.strip())
        for title in cj:
            cj_.append(title.text.strip())
        for title in dj:
            dj_.append(title.text.strip())
        for title in ej:
            ej_.append(title.text.strip())
        for title in fj:
            fj_.append(title.text.strip())
        for title in gj:
            gj_.append(title.text.strip())
        for title in hj:
            hj_.append(title.text.strip())
        for title in ij:
            ij_.append(title.text.strip())
  # dataframe Name and Age columns
        df = pd.DataFrame({'Symbol': aj_, 'Name': bj_, 'Price': cj_, 'Change': dj_, 'Change %': ej_, 'Volume': fj_, 'Avg volume': gj_, 'Market cap': hj_, 'Ration': ij_,})
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
        creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
        client = gspread.authorize(creds)
        spreadsheet_key = '1hVc3A_XjDt4zYwtEb5YEzQbyyjCn7LcPOQlx03dsHvs'
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
        schedule.every(15).minutes.do(mostactivepage)
        #requests.get("https://stocks.desss-portfolio.com/yahoo/most_active")
        while 1:
            schedule.run_pending()
            time.sleep(1)
        return 'ok'
  else:
        return render_template("mostactive-page3.html")


@app.route("/ytrending", methods =["GET", "POST"])
def ytrending():
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
  

        an = soup.find_all('a', attrs={'class': 'Fw(600) C($linkColor)'})
        bn = soup.find_all('td', attrs={'aria-label': 'Name'})
        cn = soup.find_all('td', attrs={'aria-label': 'Last Price'})
        dn = soup.find_all('td', attrs={'aria-label': 'Market Time'})
        en = soup.find_all('td', attrs={'aria-label': 'Change'})
        fn = soup.find_all('td', attrs={'aria-label': '% Change'})
        gn = soup.find_all('td', attrs={'aria-label': 'Volume'})
        hn = soup.find_all('td', attrs={'aria-label': 'Market Cap'})
  

        an_ = []
        bn_ = []
        cn_ = []
        dn_ = []
        en_ = []
        fn_ = []
        gn_ = []
        hn_ = []
        for title in an:
            an_.append(title.text.strip())
        for title in bn:
            bn_.append(title.text.strip())
        for title in cn:
            cn_.append(title.text.strip())
        for title in dn:
            dn_.append(title.text.strip())
        for title in en:
            en_.append(title.text.strip())
        for title in fn:
            fn_.append(title.text.strip())
        for title in gn:
            gn_.append(title.text.strip())
        for title in hn:
            hn_.append(title.text.strip())
        # dataframe Name and Age columns
        df = pd.DataFrame({'Symbol': an_, 'Name': bn_, 'Price': cn_, 'Market Time': dn_, 'Change': en_, 'Change %': fn_, 'Volume': gn_, 'Market cap': hn_})
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
        creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
        client = gspread.authorize(creds)
        spreadsheet_key = '1FDbwLYGQHiuVALZBUcId-OggbZxdrO4CJGncd0zoY0Q'
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
        schedule.every(15).minutes.do(ytrending)
        requests.get("https://stocks.desss-portfolio.com/yahoo/yahoo_trending")
        while 1:
            schedule.run_pending()
            time.sleep(1)
        return 'ok'
  else:
        return render_template("trending.html")



@app.route("/ganiers-file/<url>", methods =["GET", "POST"])
def gainersdatas():
    if request.method == "POST":
        url = request.form['text']
        # getting input with name = fname in HTML form
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'lxml')
        ac = soup.find_all('a', attrs={'data-test': 'quoteLink'})
        bc = soup.find_all('td', attrs={'aria-label': 'Name'})
        cc = soup.find_all('td', attrs={'aria-label': 'Price (Intraday)'})
        dc = soup.find_all('td', attrs={'aria-label': 'Change'})
        ec = soup.find_all('td', attrs={'aria-label': '% Change'})
        fc = soup.find_all('td', attrs={'aria-label': 'Volume'})
        gc = soup.find_all('td', attrs={'aria-label': 'Avg Vol (3 month)'})
        hc = soup.find_all('td', attrs={'aria-label': 'Market Cap'})
        ic = soup.find_all('td', attrs={'aria-label': 'PE Ratio (TTM)'})
  

        ac_ = []
        bc_ = []
        cc_ = []
        dc_ = []
        ec_ = []
        fc_ = []
        gc_ = []
        hc_ = []
        ic_ = []
        for title in ac:
            ac_.append(title.text.strip())
        for title in bc:
            bc_.append(title.text.strip())
        for title in cc:
            cc_.append(title.text.strip())
        for title in dc:
            dc_.append(title.text.strip())
        for title in ec:
            ec_.append(title.text.strip())
        for title in fc:
            fc_.append(title.text.strip())
        for title in gc:
            gc_.append(title.text.strip())
        for title in hc:
            hc_.append(title.text.strip())
        for title in ic:
            ic_.append(title.text.strip())
  # dataframe Name and Age columns
        df = pd.DataFrame({'Symbol': ac_, 'Name': bc_, 'Price': cc_, 'Change': dc_, 'Change %': ec_, 'Volume': fc_, 'Avg volume': gc_, 'Market cap': hc_, 'Ration': ic_,})
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