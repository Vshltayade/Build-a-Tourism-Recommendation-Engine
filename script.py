# Now let’s create some data that we’re going to use to test the functionality that we create for The Boredless Tourist.
# The first is our list of destinations that we’re going to be using.
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

# And let’s define a test traveler to see how our functionality is working so far.
# This is a traveler (a user of The Boredless Tourist application) whose name is Erin Wilkes who likes
# historical buildings and art.
# Erin is in China right now, hopefully we can find some good places to show her.
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


# Now that we have test data for a traveler and a list of destinations that we can use, we can start building some of
# the Boredless Tourist‘s functionality.
# When a traveler arrives at a destination, we want to know where they are! Since we use lists for all of our data —
# we are going to identify each location based on its index in our destinations list. But we need to retrieve
# that index first.
def get_destination_index(destination):
    #  find the index of destination and save the results into a variable called destination_index.
    destination_index = destinations.index(destination)
    return destination_index


# print(get_destination_index("Los Angeles, USA")) => 2

# access the traveler’s destination string and save it into traveler_destination.
def get_traveler_location(traveler):
    # The destination string of our example traveler is at index 1. Get the traveler’s destination string by calling
    # traveler[1] and saving that to traveler_destination.
    traveler_destination = test_traveler[1]
    # Use traveler_destination along with get_destination_index() to retrieve the index of the destination where the
    # traveler is. Save the index of the traveler’s destination into the variable traveler_destination_index.
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


# Create a variable called test_destination_index. Save the results of calling get_traveler_location()
# with our test_traveler.
test_destination_index = get_traveler_location(test_traveler)
# print(test_destination_index) => 1

# Now we want to create and maintain a list of attractions. Let’s start by defining a list called attractions.
# Actually, we want attractions to be an empty list for every destination in destinations.
attractions = [[] for i in range(5)]


# Now let’s create a function called add_attraction(). This function should take two parameters: destination,
# the name of the location and attraction, the attraction.
def add_attraction(destination, attraction):
    # First we should attempt to find the index of the destination. Use get_destination_index() with the passed in
    # destination in order to retrieve the index of the destination. Save the results into destination_index.

    # What happens if the destination passed in to add_attraction() doesn't exist?
    # Add a try block and catch the possible ValueError that could happen
    # when you define destination_index.
    try:
        destination_index = get_destination_index(destination)
        # Use the destination_index to find the appropriate list in attractions and save that list to
        # attractions_for_destination.
        attractions_for_destination = attractions[destination_index]
        # Append the attraction passed into add_attraction to the list attractions_for_destination.
        attractions_for_destination.append(attraction)
        return
    except ValueError:
        # Here we don’t want to add an attraction to a destination we don’t have, so simply return.
        return


# add attractions to the destinations by calling add_attraction
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions)
