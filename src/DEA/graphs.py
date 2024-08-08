"""This package hold function to make graphs"""

from plotly.graph_objs._figure import Figure
import numpy as np
import pandas as pd
from IPython.display import display
from IPython.core.display import HTML
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px


# Function to create scrollable table within a small window
def create_scrollable_table(df: pd.DataFrame, table_id: str, title: str) -> str:
    """This function return a html in document in string format that render a
    pandas datatframe in an scrollable div

    Parameters
    ----------
    df : pd.DataFrame
        The dataframe to be rendered
    table_id : str
        The string use as the html id
    title : str
        The title to display for the dataframe

    Returns
    -------
    str
        A string version of the html document
    """
    html = f"<h3>{title}</h3>"
    html += f'<div id="{table_id}" style="height:600px; overflow:auto;">'
    html += df.to_html()
    html += "</div>"
    return html


def render_scrooll(df: pd.Series, title: str = ""):
    """This function render a pandas inside a scrollable box. It use a scrollable html div

    Parameters
    ----------
    df : pd.Series
        The Serie to be rendered
    title : str, optional
        The Title to put at the top of the box, by default ""
    """
    html_null_values = create_scrollable_table(df.to_frame(), "Scrollable", title)

    display(HTML(html_null_values))


def graph_price_bar(df: pd.DataFrame, feature_name: str, title: str) -> Figure:
    """This function return a plotly express figute for with a bar chart of the price and another feature

    Parameters
    ----------
    df : pd.DataFrame
        The dataframe that has the data
    feature_name : str
        The name of the column that will be use as the x-axis
    title : str
        The title of the plot

    Return
    ------
    fig: Figure
        The plotly express figure
    """
    colors = px.colors.qualitative.Plotly
    feature_to_prices = df.groupby(feature_name)["SalePrice"].mean()
    fig = px.bar(
        x=feature_to_prices.index,
        y=feature_to_prices.values,
        title=title,
        # color_discrete_sequence=["purple", "green"],
        text=feature_to_prices.values,
        template="plotly_dark",
    )

    fig.update_traces(
        marker_color=colors, texttemplate="$%{text:,.0f}", textposition="outside"
    )
    fig.update_yaxes(title="Sale Price", tickprefix="$", tickformat=",")
    fig.update_xaxes(title=title)
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode="hide")
    return fig
