import sys

# Check arguments
if len(sys.argv) == 1:
    print("Debes pasar un salario como argumento.")
elif len(sys.argv) > 2:
    print("Debes introducir solamente un salario como argumento.")
else:
    # Begin the IRPF calculator

    # Save the SAB (Salario Bruto Anual)
    sab = int(sys.argv[1])
    print("SAB (Salario Bruto Anual): " + str(sab))

    # Net annual salary
    net = 0 

    # Tax % brackets
    type1tax = 0.19 # 19%
    type2tax = 0.24 # 24%
    type3tax = 0.30 # 30%
    type4tax = 0.37 # 37%
    type5tax = 0.45 # 45%
    
    # Var helper
    carryTax = 0 

    # Calculation logic
    if sab < 12450: # type1
        net = sab - (sab * type1tax)
    elif (sab >= 12450 & sab < 20200): # type2
        type1 = 12450 * type1tax
        carryTax = (sab - 12450) * type2tax

        net = sab - (type1 + carryTax)
    elif (sab >= 20200 & sab < 35200): # type3
        type1 = 12450 * type1tax
        type2 = 7750 * type2tax
        carryTax = (sab - 20200) * type3tax

        net = sab - (type1 + type2 + carryTax)
    elif (sab >= 35200 & sab < 60000): # type4
        type1 = 12450 * type1tax
        type2 = 7750 * type2tax
        type3 = 15000 * type3tax
        carryTax = (sab - 35200) * type4tax

        net = sab - (type1 + type2 + type3 + carryTax)
    elif (sab >= 60000): # type5
        type1 = 12450 * type1tax
        type2 = 7750 * type2tax
        type3 = 15000 * type3tax
        type4 = 24800 * type4tax
        carryTax = (sab - 60000) * type5tax

        net = sab - (type1 + type2 + type3 + type4 + carryTax)

    print("Salario neto anual: " + str("{:,.2f}".format(net)) + "€")

    print("Salario mensual (12 pagas): " + str("{:,.2f}".format(net/12)) + "€")
    print("Salario mensual (14 pagas): " + str("{:,.2f}".format(net/14)) + "€")

