import data
import build_data
import unittest

from hw3 import population_total, filter_by_state, population_by_education, population_by_ethnicity, population_below_poverty_level, percent_by_education, percent_by_ethnicity, percent_below_poverty_level, education_less_than, education_greater_than, ethnicity_greater_than, ethnicity_less_than, below_poverty_level_less_than, below_poverty_level_greater_than

# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

class TestCases(unittest.TestCase):
    pass

    # Part 1
    # test population_total
    def test_population_total(self):
        assert population_total(reduced_data) == 655813 # Normal test
        assert population_total([reduced_data[0]]) == 55395  # Single county
        assert population_total([]) == 0  # Empty list


    # Part 2
    # test filter_by_state
    def test_filter_by_state(self):
        # Test with CA (California) - should return 2 counties from reduced_data
        ca_counties = filter_by_state(reduced_data, "CA")
        assert len(ca_counties) == 2
        assert ca_counties[0].county == "San Luis Obispo County"
        assert ca_counties[1].county == "Yolo County"

        # Test with AR (Arkansas) - should return 1 county
        ar_counties = filter_by_state(reduced_data, "AR")
        assert len(ar_counties) == 1
        assert ar_counties[0].county == "Crawford County"

        # Test with NY (New York) - should return empty list as no NY counties in reduced_data
        ny_counties = filter_by_state(reduced_data, "NY")
        assert len(ny_counties) == 0

        # Test with empty input list
        empty_result = filter_by_state([], "CA")
        assert len(empty_result) == 0

    # Part 3
    # test population_by_education
    def test_population_by_education(self):
        # Test with Bachelor's Degree or Higher
        bachelors_pop = population_by_education(reduced_data, "Bachelor's Degree or Higher")
        expected_bachelors = sum(county.population['2014 Population'] *
                                 county.education["Bachelor's Degree or Higher"] / 100
                                 for county in reduced_data)
        assert abs(bachelors_pop - expected_bachelors) < 0.001  # Account for floating-point precision

        # Test with High School or Higher
        highschool_pop = population_by_education(reduced_data, "High School or Higher")
        expected_highschool = sum(county.population['2014 Population'] *
                                  county.education["High School or Higher"] / 100
                                  for county in reduced_data)
        assert abs(highschool_pop - expected_highschool) < 0.001

        # Test with invalid key
        invalid_pop = population_by_education(reduced_data, "Invalid Key")
        assert invalid_pop == 0

        # Test with empty list
        empty_pop = population_by_education([], "Bachelor's Degree or Higher")
        assert empty_pop == 0

    # test population_by_ethnicity
    def test_population_by_ethnicity(self):
        # Test with White Alone
        white_pop = population_by_ethnicity(reduced_data, "White Alone")
        expected_white = sum(county.population['2014 Population'] *
                             county.ethnicities["White Alone"] / 100
                             for county in reduced_data)
        assert abs(white_pop - expected_white) < 0.001

        # Test with Hispanic or Latino
        hispanic_pop = population_by_ethnicity(reduced_data, "Hispanic or Latino")
        expected_hispanic = sum(county.population['2014 Population'] *
                                county.ethnicities["Hispanic or Latino"] / 100
                                for county in reduced_data)
        assert abs(hispanic_pop - expected_hispanic) < 0.001

        # Test with invalid key
        invalid_pop = population_by_ethnicity(reduced_data, "Invalid Key")
        assert invalid_pop == 0

        # Test with empty list
        empty_pop = population_by_ethnicity([], "White Alone")
        assert empty_pop == 0

    # test population_below_poverty_level
    def test_population_below_poverty_level(self):
        # Test with full reduced data
        poverty_pop = population_below_poverty_level(reduced_data)
        expected_poverty = sum(county.population['2014 Population'] *
                               county.income["Persons Below Poverty Level"] / 100
                               for county in reduced_data)
        assert abs(poverty_pop - expected_poverty) < 0.001

        # Test with single county
        single_county = [reduced_data[0]]
        single_poverty = population_below_poverty_level(single_county)
        expected_single = (single_county[0].population['2014 Population'] *
                           single_county[0].income["Persons Below Poverty Level"] / 100)
        assert abs(single_poverty - expected_single) < 0.001

        # Test with empty list
        empty_poverty = population_below_poverty_level([])
        assert empty_poverty == 0

    # Part 4
    def test_percent_by_education(self):
        # Test with normal case
        bachelors_percent = percent_by_education(reduced_data, "Bachelor's Degree or Higher")
        expected_bachelors = (population_by_education(reduced_data, "Bachelor's Degree or Higher") /
                              population_total(reduced_data)) * 100 if population_total(reduced_data) != 0 else 0
        assert abs(bachelors_percent - expected_bachelors) < 0.001

        # Test with invalid key
        assert percent_by_education(reduced_data, "Invalid Key") == 0

        # Test with empty list
        assert percent_by_education([], "Bachelor's Degree or Higher") == 0

    def test_percent_by_ethnicity(self):
        # Test with normal case - White Alone
        white_percent = percent_by_ethnicity(reduced_data, "White Alone")
        expected_white = (population_by_ethnicity(reduced_data, "White Alone") /
                          population_total(reduced_data)) * 100 if population_total(reduced_data) != 0 else 0
        assert abs(white_percent - expected_white) < 0.001

        # Test with Hispanic or Latino
        hispanic_percent = percent_by_ethnicity(reduced_data, "Hispanic or Latino")
        expected_hispanic = (population_by_ethnicity(reduced_data, "Hispanic or Latino") /
                             population_total(reduced_data)) * 100 if population_total(reduced_data) != 0 else 0
        assert abs(hispanic_percent - expected_hispanic) < 0.001

        # Test with invalid key
        assert percent_by_ethnicity(reduced_data, "Invalid Key") == 0

        # Test with empty list
        assert percent_by_ethnicity([], "White Alone") == 0

    def test_percent_below_poverty_level(self):
        # Test with normal case
        poverty_percent = percent_below_poverty_level(reduced_data)
        expected_poverty = (population_below_poverty_level(reduced_data) /
                            population_total(reduced_data)) * 100 if population_total(reduced_data) != 0 else 0
        assert abs(poverty_percent - expected_poverty) < 0.001

        # Test with single county
        single_county = [reduced_data[0]]
        single_poverty_percent = percent_below_poverty_level(single_county)
        expected_single = (population_below_poverty_level(single_county) /
                           population_total(single_county)) * 100
        assert abs(single_poverty_percent - expected_single) < 0.001

        # Test with empty list
        assert percent_below_poverty_level([]) == 0

    # Part 5
    # test education_greater_than
    def test_education_greater_than(self):
        # Test for Bachelor's Degree or Higher > 30%
        high_education = education_greater_than(reduced_data, "Bachelor's Degree or Higher", 30)
        assert len(high_education) == 2  # San Luis Obispo and Yolo counties
        assert "San Luis Obispo County" in [county.county for county in high_education]
        assert "Yolo County" in [county.county for county in high_education]

        # Test with threshold that no county meets
        very_high = education_greater_than(reduced_data, "Bachelor's Degree or Higher", 90)
        assert len(very_high) == 0

        # Test with invalid key
        invalid_key = education_greater_than(reduced_data, "Invalid Key", 50)
        assert len(invalid_key) == 0

        # Test with empty list
        empty_list = education_greater_than([], "Bachelor's Degree or Higher", 30)
        assert len(empty_list) == 0

    # test education_less_than
    def test_education_less_than(self):
        # Test for Bachelor's Degree or Higher < 20%
        low_education = education_less_than(reduced_data, "Bachelor's Degree or Higher", 20)
        assert len(low_education) == 3  # Counties with < 20% bachelor's degrees
        for county in low_education:
            assert county.education["Bachelor's Degree or Higher"] < 20

        # Test with threshold that no county meets
        very_low = education_less_than(reduced_data, "Bachelor's Degree or Higher", 0)
        assert len(very_low) == 0

        # Test with invalid key
        invalid_key = education_less_than(reduced_data, "Invalid Key", 50)
        assert len(invalid_key) == 0

        # Test with empty list
        empty_list = education_less_than([], "Bachelor's Degree or Higher", 20)
        assert len(empty_list) == 0
    # test ethnicity_greater_than
    def test_ethnicity_greater_than(self):
        # Test for Hispanic or Latino > 20%
        high_hispanic = ethnicity_greater_than(reduced_data, "Hispanic or Latino", 20)
        assert len(high_hispanic) == 2  # San Luis Obispo and Yolo counties
        for county in high_hispanic:
            assert county.ethnicities["Hispanic or Latino"] > 20

        # Test with threshold that no county meets
        very_high = ethnicity_greater_than(reduced_data, "Hispanic or Latino", 90)
        assert len(very_high) == 0

        # Test with invalid key
        invalid = ethnicity_greater_than(reduced_data, "Invalid Key", 50)
        assert len(invalid) == 0

    # test ethnicity_less_than
    def test_ethnicity_less_than(self):
        # Test for Hispanic or Latino < 10%
        low_hispanic = ethnicity_less_than(reduced_data, "Hispanic or Latino", 10)
        assert len(low_hispanic) > 0
        for county in low_hispanic:
            assert county.ethnicities["Hispanic or Latino"] < 10

    # test below_poverty_level_greater_than
    def test_below_poverty_level_greater_than(self):
        # Test for poverty level > 15%
        high_poverty = below_poverty_level_greater_than(reduced_data, 15)
        assert len(high_poverty) > 0
        for county in high_poverty:
            assert county.income["Persons Below Poverty Level"] > 15

        # Test with empty list
        assert len(below_poverty_level_greater_than([], 15)) == 0

    # test below_poverty_level_less_than
    def test_below_poverty_level_less_than(self):
        # Test for poverty level < 15%
        low_poverty = below_poverty_level_less_than(reduced_data, 15)
        assert len(low_poverty) > 0
        for county in low_poverty:
            assert county.income["Persons Below Poverty Level"] < 15


if __name__ == '__main__':
    unittest.main()
