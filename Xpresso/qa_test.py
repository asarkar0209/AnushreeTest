from xpresso.ai.core.data.xdm.structured_dataset import StructuredDataset
from xpresso.ai.core.data.exploration.dataset_explorer import Explorer
import pandas as pd





# create a dataset
dataset = StructuredDataset()


# import data into the dataset

user_config1 = {
        "type": "FS",
        "data_source":"Local",
        "path": "/home/abzooba/PycharmProjects/xpresso.ai/datasets/haberman.csv"

    }
dataset.import_dataset(user_config1,local_storage_required=True)
print('Unique Values of Age Column')
unique=dataset.unique(attr_name='Age')
print(unique)
# create a Data Explorer object for the dataset
explorer1 = Explorer(dataset)


# # understand the dataset
explorer1.understand(verbose=True)

# # explore univariate & multivariate
explorer1.explore_univariate()


explorer1.explore_multivariate(to_excel=True)






# from xpresso.ai.core.data.visualization.visualizer import Visualizer
#
# visualize1=Visualizer.get_visualizer(dataset, backend = "seaborn")
# visualize2=Visualizer.get_visualizer(dataset_numeric, backend = "plotly")
#
#
# # In[4]:
#
#
# visualize1.render_univariate(attr_name="Clothing ID")
#
#
# # In[5]:
#
#
# visualize1.render_univariate(attr_name="Age")
#
#
# # In[6]:
#
#
# visualize1.render_univariate(attr_name="Rating")
#
#
# # In[7]:
#
#
# visualize1.render_multivariate()
#
#
# # In[8]:
#
#
# visualize2.render_multivariate()
#
#
# # In[9]:
#
#
# visualize2.render_univariate(attr_name='Age')
#
#
# # In[10]:
#
#
# # dataset_numeric.head()
# visualize2.scatter(attribute_x="Age",attribute_y="Op_Year")
#
#
# # In[11]:
#
#
# visualize2.render_all()
#
#
# # In[1]:
#
#
# from xpresso.ai.core.data.connections.connector import DataConnector
# from xpresso.ai.core.data.exploration.dataset_explorer import Explorer
# from xpresso.ai.core.data.xdm.unstructured_dataset import UnstructuredDataset
#
# # set parameters for importing a CSV file
#
# dataset2=UnstructuredDataset()
#
# loc_con = {
#         "type": "FS",
#         "path": "/test_connector/small_size_data/city.txt"
#     }
#
# data = DataConnector().getconnector(loc_con.get("type"),loc_con.get("data_source")).import_files(loc_con)
#
# print(data)
# # dataset2.import_dataset()
# # explorer3=Explorer(dataset2)
# # explorer3.explore_unstructured()
#
#
# # In[1]:
#
#
# from xpresso.ai.core.data.xdm.unstructured_dataset import UnstructuredDataset
# dataset_text=UnstructuredDataset()
#
# user_config3 = {
#         "type": "FS",
#         "path": "/test_connector/small_size_data/city.txt"
# }
#
#
# dataset_text.import_dataset(user_config3)
# explorer3=Explorer(dataset_text)
# explorer3.explore_unstructured()
#
#
# # In[2]:
#
#
# from xpresso.ai.core.data.xdm.unstructured_dataset import UnstructuredDataset
# from xpresso.ai.core.data.exploration.dataset_explorer import Explorer
# from xpresso.ai.core.data.connections.internal_connectors.local_file_system.connector import LocalFSConnector
# local=LocalFSConnector()
# config = {
#                 "path": "/home/abzooba/JupyterProjects/xpresso.ai/datasets/Womens Clothing E-Commerce Reviews.csv"
#             }
# review_dataset=local.import_dataframe(config)
# explorer4=Explorer(review_dataset)
#
# explorer4.explore_unstructured()
#
#
# # In[ ]:
#
#
#
#
#
# # In[ ]:
#
#
#
#
