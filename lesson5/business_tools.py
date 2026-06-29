
def calculate_profit(revenue, costs):
    """Return profit from revenue and costs."""
    return revenue - costs


def classify_customer(total_spent):
    """Return a customer category based on total spending."""
    if total_spent >= 1000:
        return "Gold"
    elif total_spent >= 500:
        return "Silver"
    else:
        return "Bronze"
