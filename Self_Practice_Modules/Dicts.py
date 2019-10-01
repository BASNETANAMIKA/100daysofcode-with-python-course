# Given the provided cars dictionary:
#
# Get all Jeeps
# Get the first car of every manufacturer.
# Get all vehicles containing the string Trail in their names (should work for other grep too)
# Sort the models (values) alphabetically


cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""

    vehicles = cars['Jeep']
    separator = ', '
    separator.join(vehicles)
    print(separator.join(vehicles))
    return separator.join(vehicles)



def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_model_list = []
    for values in cars.values():
        first_model_list.append(values[0])
    print(first_model_list)
    return first_model_list


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    import re
    matching_models_list = []
    for manufacturer, cars_list in cars.items():
        for car in cars_list:
            match_found = re.search(grep, car, re.IGNORECASE)
            if match_found:
                matching_models_list.append(car)
    print(matching_models_list)
    matching_models_list.sort()
    return matching_models_list


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
    sorted alphabetically"""
    for model, car_list in cars.items():
        print(car_list)
        car_list.sort()
        # prints car_list.sort() returns None
        cars[model] = car_list

    print(cars)
    return cars


if __name__=="__main__":
    # get_all_jeeps()
    # get_first_model_each_manufacturer()
    get_all_matching_models(grep="CO")
    # get_all_matching_models()
    # sort_car_models()