from ModifyData import modified_data
import matplotlib.pyplot as plt
import numpy as np


def visualize(country_names):
    """
    Visualizing the data with the help of the ModifyData file.
    Also it can get multiple country names, for much better comparison.
    """
    countries_array = modified_data()
    current_countries = []
    if type(country_names) != list:
        country_names = [country_names]
    for country in countries_array:
        for country_name in country_names:
            if country_name == country.country_name:
                current_countries.append(country)
                break
    bar_out_of_school(current_countries)
    plot_by_time(current_countries, "fertility")
    plot_by_time(current_countries, "mortality")
    plot_by_time(current_countries, "poverty")
    bar_gdp(current_countries)
    bar_child_marriages(current_countries)


def plot_by_time(current_countries, feature_name):
    """
    Plotting the features that is represented as time by time.
    :param current_countries:
    :param feature_name:
    """
    if feature_name == "poverty":

        title_string = "Poverty headcount ratio at $1.90 for Countries :"
        plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow', 'magenta'])
        for current_country in current_countries:
            y = get_time_values_poverty(current_country)
            x = range(1960, 1960 + len(current_country.poverty_headcount_ratio))
            title_string += ": " + current_country.country_name
            plt.plot(x, y)
    elif feature_name == "mortality":

        title_string = "Mortality rate, under-5 (per 1000) for Countries :"
        plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow', 'magenta'])
        for current_country in current_countries:
            y = get_time_values_mortality(current_country)
            x = range(1960, 1960 + len(current_country.mortality_rate_under_5))
            title_string += ": " + current_country.country_name
            plt.plot(x, y)
    elif feature_name == "fertility":

        title_string = "Fertility rate, total (births per woman) for Countries :"
        plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow', 'magenta'])
        for current_country in current_countries:
            y = get_time_values_fertility(current_country)
            x = range(1960, 1960 + len(current_country.fertility_rate_per_woman))
            title_string += ": " + current_country.country_name
            plt.plot(x, y)

    plt.legend([i.country_name for i in current_countries])
    plt.xlabel('Years')
    plt.ylabel(feature_name)
    plt.title(title_string)
    plt.show()


def get_time_values_poverty(current_country):
    """
    Gets the values of poverty by time
    :param current_country:
    :return:
    """
    feature = np.array(current_country.poverty_headcount_ratio)
    feature[feature == ''] = '-1'
    y = feature.astype(float)
    return y


def get_time_values_fertility(current_country):
    """
       Gets the values of fertility by time
       :param current_country:
       :return:
       """
    feature = np.array(current_country.fertility_rate_per_woman)
    feature[feature == ''] = '-1'
    y = feature.astype(float)
    return y


def get_time_values_mortality(current_country):
    """
       Gets the values of mortality by time
       :param current_country:
       :return:
       """
    feature = np.array(current_country.mortality_rate_under_5)
    feature[feature == ''] = '-1'
    y = feature.astype(float)
    return y


def get_key_marriage(custom):
    return custom.child_marriages_rate_by15


def get_key_out_of_school(custom):
    return custom.out_of_school_rate_total


def get_key__gdp(custom):
    return custom.gdp


def bar_out_of_school(current_countries):
    """
    Makes Bar Chart for Out of School feature.
    :param current_countries:
    :return:
    """
    title_string = "Out of School Rate for Countries :"
    plt.legend([i.country_name for i in current_countries])
    current_countries = list(reversed(sorted(current_countries, key=get_key_out_of_school)))
    for current_country in current_countries:
        y = [current_country.out_of_school_rate_total, current_country.out_of_school_rate_female,
             current_country.out_of_school_rate_male]
        x = ["Total", "Women", "Men"]
        title_string += ": " + current_country.country_name
        plt.bar(x, y)
    plt.xlabel('Rate Types')
    plt.ylabel("Rate")
    plt.title(title_string)
    plt.legend([i.country_name for i in current_countries])
    plt.show()


def bar_gdp(current_countries):
    """
    Makes Bar Chart for GDP feature.
    :param current_countries:
    :return:
    """
    title_string = "Gross Domestic Products for Countries :"
    plt.legend([i.country_name for i in current_countries])
    current_countries = list(reversed(sorted(current_countries, key=get_key__gdp)))
    for current_country in current_countries:
        y = [current_country.gdp]
        x = [current_country.country_name]
        title_string += ": " + current_country.country_name
        plt.bar(x, y)
    plt.xlabel('Value (Million $)')
    plt.ylabel("GDP")
    plt.title(title_string)
    plt.legend([i.country_name for i in current_countries])
    plt.show()


def bar_child_marriages(current_countries):
    """
    Makes Bar Chart for Child Marriages feature.
    :param current_countries:
    :return:
    """
    title_string = "Child Marriages Rate for Countries :"
    plt.legend([i.country_name for i in current_countries])
    current_countries = list(reversed(sorted(current_countries, key=get_key_marriage)))
    for current_country in current_countries:
        y = [current_country.child_marriages_rate_by15, current_country.child_marriages_rate_by18]
        x = ["Child Marriages by 15", "Child Marriages by 18"]
        title_string += ": " + current_country.country_name
        plt.bar(x, y)
    plt.xlabel('Rate Types')
    plt.ylabel("Rate Value")
    plt.title(title_string)
    plt.legend([i.country_name for i in current_countries])
    plt.show()


visualize(["Honduras", "Ghana", "Uganda"])
