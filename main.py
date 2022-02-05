# Load functions
from import_data import returnsDataSet
from lib_versions import getLibVersions
from summarize_dataset import summarizeDataset
from show_graphs import showGraphs
from evaluate_algorithms import createValidationDataset, evaluateSVC, algorithmComparison



if __name__ == '__main__':
    getLibVersions()
    _, names, dataset = returnsDataSet()
    summarizeDataset(dataset)
    showGraphs(dataset)
    X_train, X_validation, Y_train, Y_validation = createValidationDataset(dataset)
    algorithmComparison(X_train, Y_train)
    evaluateSVC(X_train, Y_train, X_validation, Y_validation)