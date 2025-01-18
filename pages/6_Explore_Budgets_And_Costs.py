import streamlit as st
import pandas as pd

# ------------------------------------------------------------------------------------
def render_dataframe_with_highlight(df, highlight_col_idx=1, highlight_color='lightgrey'):
    """
    Render a DataFrame in Streamlit as an HTML table with a highlighted column.

    Parameters:
    - df: pandas DataFrame to display
    - highlight_col_idx: Index of the column to highlight (default is 1 for the second column)
    - highlight_color: The color to apply to the highlighted column (default is 'red')
    """
    # Convert all columns to strings
    df = df.astype(str)

    # Construct the HTML table
    html_table = '<table border="1" class="dataframe">\n'
    # Add table headers
    html_table += "<thead><tr>" + "".join(f"<th>{col}</th>" for col in df.columns) + "</tr></thead>\n"
    # Add table rows
    html_table += "<tbody>\n"
    for _, row in df.iterrows():
        html_table += "<tr>"
        for idx, cell in enumerate(row):
            # Apply background color to the specified column
            if idx == highlight_col_idx:
                html_table += f'<td style="background-color: {highlight_color};">{cell}</td>'
            else:
                html_table += f"<td>{cell}</td>"
        html_table += "</tr>\n"
    html_table += "</tbody>\n</table>"
    return html_table 


# ------------------------------------------------------------------------------------
df_Invoices = pd.read_csv(f'./data/Zoo-Invoices.csv')
df_Budgets = pd.read_csv(f'./data/Zoo-Budgets.csv')

# Group by 'Month' and 'Order', then sum the 'Budget'
df_grouped = df_Budgets.groupby(['Month', 'Order Type'], as_index=False).sum()

# Pivot the DataFrame to wide format
df_result = df_grouped.pivot(index='Month', columns='Order Type', values='Budget').reset_index()

# Optionally, clean up column names (remove MultiIndex if present)
df_result.columns.name = None
df_result['Total'] = df_result.iloc[:, 1:].sum(axis=1)
df_result = df_result[['Month','Total','Coffee', 'Tea', 'Meat','Fish','Fruit','Plants']]

# ------------------------------------------------------------------------------------
st.subheader('Monthly Budgets')

df_result = df_result.astype(str)
html_result = render_dataframe_with_highlight(df_result, highlight_col_idx=1, highlight_color='lightgrey')
# Render the styled table in Streamlit
st.markdown(html_result, unsafe_allow_html=True)

