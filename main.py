from pyscript import display, document

def computing_order(a):
    document.getElementById('for').innerHTML = "Order for:"
    document.getElementById('where').innerHTML = "Address:"
    document.getElementById('no_').innerHTML = "Contact Number:"
    document.getElementById('total').innerHTML = "Total:"
    document.getElementById('incomplete').innerHTML = ""

   
    name = document.getElementById('name').value # collecting value from an input field
    address = document.getElementById('address').value 
    number = document.getElementById('number').value
    total = 0

    # Menu items
    if document.getElementById('super_pretzel').checked:
        total += float(document.getElementById('super_pretzel').value)

    if document.getElementById('pretzel_bum').checked:
        total += float(document.getElementById('pretzel_bum').value)

    if document.getElementById('coffee').checked:
        total += float(document.getElementById('coffee').value)

    if document.getElementById('pretzel_crisps').checked:
        total += float(document.getElementById('pretzel_crisps').value)

    if document.getElementById('cheese_dip').checked:
        total += float(document.getElementById('cheese_dip').value)

    
    if total == 0 or not name or not address or not number:
        display("⚠ Please complete your order.", target="incomplete")
        return


    display(f"Order for: {name}", target="for")
    display(f"Address: {address}", target="where")
    display(f"Contact Number: {number}", target="no_")
    display(f"Total: ₱{total}", target="total")
