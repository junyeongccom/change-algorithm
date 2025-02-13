from com.junyeongc.won.exchange.exchange_w_model import ExchangeModel
from com.junyeongc.won.exchange.exchange_w_service import ExchangeService

class ExchangeController:

    def __init__(self, **kwargs):
        self.amount = kwargs.get('amount')
        self.currency = kwargs.get('currency')
        print("currency: ", self.currency)
        print("amount: ", self.amount)

    def get_result(self)->ExchangeModel:
        exchange = ExchangeModel()
        service = ExchangeService()
        exchange.amount = self.amount
        exchange.currency = self.currency
        return service.execute(exchange)
