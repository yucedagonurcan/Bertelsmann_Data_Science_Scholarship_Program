from CountryModel import CountryModel
import xlrd


def modified_data():
    """
        Out Of School Rates,
        Child Marriages Rates,
        Poverty headcount ratio at $1.90 a day,
        Fertility rate, total (births per woman) and
        GDP for the countries that has the data.
    """
    ## Out of school rates

    workbook = xlrd.open_workbook('Data/Out-of-School-Rate-Final-for-website.xlsx', on_demand=True)
    worksheet = workbook.sheet_by_name(' Primary OOS')

    countries_array = []
    i = 1
    current_row = worksheet.row(i)

    while current_row[0].value != '':
        newCountry = CountryModel(country_code=current_row[0].value,
                                  country_name=current_row[1].value,
                                  out_of_school_total=current_row[2].value,
                                  out_of_school_male=current_row[4].value,
                                  out_of_school_female=current_row[6].value)
        countries_array.append(newCountry)
        i += 1
        current_row = worksheet.row(i)

    ## Out of school rate

    ## Child marriage

    workbook = xlrd.open_workbook('Data/Child-marriage-database_Mar-2018.xlsx', on_demand=True)
    worksheet = workbook.sheet_by_name('Child marriage')

    i = 1
    current_row = worksheet.row(i)

    while current_row[0].value != '':

        for country in countries_array:
            if country.country_name == current_row[0].value:
                if current_row[1].value == '':
                    current_row[1].value = -1
                country.child_marriages_rate_by15 = current_row[1].value
                if current_row[3].value == '':
                    current_row[3].value = -1
                country.child_marriages_rate_by18 = current_row[3].value

        i += 1
        current_row = worksheet.row(i)
    ## Child marriage


    ## Poverty headcount ratio at $1.90 a day (2011 PPP) (% of population)

    workbook = xlrd.open_workbook('Data/API_SI.POV.DDAY_DS2_en_excel_v2_9985604.xls', on_demand=True)
    worksheet = workbook.sheet_by_name('Data')

    i = 1
    current_row = worksheet.row(i)
    while current_row is not None and current_row[0].value != '':
        for country in countries_array:
            if country.country_name == current_row[0].value and country.country_code == current_row[1].value:
                country_poverty_headcunt_ratio_array = []
                for j in range(4, 62):  # current_row[4].value[61]
                    country_poverty_headcunt_ratio_array.append(current_row[j].value)
                country_poverty_headcunt_ratio_array[country_poverty_headcunt_ratio_array == ''] = -1
                country.poverty_headcount_ratio = country_poverty_headcunt_ratio_array
        i += 1
        try:
            current_row = worksheet.row(i)
        except:
            current_row[0].value = ''
            current_row = None

    ## Poverty headcount ratio at $1.90 a day (2011 PPP) (% of population)


    ## Fertility rate, total (births per woman)

    workbook = xlrd.open_workbook('Data/API_SP.DYN.TFRT.IN_DS2_en_excel_v2_9984982.xls', on_demand=True)
    worksheet = workbook.sheet_by_name('Data')

    i = 1
    current_row = worksheet.row(i)
    while current_row is not None and current_row[0].value != '':
        for country in countries_array:
            if country.country_name == current_row[0].value and country.country_code == current_row[1].value:
                country_fertility_rate_total_array = []
                for j in range(4, 62):  # current_row[4].value[61]
                    country_fertility_rate_total_array.append(current_row[j].value)
                country_fertility_rate_total_array[country_fertility_rate_total_array == ''] = -1
                country.fertility_rate_per_woman = country_fertility_rate_total_array
        i += 1
        try:
            current_row = worksheet.row(i)
        except:
            current_row[0].value = ''
            current_row = None

    ## Fertility rate, total (births per woman)



    ## Mortality rate, under-5 (per 1,000 live births)

    workbook = xlrd.open_workbook('Data/API_SH.DYN.MORT_DS2_en_excel_v2_9989226.xls', on_demand=True)
    worksheet = workbook.sheet_by_name('Data')

    i = 1
    current_row = worksheet.row(i)
    while current_row is not None and current_row[0].value != '':
        for country in countries_array:
            if country.country_name == current_row[0].value and country.country_code == current_row[1].value:
                mortality_rate_under_5_array = []
                for j in range(4, 62):  # current_row[4].value[61]
                    mortality_rate_under_5_array.append(current_row[j].value)
                country.mortality_rate_under_5 = mortality_rate_under_5_array
        i += 1
        try:
            current_row = worksheet.row(i)
        except:
            current_row[0].value = ''
            current_row = None

    ## Mortality rate, under-5 (per 1,000 live births)

    ## GDP
    workbook = xlrd.open_workbook('Data/GDP.xls', on_demand=True)
    worksheet = workbook.sheet_by_name('GDP')

    i = 1
    current_row = worksheet.row(i)
    while current_row is not None and current_row[0].value != '':
        for country in countries_array:
            if country.country_name == current_row[3].value and country.country_code == current_row[0].value:
                country.gdp = current_row[4].value
        i += 1
        try:
            current_row = worksheet.row(i)
        except:
            current_row[0].value = ''
            current_row = None
    ## GDP
    return countries_array
