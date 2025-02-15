from com.junyeongc.won.knpsack.knpsack_model import KnpsackModel

class KnpsackService:

    def __init__(self):
        pass

    def execute(self, knpsack: KnpsackModel) -> KnpsackModel:

        print("🎒배낭 문제 풀기🎒")
        item1 = {"profit": knpsack.profit1, "weight": knpsack.weight1}
        item2 = {"profit": knpsack.profit2, "weight": knpsack.weight2}
        item3 = {"profit": knpsack.profit3, "weight": knpsack.weight3}
        item4 = {"profit": knpsack.profit4, "weight": knpsack.weight4}
        items = [item1, item2, item3, item4]
    
        for i in range(4):
            items[i]['name'] = f"item{i+1}"
            items[i]['profit_per_weight'] = items[i].get('profit')/items[i].get('weight')
        for i in items:
            print("😊",i.get('name'), i.get('profit_per_weight'))
        
        for i in range(4):  
            for j in range(i+1, 4):
                if items[i].get("profit_per_weight") < items[j].get("profit_per_weight"):
                    items[i], items[j] = items[j], items[i] 
        for i in items:
            print("❗중간점검", i.get("name"))

        remain_weight = knpsack.capacity
        total_profit = 0

        select_box = []
        for i in range(4):
            if items[i].get("weight") <= remain_weight:
                remain_weight -= items[i].get("weight")
                total_profit += items[i].get("profit")
                select_box.append(items[i].get('name'))
                continue
            else:
                total_profit = total_profit + remain_weight*items[i].get("profit_per_weight")
                select_box.append(items[i].get('name'))
                break
        
        knpsack.total_profit = total_profit
        knpsack.select_box = select_box
        
        return knpsack
    



           
        

        