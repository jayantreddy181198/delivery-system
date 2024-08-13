from .models import FoodItem, BarItem

def calculate_total_cost(items):
    total_cost = 0
    for item in items:
        food_item = FoodItem.objects.using('postgres_db').filter(name=item['name']).first()
        bar_item = BarItem.objects.using('postgres_db').filter(name=item['name']).first()

        if food_item:
            total_cost += food_item.price * item['quantity']
        elif bar_item:
            total_cost += bar_item.price * item['quantity']
        else:
            raise ValueError(f"Item '{item['name']}' not found.")
    
    return total_cost
