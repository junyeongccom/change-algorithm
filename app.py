from flask import Flask, render_template, request
app = Flask(__name__)

def get_unit_count(amount, won_list):
    money = amount
    won_dict = {}
    for won in won_list:
        won_dict [won] = money // won
        money %= won
    return won_dict

@app.route('/', methods=["POST","GET"])
def index() :
    print("🪙거스름름돈 계산기🪙")
    if request.method == "POST" :
        print("💲POST방식으로 요청💲")
        total = request.form.get('total')
        paid = request.form.get('paid')
        amount = int(paid) - int(total)
        print("📝가격(원):",total)
        print("💸지불한금액(원):",paid)
        
        if amount < 0:
            error = "😡금액을 더 지불하세요😡"
            print("😡금액을 더 지불하세요😡")
            
            return render_template("index.html", error = error)

        else: 
            WON_50000 = 50000
            WON_10000 = 10000
            WON_5000 = 5000
            WON_1000 = 1000
            WON_500 = 500
            WON_100 = 100
            WON_50 = 50
            WON_10 = 10

            won_list = [WON_50000, WON_10000, WON_5000, WON_1000, WON_500, WON_100, WON_50, WON_10]

            won_dict = get_unit_count(amount, won_list)
            
            for won, count in won_dict.items():
                print(f"{won}원:{count}개")

            render_html = '<h1> 결과보기 </h1>'
            for won, count in won_dict.items():
                render_html += f"{won}원:{count}개<br/>"

            return render_template("index.html", render_html = render_html)

    else:
        print("💲GET방식으로 요청💲")
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)