from ortools.linear_solver import pywraplp
from geopy.distance import geodesic

# Suburb coordinates (Latitude, Longitude)
suburb_coordinates = {
    "Ingleburn": [-34.004880, 150.875907],
    "Glenwood": [-33.721380, 150.928880],
    "Sefton": [-33.888700, 151.022030],
    "Hornsby": [-33.703442, 151.101596],
    "Pymble": [-33.749210, 151.134140],
    "Burwood": [-33.877421, 151.104046],
    "Wiley Park": [-33.921799, 151.045529],
    "Northbridge": [-33.818135, 151.209827],
    "Leppington": [-33.919801, 150.820588],
    "Dundas": [-33.803740, 151.039730],
    "North Parramatta": [-33.797508, 151.022233],
    "West Pennant Hills": [-33.747501, 151.045845],
    "Cabramatta": [-33.890830, 150.936550],
    "Hurstville": [-33.967650, 151.102630],
    "Lakemba": [-33.918480, 151.074800],
    "Kingsgrove": [-33.945930, 151.094120],
    "Thornleigh": [-33.723507, 151.076541],
    "Castle Hill": [-33.731040, 151.003190],
    "Cheltenham": [-33.806240, 151.072100],
    "West Ryde": [-33.811810, 151.088900],
    "Kogarah": [-33.961040, 151.137140],
    "Pagewood": [-33.937780, 151.213020],
    "Rosebery": [-33.922780, 151.204340]
}

def dist_from_driver1(suburb2):
    driver1_coordinates = suburb_coordinates[drivers["driver1"]]
    coordinates_suburb1 = (driver1_coordinates[0], driver1_coordinates[1]) #lat, long
    coordinates_suburb2 = (suburb2[0], suburb2[1])

    distance = geodesic(coordinates_suburb1, coordinates_suburb2).kilometers
    return distance

def dist_from_driver2(suburb2):
    driver2_coordinates = suburb_coordinates[drivers["driver2"]]
    coordinates_suburb1 = (driver2_coordinates[0], driver2_coordinates[1]) #lat, long
    coordinates_suburb2 = (suburb2[0], suburb2[1])

    distance = geodesic(coordinates_suburb1, coordinates_suburb2).kilometers
    return distance

def dist_from_driver3(suburb2):
    driver3_coordinates = suburb_coordinates[drivers["driver3"]]
    coordinates_suburb1 = (driver3_coordinates[0], driver3_coordinates[1]) #lat, long
    coordinates_suburb2 = (suburb2[0], suburb2[1])

    distance = geodesic(coordinates_suburb1, coordinates_suburb2).kilometers
    return distance

def dist_from_driver4(suburb2):
    driver4_coordinates = suburb_coordinates[drivers["driver4"]]
    coordinates_suburb1 = (driver4_coordinates[0], driver4_coordinates[1]) #lat, long
    coordinates_suburb2 = (suburb2[0], suburb2[1])

    distance = geodesic(coordinates_suburb1, coordinates_suburb2).kilometers
    return distance

def dist_from_driver5(suburb2):
    driver5_coordinates = suburb_coordinates[drivers["driver5"]]
    coordinates_suburb1 = (driver5_coordinates[0], driver5_coordinates[1]) #lat, long
    coordinates_suburb2 = (suburb2[0], suburb2[1])

    distance = geodesic(coordinates_suburb1, coordinates_suburb2).kilometers
    return distance

# Driver locations
drivers = {
    "driver1": "Ingleburn",
    "driver2": "Glenwood",
    # "driver3": "Sefton",
    "driver4": "Hornsby",
    "driver5": "Pymble"
}

# Passenger locations
passengers = {
    "passenger1": "Burwood",
    "passenger2": "Wiley Park",
    # "passenger3": "Northbridge",
    "passenger4": "Leppington",
    "passenger5": "Dundas",
    "passenger6": "North Parramatta",
    "passenger7": "West Pennant Hills",
    "passenger8": "Cabramatta",
    "passenger9": "Hurstville",
    "passenger10": "Lakemba",
    "passenger11": "Kingsgrove",
    "passenger12": "Thornleigh",
    # "passenger13": "Castle Hill",
    # "passenger14": "Cheltenham",
    "passenger15": "West Ryde",
    # "passenger16": "Kogarah",
    "passenger17": "Pagewood",
    # "passenger18": "Rosebery"
}

