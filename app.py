from flask import Flask, render_template, request
from com.junyeongc.won.exchange.exchange_w_controller import ExchangeController
from com.junyeongc.won.exchange.exchange_w_model import ExchangeModel
from com.junyeongc.won.knpsack.knpsack_controller import KnpsackController, KnpsackController
from com.junyeongc.won.knpsack.knpsack_model import KnpsackModel
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

@app.route('/knpsack')
def knapsack() :
    return render_template('knpsack.html')

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
        pass

@app.route('/solve_knpsack', methods=["POST", "GET"] )
def solve_knpsack():
    print("💰가방 문제 풀기기💰")
    if request.method == "POST" :
        print("😊POST 접근😊")       
        capacity = int(request.form.get('capacity'))
        weight1 = int(request.form.get('weight1'))
        weight2 = int(request.form.get('weight2'))
        weight3 = int(request.form.get('weight3'))
        weight4 = int(request.form.get('weight4'))
        profit1 = int(request.form.get('profit1'))
        profit2 = int(request.form.get('profit2'))
        profit3 = int(request.form.get('profit3'))
        profit4 = int(request.form.get('profit4'))
        print("capacity: ", capacity)
        print("weight1: ", weight1)
        print("weight2: ", weight2)
        print("weight3: ", weight3)
        print("weight4: ", weight4)
        print("profit1: ", profit1)
        print("profit2: ", profit2)
        print("profit3: ", profit3)
        print("profit4: ", profit4)

        controller = KnpsackController(capacity=capacity, weight1=weight1, weight2=weight2, 
                                        weight3=weight3, weight4=weight4, profit1=profit1, 
                                        profit2=profit2, profit3=profit3, profit4=profit4)
        resp : KnpsackModel = controller.get_result()
        print(resp)
        
        render_html = "<h1>결과보기</h1>"
        render_html += "<h3>최대 이익:</h3>" + str(resp.total_profit)
        render_html += "<h3>담을 항목:</h3>" + str(resp.select_box)

        return render_template('knpsack.html', render_html = render_html)

        

    else:
        return render_template('knpsack.html')


if __name__ == '__main__':
    app.run(debug=True)


   