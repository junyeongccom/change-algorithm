from flask import Flask, render_template, request

from com.junyeongc.won.exchange_d_controller import ExchangeDController
from com.junyeongc.won.exchange_d_model import ExchangeDModel
app = Flask(__name__)


@app.route('/')
def index() :
    return render_template('index.html')


@app.route('/exchangewon', methods=["POST","GET"])
def exchangewon() :
    print("🪙거스름돈 계산기🪙")
    if request.method == "POST" :
        print("💲POST방식으로 요청💲")
        total = request.form.get('total')
        print("📝총금액(원):",total)
        
        WON_50000 = 50000
        WON_10000 = 10000
        WON_5000 = 5000
        WON_1000 = 1000
        WON_500 = 500
        WON_100 = 100
        WON_50 = 50
        WON_10 = 10

        won_list = [WON_50000, WON_10000, WON_5000, WON_1000, WON_500, WON_100, WON_50, WON_10]

        render_html = render_html

        return render_template("exchangewon.html", render_html = render_html)

    else:
        print("💲GET방식으로 요청💲")
        return render_template("exchangewon.html")


@app.route('/exchangedollar', methods=["POST","GET"])
def exchangedollar() :
    print("💲달러 환전💲")
    if request.method == "POST" :
        print("💲POST방식으로 요청💲")
        total = request.form.get('total')
        print("📝총금액(달러):",total) 

        controller = ExchangeDController(total = total)
        resp: ExchangeDModel = controller.get_result()
        dollar_dict = resp.dollar_dict

        for dollar, count in dollar_dict.items():
            print(f"${dollar}:{count}장")

        render_html = '<h3>결과보기</h3>'
        for dollar, count in dollar_dict.items():
            render_html += f"${dollar}:{count}개<br/>"

        return render_template("exchangedollar.html", render_html = render_html)

    else:
        print("💲GET방식으로 요청💲")
        return render_template("exchangedollar.html")

if __name__ == '__main__':
    app.run(debug=True)