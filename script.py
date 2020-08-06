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