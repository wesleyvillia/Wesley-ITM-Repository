# Products available
products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

# Product information lookup
def get_product(code):
    return(products[code])
get_product('espresso')

# Product property lookup
def get_property(code,prop):
    return(products[code][prop])
get_property("espresso", "price")

# POS System
def main():
    # create dictionary for product code and quantity
    order_dict = {}
    while True:
        # split input to get the code and the quantity
        order = input("{product_code},{quantity}").split(',')
        if order[0] == '/':
            break
        else:
            code = order[0]
            quantity = int(order[1])
            if code not in products:
                continue
            elif code in order_dict:
                order_dict[code] = order_dict[code] + quantity
            else:
                order_dict[code] = quantity

    receipt = """==\nCODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL"""
    alphabetized_order = sorted(order_dict)
    total = 0
    for product_code in alphabetized_order:
        name = get_property(product_code,'name')
        price = int(get_property(product_code,'price'))
        quant = order_dict[product_code]
        subtotal = price*quant
        total += subtotal
        # there is a bug with the formatting of dalgona, thus the if statement as a special case
        if product_code == 'dalgona':
            receipt += f"\n{product_code}\t\t\t{name}\t\t\t\t{quant}\t\t\t{subtotal}"
        else:
            receipt += f"\n{product_code}\t\t{name}\t\t\t{quant}\t\t\t{subtotal}"
    receipt += f"""\nTotal:\t\t\t\t\t\t\t\t\t\t{total}\n=="""

    with open('receipt.txt','w') as receipt_text:
        receipt_text.write(receipt)

# Call main
main()
