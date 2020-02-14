


#constants
rf = 0.55
rm = 0.68
r = rf

#input
total_ounces = 6.0
body_weight_in_lbs = 120.0
ac_of_drink = 40.0
elapsed_time_hours = 5.0

#conversions
body_weight_in_grams = body_weight_in_lbs*453.592#convert pounds to grams
vol_of_drinks = total_ounces*29.5735#convert ounces to ml



def calc_bac(vod, acod, bwig, rr, eth):
    acig = vod*(acod/100.0)*0.789
    bac = acig/(bwig*rr)*100.0
    bact = bac - (eth*0.015)
    return bac, bact, acig 

print(calc_bac(vol_of_drinks, ac_of_drink, body_weight_in_grams, r, elapsed_time_hours))