class CountryModel:
    """
        Model class from countries that has the features:
            Country Code,
            Country Name,
            Out of School Rates,
            Child Marriages,
            Poverty Headcount,
            Fertility Rate,
            Mortality Rate
    """
    number_of_country = 0

    def __init__(self, country_code, country_name, out_of_school_total, out_of_school_male, out_of_school_female,
                 child_marriages_by15=0, child_marriages_by18=0, poverty_headcount_ratio=[],
                 fertility_rate_per_woman=[], mortality_rate_under_5=[], gdp= -1):
        self.country_code = country_code
        self.country_name = country_name
        self.out_of_school_rate_total= out_of_school_male
        self.out_of_school_rate_male= out_of_school_male
        self.out_of_school_rate_female= out_of_school_female
        self.child_marriages_rate_by15 = child_marriages_by15
        self.child_marriages_rate_by18 = child_marriages_by18
        self.poverty_headcount_ratio = poverty_headcount_ratio
        self.fertility_rate_per_woman = fertility_rate_per_woman
        self.number_of_country += 1
        self.mortality_rate_under_5 = mortality_rate_under_5
        self.gdp = gdp
