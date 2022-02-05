from import_data import returnsDataSet

def summarizeDataset(dataset):
    # shape
    print(dataset.shape)
    # head
    print(dataset.head(20))
    # descriptions
    print(dataset.describe())
    # class distribution    
    print(dataset.groupby('class').size())

if __name__ == '__main__':
    _, _, dataset = returnsDataSet()
    summarizeDataset(dataset)