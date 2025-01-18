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


# ------------------------------------------------------------------------------------
st.subheader('Annual Budgets')

# Group by 'Month' and 'Order', then sum the 'Budget'
df_grouped = df_Budgets.groupby(['Month', 'Order Type'], as_index=False).sum()
# Pivot the DataFrame to wide format
df_result = df_grouped.pivot(index='Month', columns='Order Type', values='Budget').reset_index()
# Optionally, clean up column names (remove MultiIndex if present)
df_result.columns.name = None
df_result['Total'] = df_result.iloc[:, 1:].sum(axis=1)
df_result = df_result[['Month','Total','Coffee', 'Tea', 'Meat','Fish','Fruit','Plants']]
df_result = df_result.applymap(lambda x: f"£{x:,.2f}" if isinstance(x, (int, float)) else x)

html_result = render_dataframe_with_highlight(df_result, highlight_col_idx=1, highlight_color='lightgrey')
# Render the styled table in Streamlit
# Add CSS for scrollable div with specified height
html_table_with_scroll = f"""
<div style="height: 200px; overflow-y: scroll; border: 1px solid #ccc; padding: 10px;">
    {html_result}
</div>
"""
st.markdown(html_table_with_scroll, unsafe_allow_html=True)

# ------------------------------------------------------------------------------------
st.subheader('Annual Costs')

# Group by 'Month' and 'Order', then sum the 'Budget'
df_grouped = df_Invoices.groupby(['Month', 'Order Type'], as_index=False).sum()
# Pivot the DataFrame to wide format
df_result = df_grouped.pivot(index='Month', columns='Order Type', values='Cost').reset_index()
# Optionally, clean up column names (remove MultiIndex if present)
df_result.columns.name = None
df_result['Total'] = df_result.iloc[:, 1:].sum(axis=1)
df_result = df_result[['Month','Total','Coffee', 'Tea', 'Meat','Fish','Fruit','Plants']]

df_result = df_result.applymap(lambda x: f"£{x:,.2f}" if isinstance(x, (int, float)) else x)

html_result = render_dataframe_with_highlight(df_result, highlight_col_idx=1, highlight_color='lightgrey')
# Render the styled table in Streamlit
# Add CSS for scrollable div with specified height
html_table_with_scroll = f"""
<div style="height: 200px; overflow-y: scroll; border: 1px solid #ccc; padding: 10px;">
    {html_result}
</div>
"""
st.markdown(html_table_with_scroll, unsafe_allow_html=True)

# ------------------------------------------------------------------------------------
st.subheader('Monthly Budget Allocation by Enclosure')

df_Budgets['Text'] = df_Budgets.apply(lambda row: f"{row['Enclosure']} (£{row['Budget']:.0f})", axis=1)

df_Summary = df_Budgets[df_Budgets['Month'] == '2024-01'].groupby(['Order Type']).agg(
    Total=('Budget','sum'),
    Enclosures=('Text', lambda x: ', '.join(x.astype(str))))
df_Summary['Total'] = df_Summary['Total'].apply(lambda x: f"£{x:,.0f}")
df_Summary = df_Summary.loc[['Coffee', 'Tea', 'Meat', 'Fish', 'Fruit', 'Plants']]

st.write(df_Summary)

