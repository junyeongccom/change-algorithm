from flask import Flask, render_template, request
app = Flask(__name__)

def get_unit_count(total, won_list):
        money = int(total)
        won_dict = {}
        for won in won_list:
            won_dict [won] = money // won
            money %= won
        return won_dict

def get_dollar_count(total, dollar_list):
        money = int(total)
        dollar_dict = {}
        for dollar in dollar_list:
            dollar_dict [dollar] = money // dollar
            money %= dollar
        return dollar_dict


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

        won_dict = get_unit_count(total, won_list)
        
        for won, count in won_dict.items():
            print(f"{won}원:{count}개")

        render_html = '<h1> 결과보기 </h1>'
        for won, count in won_dict.items():
            render_html += f"{won}원:{count}개<br/>"

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
        
         
        DOLLAR_100 = 100
        DOLLAR_50 = 50
        DOLLAR_20 = 20
        DOLLAR_10 = 10
        DOLLAR_5 = 5
        DOLLAR_2 = 2
        DOLLAR_1 = 1

        dollar_list = [DOLLAR_100, DOLLAR_50, DOLLAR_20, DOLLAR_10, DOLLAR_5, DOLLAR_2, DOLLAR_1]

        dollar_dict = get_dollar_count(total, dollar_list)
        
        for dollar, count in dollar_dict.items():
            print(f"${dollar}:{count}장")

        dollar_html = '<h1> 결과보기 </h1>'
        for dollar, count in dollar_dict.items():
            dollar_html += f"{dollar}원:{count}개<br/>"

        return render_template("exchangedollar.html", dollar_html = dollar_html)

    else:
        print("💲GET방식으로 요청💲")
        return render_template("exchangedollar.html")

if __name__ == '__main__':
    app.run(debug=True)