
from flask import *
from forex_python.converter import CurrencyRates
app=Flask(__name__,template_folder="templete",static_folder='static')
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/convert",methods=['POST','GET'])
def convert():
    result,x="",""
    if request.method == 'POST' and request.form.get('amount'):
        if request.form.get('from_currency')==request.form.get('to_currency'):
            result=request.form.get('amount')
        else:
            c = CurrencyRates()
            amount =float(request.form.get('amount'))
            from_currency =(request.form.get('from_currency'))
            to_currency = (request.form.get('to_currency'))
            result = round(float(c.convert(from_currency, to_currency, amount)),3)
            x=round(float(c.convert(from_currency, to_currency, 1)),3)
    return render_template("convert.html",ans=result,to=(request.form.get('to_currency')))

app.run(debug=True)

