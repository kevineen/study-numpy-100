import streamlit as st

import numpy as np
import pandas as pd

left_column, right_column = st.beta_columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

st.write("Good morning")

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")