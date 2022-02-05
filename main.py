# Load functions
from import_data import returnsDataSet
from lib_versions import getLibVersions
from summarize_dataset import summarizeDataset
from show_graphs import showGraphs
from evaluate_algorithms import createValidationDataset, evaluateModels



if __name__ == '__main__':
    getLibVersions()
    _, names, dataset = returnsDataSet()
    summarizeDataset(dataset)
    showGraphs(dataset)
    X_train, _, Y_train, _ = createValidationDataset(dataset)
    evaluateModels(X_train, Y_train)