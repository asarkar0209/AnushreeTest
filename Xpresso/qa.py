from xpresso.ai.core.data.xdm.structured_dataset import StructuredDataset
from xpresso.ai.core.data.exploration.dataset_explorer import Explorer
from xpresso.ai.core.data.transformation.dataset_cleaning import DataCleaning

# create a dataset
dataset = StructuredDataset()

# import data into the dataset
user_config1 = {
        "type": "FS",
        "data_source":"Local",
        "path": "/home/abzooba/PycharmProjects/xpresso.ai/datasets/titanic.csv"

    }
dataset.import_dataset(user_config1,local_storage_required=True)


explorer=Explorer(dataset)
explorer.understand(verbose=True)
explorer.explore_univariate()
explorer.explore_multivariate(verbose=True)

print('Cleaning Data-set')
cleaner = DataCleaning(dataset)
cleaner.transform(deduplicate=True,columns=['Sex'],keep=True)
(dataset.show())

dataset.diff(new=dataset)




