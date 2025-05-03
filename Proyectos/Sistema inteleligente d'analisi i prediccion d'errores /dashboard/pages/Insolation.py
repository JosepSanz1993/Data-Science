from dashboard.mean.mean_page import MeanPage
from bd.mongo_db import MongoDB
mongo = MongoDB()
mongo.connect()
data = mongo.find_data("isolation_forest_results")
mongo.close()
InsolationPage = MeanPage()
InsolationPage.make_eyelashes(data)