import data


# Part 1
def population_total(l: list[data.CountyDemographics]) -> int:
    total_population = 0
    for county in l:
        total_population += county.population['2014 Population']
    return total_population

# Part 2
def filter_by_state(counties: list[data.CountyDemographics], state: str) -> list[data.CountyDemographics]:
    filtered_counties = []
    for county in counties:
        if county.state == state:
            filtered_counties.append(county)
    return filtered_counties

# Part 3
def population_by_education(counties: list[data.CountyDemographics], education_key: str) -> float:
    """
    Calculate total population with specified education level across counties.
    Returns 0 if education_key doesn't exist.
    """
    total_population = 0.0
    for county in counties:
        if education_key in county.education:
            population_2014 = county.population['2014 Population']
            education_percentage = county.education[education_key]
            total_population += (population_2014 * education_percentage / 100)
    return total_population

def population_by_ethnicity(counties: list[data.CountyDemographics], ethnicity_key: str) -> float:
    """
    Calculate total population of specified ethnicity across counties.
    Returns 0 if ethnicity_key doesn't exist.
    """
    total_population = 0.0
    for county in counties:
        if ethnicity_key in county.ethnicities:
            population_2014 = county.population['2014 Population']
            ethnicity_percentage = county.ethnicities[ethnicity_key]
            total_population += (population_2014 * ethnicity_percentage / 100)
    return total_population

def population_below_poverty_level(counties: list[data.CountyDemographics]) -> float:

    # Calculate total population below poverty level across counties.

    total_population = 0.0
    for county in counties:
        population_2014 = county.population['2014 Population']
        poverty_percentage = county.income['Persons Below Poverty Level']
        total_population += (population_2014 * poverty_percentage / 100)
    return total_population

# Part 4
def percent_by_education(counties: list[data.CountyDemographics], education_key: str) -> float:
    total_pop = population_total(counties)
    if total_pop == 0:
        return 0
    return (population_by_education(counties, education_key) / total_pop) * 100

def percent_by_ethnicity(counties: list[data.CountyDemographics], ethnicity_key: str) -> float:
    total_pop = population_total(counties)
    if total_pop == 0:
        return 0
    return (population_by_ethnicity(counties, ethnicity_key) / total_pop) * 100

def percent_below_poverty_level(counties: list[data.CountyDemographics]) -> float:
    total_pop = population_total(counties)
    if total_pop == 0:
        return 0
    return (population_below_poverty_level(counties) / total_pop) * 100

# Part 5
# Education section
def education_greater_than(counties: list[data.CountyDemographics], education_key: str, threshold: float) -> list[data.CountyDemographics]:
    """
    Return list of counties where education level exceeds threshold percentage.
    """
    result = []
    for county in counties:
        if education_key in county.education and county.education[education_key] > threshold:
            result.append(county)
    return result

def education_less_than(counties: list[data.CountyDemographics], education_key: str, threshold: float) -> list[data.CountyDemographics]:
    """
    Return list of counties where education level is below threshold percentage.
    """
    result = []
    for county in counties:
        if education_key in county.education and county.education[education_key] < threshold:
            result.append(county)
    return result

# Ethnicity Section
def ethnicity_greater_than(counties: list[data.CountyDemographics], ethnicity_key: str, threshold: float) -> list[data.CountyDemographics]:
    """
    Return list of counties where ethnicity percentage exceeds threshold.
    """
    result = []
    for county in counties:
        if ethnicity_key in county.ethnicities and county.ethnicities[ethnicity_key] > threshold:
            result.append(county)
    return result

def ethnicity_less_than(counties: list[data.CountyDemographics], ethnicity_key: str, threshold: float) -> list[data.CountyDemographics]:
    """
    Return list of counties where ethnicity percentage is below threshold.
    """
    result = []
    for county in counties:
        if ethnicity_key in county.ethnicities and county.ethnicities[ethnicity_key] < threshold:
            result.append(county)
    return result

# Poverty Section
def below_poverty_level_greater_than(counties: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    """
    Return list of counties where poverty level exceeds threshold percentage.
    """
    result = []
    for county in counties:
        if county.income["Persons Below Poverty Level"] > threshold:
            result.append(county)
    return result

def below_poverty_level_less_than(counties: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    """
    Return list of counties where poverty level is below threshold percentage.
    """
    result = []
    for county in counties:
        if county.income["Persons Below Poverty Level"] < threshold:
            result.append(county)
    return result