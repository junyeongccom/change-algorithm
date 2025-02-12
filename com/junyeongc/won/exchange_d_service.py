

from com.junyeongc.won.exchange_d_model import ExchangeDModel


class ExchangeDService:
    def __init__(self):
        pass

    def execute(self, dollar: ExchangeDModel) -> ExchangeDModel:
        
        total = int(dollar.total)
        
        DOLLAR_100 = 100
        DOLLAR_50 = 50
        DOLLAR_20 = 20
        DOLLAR_10 = 10
        DOLLAR_5 = 5
        DOLLAR_2 = 2
        DOLLAR_1 = 1

        dollar_list = [DOLLAR_100, DOLLAR_50, DOLLAR_20, DOLLAR_10, DOLLAR_5, DOLLAR_2, DOLLAR_1]

        dollar_dict = {}
        for money in dollar_list:
            dollar_dict [money] = total // money
            total %= money
    
        dollar.dollar_dict = dollar_dict

        return dollar