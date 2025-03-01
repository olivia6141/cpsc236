def sales_tax(total):
    salest = .06 * total
    return round(salest,2)

def totalaftertax(total, salest):
    return round(total + salest,2)