# Sample distance matrix
distances = {
    "driver1": {
        "passenger1": dist_from_driver1(suburb_coordinates[passengers["passenger1"]]),
        "passenger2": dist_from_driver1(suburb_coordinates[passengers["passenger2"]]),
        # "passenger3": dist_from_driver1(suburb_coordinates[passengers["passenger3"]]),
        "passenger4": dist_from_driver1(suburb_coordinates[passengers["passenger4"]]),
        "passenger5": dist_from_driver1(suburb_coordinates[passengers["passenger5"]]),
        "passenger6": dist_from_driver1(suburb_coordinates[passengers["passenger6"]]),
        "passenger7": dist_from_driver1(suburb_coordinates[passengers["passenger7"]]),
        "passenger8": dist_from_driver1(suburb_coordinates[passengers["passenger8"]]),
        "passenger9": dist_from_driver1(suburb_coordinates[passengers["passenger9"]]),
        "passenger10": dist_from_driver1(suburb_coordinates[passengers["passenger10"]]),
        "passenger11": dist_from_driver1(suburb_coordinates[passengers["passenger11"]]),
        "passenger12": dist_from_driver1(suburb_coordinates[passengers["passenger12"]]),
        # "passenger13": dist_from_driver1(suburb_coordinates[passengers["passenger13"]]),
        # "passenger14": dist_from_driver1(suburb_coordinates[passengers["passenger14"]]),
        "passenger15": dist_from_driver1(suburb_coordinates[passengers["passenger15"]]),
        # "passenger16": dist_from_driver1(suburb_coordinates[passengers["passenger16"]]),
        "passenger17": dist_from_driver1(suburb_coordinates[passengers["passenger17"]]),
        # "passenger18": dist_from_driver1(suburb_coordinates[passengers["passenger18"]])
    },
    "driver2": {
        "passenger1": dist_from_driver2(suburb_coordinates[passengers["passenger1"]]),
        "passenger2": dist_from_driver2(suburb_coordinates[passengers["passenger2"]]),
        # "passenger3": dist_from_driver2(suburb_coordinates[passengers["passenger3"]]),
        "passenger4": dist_from_driver2(suburb_coordinates[passengers["passenger4"]]),
        "passenger5": dist_from_driver2(suburb_coordinates[passengers["passenger5"]]),
        "passenger6": dist_from_driver2(suburb_coordinates[passengers["passenger6"]]),
        "passenger7": dist_from_driver2(suburb_coordinates[passengers["passenger7"]]),
        "passenger8": dist_from_driver2(suburb_coordinates[passengers["passenger8"]]),
        "passenger9": dist_from_driver2(suburb_coordinates[passengers["passenger9"]]),
        "passenger10": dist_from_driver2(suburb_coordinates[passengers["passenger10"]]),
        "passenger11": dist_from_driver2(suburb_coordinates[passengers["passenger11"]]),
        "passenger12": dist_from_driver2(suburb_coordinates[passengers["passenger12"]]),
        # "passenger13": dist_from_driver2(suburb_coordinates[passengers["passenger13"]]),
        # "passenger14": dist_from_driver2(suburb_coordinates[passengers["passenger14"]]),
        "passenger15": dist_from_driver2(suburb_coordinates[passengers["passenger15"]]),
        # "passenger16": dist_from_driver2(suburb_coordinates[passengers["passenger16"]]),
        "passenger17": dist_from_driver2(suburb_coordinates[passengers["passenger17"]]),
        # "passenger18": dist_from_driver2(suburb_coordinates[passengers["passenger18"]])
    },
    # "driver3": {
    #     "passenger1": dist_from_driver3(suburb_coordinates[passengers["passenger1"]]),
    #     "passenger2": dist_from_driver3(suburb_coordinates[passengers["passenger2"]]),
    #     "passenger3": dist_from_driver3(suburb_coordinates[passengers["passenger3"]]),
    #     # "passenger4": dist_from_driver3(suburb_coordinates[passengers["passenger4"]]),
    #     "passenger5": dist_from_driver3(suburb_coordinates[passengers["passenger5"]]),
    #     "passenger6": dist_from_driver3(suburb_coordinates[passengers["passenger6"]]),
    #     "passenger7": dist_from_driver3(suburb_coordinates[passengers["passenger7"]]),
    #     "passenger8": dist_from_driver3(suburb_coordinates[passengers["passenger8"]]),
    #     "passenger9": dist_from_driver3(suburb_coordinates[passengers["passenger9"]]),
    #     "passenger10": dist_from_driver3(suburb_coordinates[passengers["passenger10"]]),
    #     "passenger11": dist_from_driver3(suburb_coordinates[passengers["passenger11"]]),
    #     "passenger12": dist_from_driver3(suburb_coordinates[passengers["passenger12"]]),
    #     # "passenger13": dist_from_driver3(suburb_coordinates[passengers["passenger13"]]),
    #     "passenger14": dist_from_driver3(suburb_coordinates[passengers["passenger14"]]),
    #     "passenger15": dist_from_driver3(suburb_coordinates[passengers["passenger15"]]),
    #     # "passenger16": dist_from_driver3(suburb_coordinates[passengers["passenger16"]]),
    #     "passenger17": dist_from_driver3(suburb_coordinates[passengers["passenger17"]]),
    #     "passenger18": dist_from_driver3(suburb_coordinates[passengers["passenger18"]])
    # },
    "driver4": {
        "passenger1": dist_from_driver4(suburb_coordinates[passengers["passenger1"]]),
        "passenger2": dist_from_driver4(suburb_coordinates[passengers["passenger2"]]),
        # "passenger3": dist_from_driver4(suburb_coordinates[passengers["passenger3"]]),
        "passenger4": dist_from_driver4(suburb_coordinates[passengers["passenger4"]]),
        "passenger5": dist_from_driver4(suburb_coordinates[passengers["passenger5"]]),
        "passenger6": dist_from_driver4(suburb_coordinates[passengers["passenger6"]]),
        "passenger7": dist_from_driver4(suburb_coordinates[passengers["passenger7"]]),
        "passenger8": dist_from_driver4(suburb_coordinates[passengers["passenger8"]]),
        "passenger9": dist_from_driver4(suburb_coordinates[passengers["passenger9"]]),
        "passenger10": dist_from_driver4(suburb_coordinates[passengers["passenger10"]]),
        "passenger11": dist_from_driver4(suburb_coordinates[passengers["passenger11"]]),
        "passenger12": dist_from_driver4(suburb_coordinates[passengers["passenger12"]]),
        # "passenger13": dist_from_driver4(suburb_coordinates[passengers["passenger13"]]),
        # "passenger14": dist_from_driver4(suburb_coordinates[passengers["passenger14"]]),
        "passenger15": dist_from_driver4(suburb_coordinates[passengers["passenger15"]]),
        # "passenger16": dist_from_driver4(suburb_coordinates[passengers["passenger16"]]),
        "passenger17": dist_from_driver4(suburb_coordinates[passengers["passenger17"]]),
        # "passenger18": dist_from_driver4(suburb_coordinates[passengers["passenger18"]])
    },
    "driver5": {
        "passenger1": dist_from_driver5(suburb_coordinates[passengers["passenger1"]]),
        "passenger2": dist_from_driver5(suburb_coordinates[passengers["passenger2"]]),
        # "passenger3": dist_from_driver5(suburb_coordinates[passengers["passenger3"]]),
        "passenger4": dist_from_driver5(suburb_coordinates[passengers["passenger4"]]),
        "passenger5": dist_from_driver5(suburb_coordinates[passengers["passenger5"]]),
        "passenger6": dist_from_driver5(suburb_coordinates[passengers["passenger6"]]),
        "passenger7": dist_from_driver5(suburb_coordinates[passengers["passenger7"]]),
        "passenger8": dist_from_driver5(suburb_coordinates[passengers["passenger8"]]),
        "passenger9": dist_from_driver5(suburb_coordinates[passengers["passenger9"]]),
        "passenger10": dist_from_driver5(suburb_coordinates[passengers["passenger10"]]),
        "passenger11": dist_from_driver5(suburb_coordinates[passengers["passenger11"]]),
        "passenger12": dist_from_driver5(suburb_coordinates[passengers["passenger12"]]),
        # "passenger13": dist_from_driver5(suburb_coordinates[passengers["passenger13"]]),
        # "passenger14": dist_from_driver5(suburb_coordinates[passengers["passenger14"]]),
        "passenger15": dist_from_driver4(suburb_coordinates[passengers["passenger15"]]),
        # "passenger16": dist_from_driver4(suburb_coordinates[passengers["passenger16"]]),
        "passenger17": dist_from_driver4(suburb_coordinates[passengers["passenger17"]]),
        # "passenger18": dist_from_driver4(suburb_coordinates[passengers["passenger18"]])
    }
}

