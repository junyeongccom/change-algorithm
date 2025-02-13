from com.junyeongc.won.knpsack.knpsack_model import KnpsackModel

class KnpsackService:

    def execute(self, knpsack: KnpsackModel) -> float:

        print("🎒배낭 문제 풀기🎒")
        profit_list = [knpsack.profit1, knpsack.profit2, knpsack.profit3, knpsack.profit4]
        weight_list = [knpsack.weight1, knpsack.weight2, knpsack.weight3, knpsack.weight4]

        item1 = {"name": "item1", "profit": knpsack.profit1, "weight": knpsack.weight1}
        item2 = {"name": "item2", "profit": knpsack.profit2, "weight": knpsack.weight2}
        item3 = {"name": "item3", "profit": knpsack.profit3, "weight": knpsack.weight3}
        item4 = {"name": "item4", "profit": knpsack.profit4, "weight": knpsack.weight4}
        items = [item1, item2, item3, item4]
        
        profit_per_weight = []
        for i in items:
            profit_per_weight.append(i["profit"]/i["weight"]) 

        for i in profit_per_weight:
            print("하늘이 천재?!", i)     
        
        
        item1 = {"name": "item1", "profit": knpsack.profit1, "weight": knpsack.weight1, "profit_per_weight": profit_per_weight[0]}
        item2 = {"name": "item2", "profit": knpsack.profit2, "weight": knpsack.weight2, "profit_per_weight": profit_per_weight[1]}
        item3 = {"name": "item3", "profit": knpsack.profit3, "weight": knpsack.weight3, "profit_per_weight": profit_per_weight[2]}
        item4 = {"name": "item4", "profit": knpsack.profit4, "weight": knpsack.weight4, "profit_per_weight": profit_per_weight[3]}
        items = [item1, item2, item3, item4]
        
        for i in range(4):  
            for j in range(i+1, 4):
                if items[i].get("profit_per_weight") < items[j].get("profit_per_weight"):
                    items[i], items[j] = items[j], items[i] 

        for i in items:
            print("❗중간점검", i.get("name"))

        total_weight = knpsack.capacity
        total_profit = 0
        for i in range(4):
            if items[i].get("weight") <= total_weight:
                total_weight -= items[i].get("weight")
                total_profit += items[i].get("profit")
            else:
                # 3/4 인 경우 처리리
                break
                

        total_value = 0  
        remaining_capacity = knpsack.capacity  
        selected_items = [None, None, None, None]  
        index = 0  

        for profit, weight in items:
            if remaining_capacity >= weight:
                remaining_capacity -= weight
                total_value += profit
                selected_items[index] = (profit, weight)  
                index += 1  
            else:
                fraction = remaining_capacity / weight
                total_value += profit * fraction
                selected_items[index] = (profit * fraction, remaining_capacity)  
                index += 1  
                break  

        selected_items = selected_items[:index]

        knpsack.items = selected_items  
        knpsack.total_value = total_value

        return knpsack


        
        

        