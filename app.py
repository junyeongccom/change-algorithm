from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index() :

    if request.method == "POST" :
        print("💲POST방식으로 요청💲")
        total = request.form.get('total')
        paid = request.form.get('paid')
        amount = int(paid) - int(total)
        if amount < 0:
            error = "😡금액을 더 지불하세요😡"
            print("📝가격(원):",total)
            print("💸지불한금액(원):",paid)
            print("😡금액을 더 지불하세요😡")
            return render_template("index.html", error = error)
        else: 
            COIN_500 = 500
            COIN_100 = 100
            COIN_50 = 50
            COIN_10 = 10
            coin500 = amount // COIN_500
            coin500_nmg = amount % COIN_500
            coin100 = coin500_nmg // COIN_100
            coin100_nmg = coin500_nmg % COIN_100
            coin50 = coin100_nmg // COIN_50
            coin50_nmg = coin100_nmg % COIN_50
            coin10 = coin50_nmg // COIN_10

            print("📝가격(원):",total)
            print("💸지불한금액(원):",paid)
            print("💰500원:",coin500, "개")
            print("💰100원:",coin100, "개")
            print("💰50원:",coin50, "개")
            print("💰10원:",coin10, "개")
            return render_template("index.html", total = total, paid = paid, amount = amount, 
                                   coin500 = coin500, coin100 = coin100, coin50 = coin50, coin10 = coin10)

    else:
        print("💲GET방식으로 요청💲")
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)