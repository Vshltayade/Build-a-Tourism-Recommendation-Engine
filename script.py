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

# print(attractions) =>
"""[[['the Louvre', ['art', 'museum']], ['Arc de Triomphe', ['historical site', 'monument']]],
 [['Yu Garden', ['garden', 'historcical site']], ['Yuz Museum', ['art', 'museum']], ['Oriental Pearl Tower',
  ['skyscraper', 'viewing deck']]], [['Venice Beach', ['beach']], ['LACMA', ['art', 'museum']]], [['São Paulo Zoo',
   ['zoo']], ['Pátio do Colégio', ['historical site']]], [['Pyramids of Giza', ['monument', 'historical site']],
    ['Egyptian Museum', ['museum']]]]
"""


# We want to be able to help our traveler’s find the most interesting places in a new city for them. In order to do that
# we need to match their interests with the possible locations in a city.

# Write a function called find_attractions() that takes two parameters: destination, the name of the destination and
# interests, a list of interests.

def find_attractions(destination, interests):
    # We’ll need the city’s destination_index to look up its attractions in our attractions table.
    # Create a variable called destination_index and save the destination’s index to it using get_destination_index()
    destination_index = get_destination_index(destination)
    # Look up that destination’s attractions by indexing into attractions with destination_index.
    # Save this into the variable attractions_in_city.
    attractions_in_city = attractions[destination_index]
    # Create a new list called attractions_with_interest. Make it empty when declaring it,
    # we’ll save attractions into this list if they match one of our interests.
    attractions_with_interest = []
    # Create a loop over attractions_in_city saving each item in the list into the
    # temporary variable possible_attraction.
    for attraction in attractions_in_city:
        possible_attraction = attraction
        # For each attraction, retrieve the tagged information about it.
        # The tags are all saved in the second place (index 1) in the attraction.
        # In the body of the for loop, save the attraction’s tags into the variable attraction_tags.
        attraction_tags = attraction[1]
        # After retrieving the attraction tags, we want to see if any of the given interests are in attraction_tags.
        # In order to do this, we’re going to loop through interests and check if any of them are in attraction_tags.
        for interest in interests:
            # For every interest in interests, check if that interest is in attraction_tags.
            # If the interest is in the attraction_tags, append possible_attraction to attractions_with_interest.
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest


# Let’s test out our function! Call find_attractions() with "Los Angeles, USA" and ['art'] as the two arguments
# and save the results to la_arts.
la_arts = find_attractions("Los Angeles, USA", ['art'])


# print(la_arts) => ['LACMA']

# Now let’s get to the main event, connecting people with the attractions that they are interested in.

def get_attractions_for_traveler(traveler):
    # Let’s separate out the traveler’s data. Save the following data:
    # Save traveler[1] into a variable called traveler_destination.
    # Save traveler[2] into a variable called traveler_interests.

    traveler_destination = traveler[1]
    traveler_interests = traveler[2]

    # Call find_attractions() with the two arguments traveler_destination and traveler_interests.
    # Save the results into traveler_attractions.

    traveler_attractions = find_attractions(traveler_destination, traveler_interests)

    # Create a new string, this is what we’ll want to show our traveler when they open our application:
    interests_string = "Hi "
    interests_string += traveler[0]
    interests_string += ", we think you'll like these places around "
    interests_string += traveler_destination + ": "
    for attr in traveler_attractions:
        interests_string += attr
    return interests_string


smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])

print(smills_france)
# Hi Dereck Smill, we think you'll like these places around Paris, France: Arc de Triomphe
