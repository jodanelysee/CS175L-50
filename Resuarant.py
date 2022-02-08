#CS175-50L
#Jodan Elysee
#Restuarant.py
vege = False
veg = False
glu = False
response1 = input('Is anyone in your party a vegetarian?' )
if response1 == 'yes':
    vege = True
response2 = input('Is anyone in your party a vegan?' )
if response2 == 'yes':
    veg = True
response3 = input('Is anyone in your party gluten-free?' )
if response3 == 'yes':
    glu = True

if vege == True and glu == True:
    if veg == False:
        print('Your choices for restaurants are:\n')
        print('Main Street Pizza Company\nCorners Cafe\nThe Chef\'s Kitchen')
if vege == True and glu == True and veg ==True:
    print('Your choices for restaurants are:\n')
    print('Corners Cafe\nThe Chef\'s Kitchen')
if glu == True and veg == True:
    if vege == False:
        print('Your choices for restuarants are:\n')
        print('Corners Cafe\nChef\'s Kitchen')
if vege == True and veg == True:
    if glu == False:
        print('Your choices for restuarants are:\n')
        print('Corners Cafe\nChef\'s Kitchen')
if vege == False and veg == False and glu == False:
    print('Your choices for restuarants are:\n')
    print('Main Street Pizza Company\nCorners Cafe\nThe Chef\'s Kitchen\nJoe\'s Gourmet Burgers\nMama\'s Fine Italian')


    
    
    
