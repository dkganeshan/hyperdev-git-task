"""Program for calculating the holiday cost"""
valid_codes = ['ny','ln','pr'] 

while True: 
    print (" This is the program to calculate your holiday cost. Please enter NY - New york, LN for London and PR for Paris ")
    city_flight = input ("Enter the holiday destination code: ", )
    if city_flight.lower() in valid_codes:
        break 
  
num_nights = input ("Enter number of nights of stay: ", )

 
rental_days = input("Enter number of days for car rental: ", )


def hotel_cost(num_nights):
    h_cost = int(num_nights)*100
    return h_cost

 
def plane_cost(city_flight):
    if city_flight.lower() == "ny":
        p_cost =  1000
        
    if city_flight.lower() == "ln":
        p_cost = 750
        
    if city_flight.lower() == "pr":
        p_cost = 500
    return p_cost


def car_rental(rental_days):
    c_cost = int(rental_days)*75
    return c_cost

 
def holiday_cost(p_cost,c_cost,h_cost):
    total_cost = p_cost+c_cost+h_cost
    return total_cost


h_cost = hotel_cost(num_nights)
print (f'Hotel cost: {h_cost}')

p_cost = plane_cost(city_flight)
print (f'Plane cost: {p_cost}')

c_cost = car_rental(rental_days)
print(f'Car rental: {c_cost}')



total_cost = holiday_cost(p_cost,c_cost,h_cost)

print(f"Total holiday cost: £{total_cost}")