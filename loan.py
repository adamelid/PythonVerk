item_cost = float(input("Input the cost of the item in $: "))

#stofna breytur.
afborgun = 0.0
greiddir_vext = 0.0
eftir_skuld = item_cost
total_greiddir_vextir = 0.0
rate = 0.0
number_month = 1
total_months = 0

#Ákveða vaxtaprósentu.
if item_cost <= 1000:
    rate = 1.015
else:
    rate = 1.02

#Loopa í gegnum greiðslur.
while eftir_skuld > 0:
    if eftir_skuld * rate >= 50:
        afborgun = 50.0
    else:
        afborgun = eftir_skuld * rate

    greiddir_vext = eftir_skuld * (rate-1)
    eftir_skuld += greiddir_vext - afborgun
    print("Month: "+str(number_month)+" Payment: "+str(round(afborgun, 2))+" Interest paid: "+str(round(greiddir_vext, 2))+" Remaining debt: "+str(round(eftir_skuld, 2)))
    total_greiddir_vextir += greiddir_vext
    number_month+=1

total_months = number_month-1
print("\nNumber of months: " + str(total_months))
print("Total interest paid: " + str(round(total_greiddir_vextir, 2)))