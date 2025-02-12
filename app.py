from flask import Flask, render_template, request
from com.junyeongc.won.exchange_w_controller import ExchangeController
from com.junyeongc.won.exchange_w_model import ExchangeModel
app = Flask(__name__)

@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/dollar')
def exchangedollar() :
    return render_template('exchangedollar.html')

@app.route('/won')
def exchangewon() :
    return render_template('exchangewon.html')

@app.route('/exchange', methods=["POST", "GET"] )
def paid():
    print("💰거스름돈 계산기💰")
    if request.method == "POST" :
        print("😊POST 접근😊")       
        currency = request.form.get('currency') #USD,WON 상수
        amount = int(request.form.get('amount'))
        print("currency: ", currency)
        print("amount: ", amount)

        controller = ExchangeController(amount=amount, currency=currency)
        resp : ExchangeModel = controller.get_result()

        render_html = '<h1>결과보기</h1>'
        render_html += resp.result
        if currency == 'USD':
            return render_template('exchangedollar.html', render_html=render_html)
        elif currency == 'WON':
            return render_template('exchangewon.html', render_html=render_html)
        else:
            print("잘못된 화폐단위입니다.")

    else:
         print("😊GET 접근😊")
         return render_template('exchangewon.html')


if __name__ == '__main__':
    app.run(debug=True)