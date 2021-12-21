
from flask import *
from forex_python.converter import CurrencyRates
app=Flask(__name__,template_folder="templete",static_folder='static')
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/convert",methods=['POST','GET'])
def convert():
    result,x,temp,al,status="","","","",0
    if request.method == 'POST' and request.form.get('amount'):
        if type((request.form.get('amount')))==str:
            if request.form.get('from_currency')=="Present form" and request.form.get('to_currency')=="Conversion form":
                status = 1
                al="Please Select a valid option"
            elif(request.form.get('from_currency')==request.form.get('to_currency')):
                status=1
                al="SAME CURRENCY"
                temp=request.form.get('amount')+" "+request.form.get('to_currency')
            else:
                try:
                    status=0
                    c = CurrencyRates()
                    amount =float(request.form.get('amount'))
                    from_currency =(request.form.get('from_currency'))
                    to_currency = (request.form.get('to_currency'))
                    result = round(float(c.convert(from_currency, to_currency, amount)),3)
                    x=round(float(c.convert(from_currency, to_currency, 1)),3)
                    temp=str(result)+" "+(request.form.get('to_currency'))
                except:
                    status=1
                    al = "Enter a number/valid input"
    else:
        temp="Enter Amount"
    return render_template("convert.html",ans=temp,alert=status,al=al)
@app.route("/about")
def about():
    return render_template("about.html")
app.run(debug=True)