car_capacities = {
    "driver1": 4,
    "driver2": 4,
    # "driver3": 4,
    "driver4": 4,
    "driver5": 3
}

# Create solver
solver = pywraplp.Solver.CreateSolver('SCIP')

# Create binary decision variables (1 if passenger assigned to driver, 0 otherwise)
assignment = {}
for driver in drivers:
    for passenger in passengers:
        assignment[(driver, passenger)] = solver.IntVar(0, 1, f'{driver}_{passenger}')

# Objective: Minimize total travel distance
objective = solver.Objective()
for driver in drivers:
    for passenger in passengers:
        objective.SetCoefficient(assignment[(driver, passenger)], distances[driver][passenger])
objective.SetMinimization()

# Constraint: Each passenger is assigned to exactly one driver
for passenger in passengers:
    solver.Add(solver.Sum(assignment[(driver, passenger)] for driver in drivers) == 1)

# Constraint: Car capacity
for driver in drivers:
    solver.Add(solver.Sum(assignment[(driver, passenger)] for passenger in passengers) <= car_capacities[driver])

# Solve the problem
status = solver.Solve()

# Output results
if status == pywraplp.Solver.OPTIMAL:
    for driver in drivers:
        print()
        assigned_passengers = [passenger for passenger in passengers if assignment[(driver, passenger)].solution_value() == 1]
        print(f"{driver} will drive: {', '.join(assigned_passengers)}")
        print()

        total_distance = sum(distances[driver][passenger] for passenger in assigned_passengers)
        print(f"Total distance for {driver}: {total_distance:.2f} km")

        for passenger in assigned_passengers:
            print(f"Distance from {driver} to {passenger}: {distances[driver][passenger]:.2f} km")
else:
    print("No solution found.")
