import pandas as pd

dataSet = {
    'car' : ["BMW", "Volvo", "Ford"],
    'passings' : [3,7,5]
}

pas = pd.DataFrame(dataSet)
print(pas)