

from com.junyeongc.won.exchange_d_model import ExchangeDModel
from com.junyeongc.won.exchange_d_service import ExchangeDService


class ExchangeDController:
    def __init__(self, total):
        self.total = total
        

    def get_result(self) -> ExchangeDModel:
        service = ExchangeDService()
        dollar = ExchangeDModel
        dollar.total = self.total
        return service.execute(dollar)