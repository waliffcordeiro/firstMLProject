from pandas import read_csv

def returnsDataSet():
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = read_csv(url, names=names)
    print(dataset)
    return (url, names, dataset)

if __name__ == '__main__':
    returnsDataSet()