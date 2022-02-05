from pandas.plotting import scatter_matrix
from matplotlib import pyplot

from import_data import returnsDataSet

def showGraphs(dataset):
    # box and whisker plots
    dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
    pyplot.show()
    # histograms
    dataset.hist()
    pyplot.show()
    # scatter plot matrix
    scatter_matrix(dataset)
    pyplot.show()

if __name__ == '__main__':
    _, _, dataset = returnsDataSet()
    showGraphs(dataset)