from utils.dash.mean_page import MeanPage
from scripts.var_constant import *
from bd.mongo_db import MongoDB
mongo = MongoDB(MONGO_DB_URI, MONGO_DB_NAME)
mongo.connect()
data = mongo.find_data("mlp_results",{})
copy = data.copy()
mongo.delete_all_data("mlp_results")
mongo.close()
InsolationPage = MeanPage()
InsolationPage.make_eyelashes(copy)