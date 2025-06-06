# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]

def total_sales_by_product(data, product_key):
    """Calculates the total sales of a specific product in 30 days."""
    total = 0
    for day in sales_data:
        if product_key in day:
            total += day[product_key]

    return total



def average_daily_sales(data, product_key):
    """Calculates the average daily sales of a specific product."""
    average = 0
    total_days = 0

    for day in sales_data:
        if product_key in day:
            average += day[product_key] 
            total_days += 1

    return average / total_days



def best_selling_day(data):
    """Finds the day with the highest total sales."""
    
    max_sales = 0
    best_day = None

    for day in data: 
        total = 0

        for key in day:  
            if key != "day":
                total += day[key] 
        
        if total > max_sales: 
            max_sales = total 
            best_day = day["day"] 
    return best_day



def days_above_threshold(data, product_key, threshold):
    """Counts how many days the sales of a product exceeded a given threshold."""
    days_exceeed = 0

    for day in data:
        if day[product_key] > threshold:
            days_exceeed += 1

    return days_exceeed
        

def top_product(data):
    """Determines which product had the highest total sales in 30 days."""
    a = 0
    b = 0
    c = 0

    for day in data:
        a += day["product_a"]
        b += day["product_b"]
        c += day["product_c"]

    if a >= b and a >= c:
        return "product_a"
    elif b >= a and b >= c:
        return "product_b"
    else:
        return "product_c"

    
def bottom_product(data):
    a = sum(day["product_a"] for day in data)
    b = sum(day["product_b"] for day in data)
    c = sum(day["product_c"] for day in data)

    if a <= b and a <= c:
        return "product_a"
    elif b <= a and b <= c:
        return "product_b"
    else:
        return "product_c"


def top_3(data):
    day_sales = []
    

    for day in data: 
        total = 0 

        for key in day:  
            if key != "day":
                total += day[key] 
                day_sales.append((total, day["day"])) 

    day_sales.sort(reverse=True)
    top_3_days = [day for total, day in day_sales[:3]] 
            

    return ", ".join(str(d) for d in top_3_days) 


def max_min(data):
    day_sales = []
    

    for day in data:
        total = 0

        for key in day: 
            if key != "day":
                total += day[key] 
                day_sales.append(total)

    range = max(day_sales) - min(day_sales)   

    return range

# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))
print("Product with lowest total sales:", bottom_product(sales_data))
print("Top 3 days with highest total sales:", top_3(sales_data))
print("Range max-min in total sales:", max_min(sales_data))