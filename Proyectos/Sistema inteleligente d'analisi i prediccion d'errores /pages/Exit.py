import streamlit as st
from datetime import datetime
from bd.mongo_db import MongoDB
from scripts.var_constant import *

# Page configuration
st.set_page_config(page_title="End of Project", page_icon="✅", layout="centered")

# Title and closing message
st.title("🎉 End of the Project")
st.subheader("Thank you for using this application!")

# Main message
st.markdown("""
You have reached the end of the project.  
We hope it was a useful and enriching experience.

---

🔚 **See you soon!**
""")

# Optional: celebratory image or emoji
st.image("https://media.giphy.com/media/3o6ZsZKn5KSQZ1l04s/giphy.gif", use_column_width=True)

# Show current date and time as closure info
st.caption(f"📅 Closed on {datetime.now().strftime('%B %d, %Y at %H:%M:%S')}")

#Delete collections
mongo = MongoDB(MONGO_DB_URI, MONGO_DB_NAME)
mongo.connect()
mongo.delete_collection("autoencoder_results")
mongo.delete_collection("isolation_forest_results")
mongo.delete_collection("random_forest_results")
mongo.delete_collection("mlp_results")
mongo.close()
