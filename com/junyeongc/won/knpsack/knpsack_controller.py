from com.junyeongc.won.knpsack.knpsack_model import KnpsackModel, KnpsackModel
from com.junyeongc.won.knpsack.knpsack_service import KnpsackService, KnpsackService


class KnpsackController:

    def __init__(self, **kwargs):
        self.capacity = kwargs.get('capacity')
        self.weight1 = kwargs.get('weight1')
        self.weight2 = kwargs.get('weight2')
        self.weight3 = kwargs.get('weight3')
        self.weight4 = kwargs.get('weight4')
        self.profit1 = kwargs.get('profit1')
        self.profit2 = kwargs.get('profit2')
        self.profit3 = kwargs.get('profit3')
        self.profit4 = kwargs.get('profit4')

    def get_result(self)->KnpsackModel:
        knpsack = KnpsackModel()
        service = KnpsackService()
        knpsack.capacity = self.capacity
        knpsack.weight1 = self.weight1
        knpsack.weight2 = self.weight2
        knpsack.weight3 = self.weight3
        knpsack.weight4 = self.weight4
        knpsack.profit1 = self.profit1
        knpsack.profit2 = self.profit2
        knpsack.profit3 = self.profit3
        knpsack.profit4 = self.profit4
        return service.execute(knpsack)
