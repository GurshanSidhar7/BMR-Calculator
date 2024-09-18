#Functions

#BMR Calculator for Man
def bmr_calc_Man(weight, height, age):
    BMR_VAL_MALE= (10*weight) + (6.25*height) - (5*age) + 5

    return BMR_VAL_MALE

#BMR Calculator for Woman
def bmr_calc_Woman(weight, height, age):
    BMR_VAL_WOMAN= (10*weight) + (6.25*height) - (5*age) - 5

    return BMR_VAL_WOMAN


