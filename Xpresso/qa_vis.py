from xpresso.ai.core.data.xdm.structured_dataset import StructuredDataset
from xpresso.ai.core.data.exploration.dataset_explorer import Explorer
from xpresso.ai.core.data.visualization.visualization import Visualization


# create a dataset
dataset = StructuredDataset()

# import data into the dataset
config = {
    "type": "FS",
    "data_source": "Local",
    "path": "/home/abzooba/PycharmProjects/xpresso.ai/datasets/Womens Clothing E-Commerce Reviews.csv"
}
dataset.import_dataset(user_config=config)

# create a Data Explorer object for the dataset
explorer = Explorer(dataset)

# understand the dataset
explorer.understand(verbose=True)

#explorer.explore_univariate(verbose=True, to_excel=False, validity_threshold=95)
explorer.explore_multivariate(verbose=True, to_excel=False)

visualize = Visualization.get_visualizer(dataset, backend = "seaborn")

#visualize = Visualizer.get_visualizer(dataset, backend = "seaborn")

#visualize.render_univariate(report=True)
visualize.render_multivariate(report=True)