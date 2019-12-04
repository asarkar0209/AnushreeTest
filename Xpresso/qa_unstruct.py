from xpresso.ai.core.data.xdm.unstructured_dataset import UnstructuredDataset
from xpresso.ai.core.data.exploration.dataset_explorer import Explorer
dataset_text=UnstructuredDataset()

user_config3 = {
        "type": "FS",
        "path": "/test_connector/small_size_data/city.txt"
}


dataset_text.import_dataset(user_config3)

explorer3=Explorer(dataset_text)

explorer3.understand(verbose=True)
# explorer3.explore_unstructured()