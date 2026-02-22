def premium_crops(prices):
    premium = []
    for price in prices:
        if price > 2000:
            premium.append(price)
    print("Premium Crops:", premium)
premium_crops([1500, 2500, 1800, 3200])