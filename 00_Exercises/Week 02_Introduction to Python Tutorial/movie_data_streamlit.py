# Run this file on a terminal with `streamlit run movie_data_streamlit.py`

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.write("""
# Movie Data Exploration in Streamlit

As you can see, Streamlit allows you to take python code and turn it into a simple interactive web page pretty easily.

### Exercise 1. Copy over Exercise 4 from the Jupyter Notebook.

In the previous set of exercises, you explored diary.csv with pandas and matplotlib. To start us off here, I just want you to copy over your work from exercise 4 of that set where you plotted frequency per year. 

Below, copy over all of the operations that led to that plot (don't forget to read in `diary.csv` first!). To display the plot in streamlit, you'll need to call the `st.pyplot` method ([documentation here](https://docs.streamlit.io/develop/api-reference/charts/st.pyplot)) on the figure associated with your plot.

For example, let's say you called the [plot method](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.html) available to pandas series objects. If you saved that to a variable named `plot`, you'd have to access the figure associated with that with `plot.figure` and then wrap an `st.pyplot` call around it, making the full line `st.pyplot(plot.figure)`
""")

# YOUR WORK HERE (you should only need like 2 lines unless you want it to look fancy)

st.write("""
### Exercise 2. Let's make that plot not suck.
You'll notice that the plot you made in exercise 1, with streamlit's `pyplot` method, is just a static image. That's not how we tend to like to interact with data on the web.

Instead of using that matplotlib line chart library, let's use a function built into Streamlit for this kind of thing. Let's use the `st.bar_chart` method to display our data as a bar chart. Just take the series you were plotting in the previous example and pass it to the `st.bar_chart` function (it's pretty good about making something out of whatever data you give it! You can also [view its documentation here](https://docs.streamlit.io/develop/api-reference/charts/st.bar_chart))
""")

# YOUR WORK HERE

st.write("""
### Exercise 3. Make that plot interactive.

The main reason we use a tool like streamlit is it can be used to create interactive tables and plots. So, let's see about making that plot from exercise 1 a little interactive. Below is a [slider](https://docs.streamlit.io/develop/api-reference/widgets/st.slider), particularly it is a range slider that allows the user to input a range of floating point values from 0.5 to 5.0 at a step of 0.5:
""")

slider_value = st.slider("Rating range", min_value=0.5, max_value=5.0, step=0.5, value=(0.5, 5.0))

st.write("""
	You'll notice that the slider seems to have saved a return value in a variable named `slider_value`. You can use that variable like you would any other number!

	Below, repeat the same plot as in exercise 2 with one additional restriction: **only include film logs with ratings matching the slider range (inclusive of bounds)**!
""")

# YOUR WORK HERE
