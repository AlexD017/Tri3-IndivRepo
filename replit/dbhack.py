InfoDb = []

InfoDb.append({  
               "CompanyName": "Toyota",  
               "CEO": "Akio Toyoda",  
               "Recent_Models": ["2022 Toyota Corolla Cross", "Toyota bZ4X Concept", "2022 Toyota GR 86", "2022 Toyota GR Supra A91-CF Edition", "2022 Toyota Tacoma TRD Pro"]  
              })  

InfoDb.append({  
               "CompanyName": "Ford",  
               "CEO": "Jim Farley",  
               "Recent_Models": ["2022 Ford Mustang", "2022 Ford Bronco", "2022 Ford Ranger", "2022 Ford F-150", "2022 Ford Explorer"] 
              })

InfoDb.append({  
               "CompanyName": "BMW",  
               "CEO": "Oliver Zipse",  
               "Recent_Models": ["2022 BMW 2 Series Gran Coupe", "2021 BMW 2-Series", "2022 BMW 3-Series", "2022 BMW X1", "2022 BMW X6"]              
              })

InfoDb.append({  
               "CompanyName": "Volkswagen",  
               "CEO": "Herbert Diess",  
               "Recent_Models": ["Volkswagen Golf 8 GTI", "Volkswagen Tiguan Facelift", "Volkswagen Kombi T6", "Volkswagen Crafter Update", "2022 Volkswagen ID.4"] 
              })


def print_data(n):
    print("CompanyName", InfoDb[n]["CompanyName"], "\nCEO", InfoDb[n]["CEO"])  # using comma puts space between values
    print("\t", "Recent Models: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Recent_Models"]))  # join allows printing a string list with separator
    print()


def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)


# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return


# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return


def cars():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion


# this is test driver or code that plays when executed directly,
# versus import which will not run these statements
if __name__ == "__main__":
    cars()
