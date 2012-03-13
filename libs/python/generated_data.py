# helper functions to generate data on the fly, such as usernames, phone numbers and first/last names
# TODO: add ppuser access

import datetime, random   
def firstName():
    global _firstNames
    return random.choice(_firstNames)
    
def lastName():
    global _lastNames
    return random.choice(_lastNames)
def streetName():
    global _streetNames
    return random.choice(_streetNames)

def uid():
    return datetime.datetime.now().strftime("%y%j%H%M%S")
    
def randomReplaceToken(format, token = '#', options = None):
    if options == None:
        options = range(10)
    rv = ""
    for c in format:
        if c == token[0]:
            rv = rv + str(random.choice(options))
        else:
            rv = rv + c
    return rv

# DATA    
_firstNames = ["Johnny", "Kate","Alice","Bob","Derp","Gunther","Makoto","River",
                "Kaiser","Buddy","Lucy","Olivia","T.J.","Freddie","Zeus","Thor"
                "Carl", "Dougie", "Eloise", "Rachel", "Marty", "Hal", "Ty",
                "Homer", "Marge", "Bart", "Lisa", "Maggie", "Wayne", "Garth"]

_lastNames = ["Smith","McDerpington","Jones","Public","Kobayashi","Soze","Mercury",
                "Li","Hernandez","Flanders", "Simpson", "Vasquez-Escobar"]

_streetNames = ["Church Street", "High Street", "Main Street North", "Elm Street",
                "Chestnut Street", "Main Street South", "Maple Street", "Broad Street",
                "Center Street", "Maple Avenue", "Washington Street", "Walnut Street",
                "2nd Street", "Main Street West", "Pine Street", "South Street",
                "Park Avenue", "Union Street", "Water Street", "Main Street East",
                "School Street", "North Street", "Spring Street", "Oak Street",
                "River Road", "Prospect Street", "Market Street", "Court Street",
                "Park Street", "Washington Avenue", "Front Street", "3rd Street",
                "Cedar Street", "Cherry Street", "Highland Avenue", "Central Avenue",
                "Spruce Street", "West Street", "Franklin Street", "Bridge Street",
                "State Street", "East Street", "Locust Street", "Pleasant Street",
                "Ridge Road", "Church Road", "Lincoln Avenue", "4th Street",
                "Dogwood Drive", "Green Street", "Pennsylvania Avenue", "1st Street",
                "Adams Street", "Mill Street", "Route 1", "Winding Way", "Hill Street",
                "Liberty Street", "Park Place", "2nd Avenue", "Academy Street",
                "Cherry Lane", "Grove Street", "Hillside Avenue", "Jefferson Avenue",
                "Meadow Lane", "River Street", "Route 30", "Route 6", "5th Street",
                "Broadway", "Elizabeth Street", "Hickory Lane", "Jefferson Street",
                "Lincoln Street", "Beech Street", "Jackson Street", "Madison Avenue",
                "Pearl Street", "Railroad Street", "Vine Street", "12th Street",
                "1st Avenue", "3rd Avenue", "5th Avenue", "Arch Street", "Clinton Street",
                "Fairway Drive", "Heather Lane", "Holly Drive", "Mill Road", "New Street",
                "Pheasant Run", "Route 41", "Route 7", "Route 9", "Sherwood Drive",
                "Strawberry Lane", "Wall Street", "Windsor Court", "14th Street",
                "5th Street South", "6th Street West", "Andover Court", "Ashley Court",
                "Briarwood Drive", "Bridle Lane", "Brook Lane", "Cambridge Road",
                "Clark Street", "Fieldstone Drive", "Fulton Street", "Grand Avenue",
                "Grant Street", "Heather Court", "Hickory Street", "Holly Court",
                "Jackson Avenue", "Lafayette Street", "Lakeview Drive", "Linda Lane",
                "Madison Court", "Maple Lane", "Old York Road", "Orchard Avenue",
                "Park Drive", "Park Road", "Pin Oak Drive", "Primrose Lane",
                "Rosewood Drive", "Schoolhouse Lane", "Sheffield Drive", "Spruce Avenue",
                "Summer Street", "Summit Street", "Sycamore Drive", "Valley Drive",
                "Valley View Road", "Victoria Court", "Virginia Avenue", "Warren Avenue",
                "Westminster Drive", "Williams Street", "Wood Street", "Woodland Avenue"]