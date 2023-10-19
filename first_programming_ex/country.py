
## This module defines and tests a Country class
#

import argparse
import textwrap

class Country:

    _descriptionDocs = textwrap.dedent("""
    
    A class to represent a country with name, population, and area attributes
    
    Class variables:
    
        _listNames: a list to keep track of names of the countries that were instantiated 
        _listPopulations: a list to keep track of populations of the countries that were instantiated 
        _listAreas: a list to keep track of areas of the countries that were instantiated 
        _countriesDict: a dictionary with keys being the names of countries that were instantiated and 	
	                    values being tuples with population and area of a country at the first 
	                    and second positions respectively 
    
    Instance variables:	
    
        _name: name of a country
	    _population: population of a country (in million people)
	    _area: area of a country (in thousand of square kilometers)
    
    Public methods:
    
        getCountryLargestAreaListImplement()
            Finds the country with the largest area among the instances that were defined, 
                uses Class variable of type list for this purpose.
            @return name of the country with the largest area among the instances that were defined
    
    
        getCountryLargestPopulationListImplement()
            Finds the country with the largest population among the instances that were 
                defined, uses Class variable of type list for this purpose.
            @return name of the country with the largest population among the instances that
                were defined
    
    
        getCountryLargestPopDensityListImplement()
            Finds the country with the largest population density among the instances that 
                were defined, uses Class variable of type list for this purpose.
            @return name of the country with the largest population density among the  
                instances that were defined
    
    
        getCountryLargestAreaDictImplement()
            Finds the country with the largest area among the instances that were defined, 
                uses Class variable of type dictionary for this purpose.
            @return name of the country with the largest area among the instances that were 
                defined
    
    
        getCountryLargestPopulationDictImplement()
            Finds the country with the largest population among the instances that were   
                defined, uses Class variable of type dictionary for this purpose.
            @return name of the country with the largest population among the instances that
                were defined
    
    
        getCountryLargestPopDensityDictImplement() 
            Finds the country with the largest population density among the instances that 
                were defined, uses Class variable of type dictionary for this purpose.
            @return name of the country with the largest population density among the  
                instances that were defined
    """)

    _epilogDocs = textwrap.dedent("""
    
    Examples of use:
            Finland = Country("Finland", 5.5, 338462)
            assert Finland.getCountryLargestAreaListImplement() == "Norway"
            assert Norway.getCountryLargestAreaDictImplement() == "Norway"
            assert Finland.getCountryLargestPopDensityListImplement() == "Finland"
            assert Finland.getCountryLargestPopDensityDictImplement() == "Finland"
            Sweden = Country("Sweden", 10.4, 528447)
            assert Norway.getCountryLargestPopulationDictImplement() == "Sweden"
            Denmark = Country("Denmark", 5.9, 42920)
            assert Sweden.getCountryLargestAreaListImplement() == "Sweden"
            assert Denmark.getCountryLargestPopulationListImplement() == "Sweden"
            assert Finland.getCountryLargestPopDensityListImplement() == "Denmark"
    
    """)

    _listNames = []
    _listPopulations = []
    _listAreas = []

    _countriesDict = {}

    ## Constructs an object
    #
    def __init__(self, name, population, area):
        
        self._parser = argparse.ArgumentParser(
            description = Country._descriptionDocs,
            epilog = Country._epilogDocs,
            
            # make sure that the documentation is represented nicely 
            # in the terminal
            formatter_class = argparse.RawTextHelpFormatter)
        
        # call parse_args() to process documentation so that
        # the documentation will be shown if this programm is called from
        # the terminal with -h or --help flags
        self._parser.parse_args()

        self._name = name
        self._population = population
        self._area = area

        # list implementation
        Country._listNames.append(name)
        Country._listPopulations.append(population)
        Country._listAreas.append(area)

        # dict implementation
        # key: country name, value: tuple with population at the first position,
        # and area at the second position
        # 
        Country._countriesDict[name] = (population, area)


    ## Searches for a country with the largest area among the instances
    # of this class that were created previously (using list classes)
    # @return name of the country with the largest area
    def getCountryLargestAreaListImplement(self):
        
        # gets a position in a list of areas of country with 
        # the largest area 
        pos = Country._listAreas.index(max(Country._listAreas))

        # uses the index to extract the name of the country
        return Country._listNames[pos]

    ## Searches for a country with the largest population among the instances
    # of this class that were created previously (using list classes)
    # @return name of the country with the largest population 
    def getCountryLargestPopulationListImplement(self):
        
        # gets a position in a list of areas of country with 
        # the largest population
        pos = Country._listPopulations.index(max(Country._listPopulations))

        # uses the index to extract the name of the country
        return Country._listNames[pos]
    
    ## Searches for a country with the largest population density among
    # the instances of this class that were created previously (using list classes)
    # @return name of the country with the largest population density
    def getCountryLargestPopDensityListImplement(self):
        
        # create local variables to find an index of a contry with 
        # the largest density

        # the default value is equal to 0 
        # to avoid a possibility of index being out of range
        pos = 0
        
        # the defulat value is equal to -1
        # so that in any case it is going to be replaced with 
        # an actual value for density
        max_density = -1
        
        # we extract the number of countries in order to iterate over 
        # each instance
        no_countries = len(Country._listNames)

        for i in range(no_countries):
            
            # calculate density for each country
            density = Country._listPopulations[i] / Country._listAreas[i]
            
            if density > max_density:
                # update position of a country with the largest population density so far
                pos = i
                # update density of a country with the largest population density so far
                max_density = density

        # extract the name of country with the largest population density
        return Country._listNames[pos]

    ## Searches for a country with the largest area among the instances
    # of this class that were created previously (using dict classes)
    # @return name of the country with the largest area
    def getCountryLargestAreaDictImplement(self):
        
        # initialize name variable for the name of a country with the largest area 
        name = None

        # max_area being equal to -1 initially 
        # so that it will be changed after the first iteration of the for loop
        max_area = -1

        for country_name in Country._countriesDict:

            # in _countriesDict dictionary each value is a tuple with population at the second position
            if Country._countriesDict[country_name][1] > max_area:

                # update name of the country with the largest area so far
                name = country_name
                # update area of the country with the largest area so far
                max_area = Country._countriesDict[country_name][1]

        # return a name of the country with the largest area
        return name

    ## Searches for a country with the largest population among the instances
    # of this class that were created previously (using dict classes)
    # @return name of the country with the largest population 
    def getCountryLargestPopulationDictImplement(self):
        
        # initialize name variable for the name of a country with the largest population 
        name = None

        # max_population being equal to -1 initially
        # so that it will be changed after the first iteration of the for loop
        max_population = -1

        for country_name in Country._countriesDict:
            
            # in _countriesDict dictionary each value is a tuple with population at the first position
            if Country._countriesDict[country_name][0] > max_population:
                
                # update name of the country with the largest population so far
                name = country_name
                # update population of the country with the largest population so far
                max_population = Country._countriesDict[country_name][0]

        # return a name of the country with the largest population
        return name
    
    ## Searches for a country with the largest population density among
    # the instances of this class that were created previously (using dict classes)
    # @return name of the country with the largest population density
    # 
    def getCountryLargestPopDensityDictImplement(self):
        
        # initialize name variable for the name of a country with the largest population density
        name = None

        # max_pop_density being equal to -1 initially
        # so that it will be changed after the first iteration of the for loop
        max_pop_density = -1

        for country_name in Country._countriesDict:
            pop_density = Country._countriesDict[country_name][0] / Country._countriesDict[country_name][1]
            
            if pop_density > max_pop_density:
                # update name of the country with the largest population density so far
                name = country_name
                # update population of the country with the largest population density so far
                max_pop_density = pop_density

        # return a name of the country with the largest population density
        return name 
    


if __name__ == "__main__":
    Norway = Country("Norway", 5.4, 385207)
    Finland = Country("Finland", 5.5, 338462)

    assert Finland.getCountryLargestAreaListImplement() == "Norway"
    assert Norway.getCountryLargestAreaDictImplement() == "Norway"
    assert Finland.getCountryLargestPopDensityListImplement() == "Finland"
    assert Finland.getCountryLargestPopDensityDictImplement() == "Finland"

    Sweden = Country("Sweden", 10.4, 528447)

    assert Norway.getCountryLargestPopulationDictImplement() == "Sweden"

    Denmark = Country("Denmark", 5.9, 42920)

    assert Sweden.getCountryLargestAreaListImplement() == "Sweden"
    assert Denmark.getCountryLargestPopulationListImplement() == "Sweden"
    assert Finland.getCountryLargestPopDensityListImplement() == "Denmark"

    print("Tests run successfully")
