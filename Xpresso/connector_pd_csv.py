from xpresso.ai.core.data.xdm.structured_dataset import StructuredDataset
from xpresso.ai.core.data.exploration.dataset_explorer import Explorer
import pandas as pd

dataset1=pd.read_csv('/home/abzooba/PycharmProjects/xpresso.ai/datasets/duplicate_data.csv')

dataset_object = StructuredDataset()
dataset_object.data = dataset1

print(dataset_object.type)
explorer=Explorer(dataset_object)
explorer.understand()
explorer.explore_univariate(verbose=True)
