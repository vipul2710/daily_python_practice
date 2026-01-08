logs = [
    {"user_id": 1, "action": "login"},
    {"user_id": 2, "action": "login"},
    {"user_id": 1, "action": "click"},
    {"user_id": 3, "action": None},
    {"user_id": 2, "action": "click"},
    {"user_id": 1, "action": "logout"},
    {"user_id": 2, "action": "logout"},
    {"user_id": 3, "action": "login"},
    {"user_id": 3, "action": "click"},
]

def count_user_actions(logs):
    counts = {}

    for log in logs:
        user_id = log.get('user_id')
        action = log.get('action')

        if action is None:
            continue

        counts[user_id] = counts.get(user_id, 0) + 1

    return counts

print("Total actions per user:", count_user_actions(logs))

orders = [
    {"order_id": 1, "customer": "Alice", "amount": 300},
    {"order_id": 2, "customer": "Bob", "amount": None},
    {"order_id": 3, "customer": "alice", "amount": 200},
    {"order_id": 4, "customer": "Esha", "amount": -50},
    {"order_id": 5, "customer": "Bob", "amount": 400},
    {"order_id": 6, "customer": None, "amount": 500},
    {"order_id": 7, "customer": "Alice", "amount": 100}
]

def total_spend_per_customer(orders):
    totals = {}

    for order in orders:
        customer = order.get('customer')
        amount = order.get('amount')

        # validate customer and amount
        if customer is None or amount is None:
            continue

        if amount < 0:
            continue

        # standardize customer name
        customer = customer.lower()

        # aggregate
        totals[customer] = totals.get(customer, 0) + amount

    return totals

print("Total spend per customer:", total_spend_per_customer(orders))

logs = [
    {"emp_id": 1, "hours": 8},
    {"emp_id": 2, "hours": None},
    {"emp_id": 1, "hours": 9},
    {"emp_id": 3, "hours": -5},
    {"emp_id": 2, "hours": 7},
    {"emp_id": None, "hours": 4},
    {"emp_id": 1, "hours": 6},
    {"emp_id": 3, "hours": 8},
]

def total_hours(logs):
    totals = {}

    for log in logs:
        emp = log.get('emp_id')
        hours = log.get('hours')

        if emp is None or hours is None:
            continue

        if hours < 0:
            continue

        totals[emp] = totals.get(emp, 0) + hours

    return totals

print("Total hour per emp:", total_hours(logs))


        
