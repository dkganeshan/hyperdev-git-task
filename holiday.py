"""Program for calculating the holiday cost"""
valid_codes = ['ny','ln','pr'] #entered the valid destination codes
#user input for holiday destination
while True: #loop the request until user enter valid cose
    print (" This is the program to calculate your holiday cost. Please enter NY - New york, LN for London and PR for Paris ")
    city_flight = input ("Enter the holiday destination code: ", )
    if city_flight.lower() in valid_codes:
        break # exit the loop
    
#user input for number of nights staying  
num_nights = input ("Enter number of nights of stay: ", )

#user input for number of days of car rental 
rental_days = input("Enter number of days for car rental: ", )

#function for hotel cost
def hotel_cost(num_nights):
    h_cost = int(num_nights)*100
    return h_cost

#function for plane cost  
def plane_cost(city_flight):
    if city_flight.lower() == "ny":
        p_cost =  1000
        
    if city_flight.lower() == "ln":
        p_cost = 750
        
    if city_flight.lower() == "pr":
        p_cost = 500
    return p_cost

#fuction for calculating car rental cost
def car_rental(rental_days):
    c_cost = int(rental_days)*75
    return c_cost

#function for adding up all holiday costs. 
def holiday_cost(p_cost,c_cost,h_cost):
    total_cost = p_cost+c_cost+h_cost
    return total_cost

#Calling all above three function for individual cost
h_cost = hotel_cost(num_nights)
print (f'Hotel cost: {h_cost}')

p_cost = plane_cost(city_flight)
print (f'Plane cost: {p_cost}')

c_cost = car_rental(rental_days)
print(f'Car rental: {c_cost}')


#Calling total_cost function for final cost calculation 
total_cost = holiday_cost(p_cost,c_cost,h_cost)

print(f"Total holiday cost: £{total_cost}")