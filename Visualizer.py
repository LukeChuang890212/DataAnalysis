import altair as alt
import pandas as pd
import numpy as np

#x,category,y
def plot_line_graph(source):
    # Create a selection that chooses the nearest point & selects based on x-value
    nearest = alt.selection(type='single', nearest=True, on='mouseover',
                            fields=[source.columns[0]], empty='none')

    # The basic line
    line = alt.Chart(source).mark_line(interpolate='basis').encode(
        x=source.columns[0]+':Q',
        y=source.columns[2]+':Q',
        color=source.columns[1]+':N'
    )

    # Transparent selectors across the chart. This is what tells us
    # the x-value of the cursor
    selectors = alt.Chart(source).mark_point().encode(
        x=source.columns[0]+':Q',
        opacity=alt.value(0),
    ).add_selection(
        nearest
    )

    # Draw points on the line, and highlight based on selection
    points = line.mark_point().encode(
        opacity=alt.condition(nearest, alt.value(1), alt.value(0))
    )

    # Draw text labels near the points, and highlight based on selection
    text = line.mark_text(align='left', dx=5, dy=-5).encode(
        text=alt.condition(nearest, source.columns[2]+':Q', alt.value(' '))
    )

    # Draw a rule at the location of the selection
    rules = alt.Chart(source).mark_rule(color='gray').encode(
        x=source.columns[0]+':Q',
    ).transform_filter(
        nearest
    )

    # Put the five layers into a chart and bind the data
    alt.layer(
        line, selectors, points, rules, text
    ).properties(
        width=600, height=300
    ).save("圖表\chart.html")