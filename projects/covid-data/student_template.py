# data is a single list
class CovidRecord:
    """
    A simple class to hold record data from NYT database
    """

    def __init__(self, _date='', _county='', _state='', _fips=0, _cases=0, _death=0):
        """
        Default constructor for transforming each line of the file into data point

        :param _date: Date covid case was recorded
        :param _county: County in which data was recorded
        :param _state: State in which data was recorded
        :param _fips: Federal Information Processing Standards code
        :param _cases: Number of total cases recorded
        :param _death: Number of total deaths recorded
        """
        self.date = _date
        self.county = _county
        self.state = _state

        if _fips == '':
            self.fips = 0
        else:
            self.fips = int(_fips)
        self.cases = int(_cases)

        if _death == '':
            self.death = 0
        else:
            self.death = int(_death)


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of points
    :param file_path: Path to data file
    :return: List of CovidRecord points
    """
    # data point list
    covid_data = list()

    # open the NYT file path
    fin = open(file_path)

    # get rid of the headers
    fin.readline()

    done = False

    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        elements = line.strip().split(",")

        new_point = CovidRecord((elements[0]), (elements[1]), (elements[2]),
                                (elements[3]), (elements[4]), (elements[5]))

        # to reduce file sizes, only grab Virginia points
        if new_point.state == 'Virginia':
            covid_data.append(new_point)

    return covid_data


if __name__ == "__main__":
    # load covid data as list of CovidRecord objects
    data = parse_nyt_data('us-counties.csv')

    # each element in list data is a CovidRecord object. Each of which contains
    # date, county, state, fips, cases, and deaths

    # for example, we can print out the data for the first point in the US counties file
    point = data[0]

    # print("Date: ", point.date, " County: ", point.county, " State: ", point.state,
          # " FIPS: ", point.fips, " Cases: ", point.cases, " Deaths: ", point.death)

    # Create new lists for hburg and rock data
    rockingham = []
    harrisonburg = []

    for value in data:
        if value.county == 'Rockingham':
            rockingham.append(value)
        elif value.county == 'Harrisonburg city':
            harrisonburg.append(value)
        else:
            continue

    # write code to address the following question:
    # When was the first positive COVID case in Rockingham County?
    for i in rockingham:
        if i.cases >= 1:   # greater than or equal to one to indicate the first case
            print("The first COVID case recorded in Rockingham was on", i.date)
        break

    # When was the first in Harrisonburg?
    for j in harrisonburg:
        if j.cases >= 1:
            print("The first COVID case recorded in Harrisonburg was on", j.date)
        break

    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    max_cases = 10000   # set this to be my threshold value for finding the max value
    max_date = None
    for k in harrisonburg:
        if k.cases > max_cases:
            max_cases = k.cases
            max_date = k.date
    print("The greatest number of cases in Harrisonburg was on", max_date, "with", max_cases, "cases")

    # When was the greatest day in Rockingham County?
    for l in rockingham:
        if l.cases > max_cases:
            max_cases = l.cases
            max_date = l.date
    print("The greatest number of cases in Rockingham was on", max_date, "with", max_cases, "cases")

    # What was the worst seven-day period in either the city and county for new COVID cases?

    # combine data to find the worst seven-day period from either the city or county
    local = rockingham + harrisonburg

    max_sum = 10000      # set a threshold value for the max, same as max_cases
    current_sum = 0
    max_dates = None
    for m in local:
        for n in range(0, len(local)-6, 7):
            current_sum = current_sum + m.cases
            if current_sum > max_sum:
                max_sum = current_sum
                max_dates = local[n:n + 7]
    for o in max_dates:
        print("The seven day period with the most cases is:", o.date, o.cases)

    # The End.