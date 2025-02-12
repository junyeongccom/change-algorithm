from dataclasses import dataclass

@dataclass
class ExchangeDModel:
    total: int
    dollar_dict: dict

    @property
    def total(self) -> int:
        return self._total
    @total.setter
    def total(self, total):
        self._total = total

    @property
    def dollar_dict(self) -> dict:
        return self._dollar_dict
    @dollar_dict.setter
    def dollar_dict(self, dollar_dict):
        self._dollar_dict = dollar_dict
