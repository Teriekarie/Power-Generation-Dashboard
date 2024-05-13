import streamlit as st
import pandas as pd
import altair as alt

# Setting a theme for the dashboard
st.set_page_config(page_title="Power Generation Dashboard",
                   page_icon="⚡",
                   layout="wide",
                   initial_sidebar_state="expanded",
                   menu_items={
                       'Get Help': 'https://www.example.com',
                       'Report a bug': "https://www.example.com",
                       'About': "# This is a header. This is an *extremely* cool dashboard!"
                   })

# Adding a custom theme with CSS for styling
st.markdown("""
<style>
    /* Main font for the entire dashboard */
    html, body, [class*="css"] {
        font-family: "Gill Sans", sans-serif;
    }
    /* Main dashboard background color */
    body {
        background-color: #f0f2f5;
    }
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #fafafa;
        color: #4f8af4;
    }
    /* Title color */
    h1 {
        color: #ff6347;
    }
    /* Card styling */
    .metric-card {
        padding: 10px;
        border-radius: 10px;
        background-color: #4f8af4;
        color: white;
        font-size: 20px;
        text-align: center;
        margin: 10px;
        flex-grow: 1;
    }
    /* Container for metric cards */
    .metric-container {
        display: flex;
        justify-content: space-around;
    }
    /* Divider style */
    .divider {
        border-top: 2px solid #4f8af4;
        margin: 40px 0;
    }
</style>
""", unsafe_allow_html=True)

# Title of the dashboard
st.title('⚡ Power Generation Analysis')

# Load the dataset
@st.cache_data  # Use the cache decorator to only load the data once
def load_data():
    data = pd.read_csv("file8.csv")
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data['Year'] = data['Date'].dt.year
    data['Month'] = data['Date'].dt.strftime('%Y-%m')
    data['Day'] = data['Date'].dt.day
    data['Hour'] = data['Date'].dt.hour + 1  # Adjust hour for display
    return data

df = load_data()

# Sidebar: adding filters for Genco Name and Date Range
st.sidebar.header('Search Filters')

min_date, max_date = df['Date'].min(), df['Date'].max()

start_date = st.sidebar.date_input("Start Date", min_value=min_date, max_value=max_date, value=min_date)
end_date = st.sidebar.date_input("End Date", min_value=min_date, max_value=max_date, value=max_date)

start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

filtered_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]


if 'Genco Name' in df.columns:
    genco_options = ['All'] + sorted(list(df['Genco Name'].unique()))
    selected_gencos = st.sidebar.multiselect('Select Genco', options=genco_options, default='All')
    if 'All' in selected_gencos:
        selected_gencos = genco_options[1:]  # Include all Genco options
    filtered_data = filtered_data[filtered_data['Genco Name'].isin(selected_gencos)]

# Metric cards display with icons
# # Metric cards display
total_gencos = filtered_data['Genco Name'].nunique()  # Count unique Gencos
average_power_generated = round(filtered_data['TotalGeneration'].mean(), 2)  # Calculate average TotalGeneration
average_restoration_time = round(filtered_data['Restoration_time'].mean())  # Calculate average Restoration Time
average_operational_hours = round(filtered_data['Operational Hours'].mean())  # Calculate average Operational Hours
average_downtime = round(filtered_data['Downtime Count'].sum())  # Calculate average Downtime
icons = {
    "gencos": "🏭",
    "power": "⚡",
    "time": "⏳",
    "hours": "⏰",
    "downtime": "🔧"
}

st.markdown(f"""
<div class='metric-container'>
    <div class='metric-card'>{icons['gencos']} Total Gencos: {total_gencos}</div>
    <div class='metric-card'>{icons['power']} Average Power Generated: {average_power_generated:.2f} MW</div>
    <div class='metric-card'>{icons['time']} Average Restoration Time: {average_restoration_time} hours</div>
    <div class='metric-card'>{icons['hours']} Average Operational Hours: {average_operational_hours} hours</div>
    <div class='metric-card'>{icons['downtime']} Total Downtime Count: {average_downtime} times</div>
</div>
<div class='divider'></div>
""", unsafe_allow_html=True)

# Continue with your chart definitions and other dashboard components...


# import streamlit as st
# import pandas as pd
# import altair as alt

# # Setting a theme for the dashboard
# st.set_page_config(page_title="Power Generation Dashboard",
#                    page_icon=":zap:",
#                    layout="wide",
#                    initial_sidebar_state="expanded",
#                    menu_items={
#                        'Get Help': 'https://www.example.com',
#                        'Report a bug': "https://www.example.com",
#                        'About': "# This is a header. This is an *extremely* cool dashboard!"
#                    })

# # Adding a custom theme with CSS for styling
# st.markdown("""
# <style>
#     /* Main font for the entire dashboard */
#     html, body, [class*="css"] {
#         font-family: "Gill Sans", sans-serif;
#     }
#     /* Main dashboard background color */
#     body {
#         background-color: #f0f2f5;
#     }
#     /* Sidebar styling */
#     .css-1d391kg {
#         background-color: #fafafa;
#         color: #4f8af4;
#     }
#     /* Title color */
#     h1 {
#         color: #ff6347;
#     }
#     /* Card styling */
#     .metric-card {
#         padding: 10px;
#         border-radius: 10px;
#         background-color: #4f8af4;
#         color: white;
#         font-size: 20px;
#         text-align: center;
#         margin: 10px;
#         flex-grow: 1;
#     }
#     /* Container for metric cards */
#     .metric-container {
#         display: flex;
#         justify-content: space-around;
#     }
#     /* Divider style */
#     .divider {
#         border-top: 2px solid #4f8af4;
#         margin: 40px 0;
#     }
# </style>
# """, unsafe_allow_html=True)

# # Title of the dashboard
# st.title('Power Generation Analysis')

# # Load the dataset
# @st.cache_data  # Use the cache decorator to only load the data once

# def load_data():
#     data = pd.read_csv("C:/Users/terre/Documents/CODES/VAP/grid_analysis/file8.csv")
#     data['Date'] = pd.to_datetime(data['Date'], errors='coerce')  # Convert 'Date' to datetime format
#     data['Year'] = data['Date'].dt.year  # Extract year from the date for grouping
#     data['Month'] = data['Date'].dt.strftime('%Y-%m')  # Extract year-month for more detailed grouping
#     data['Day'] = data['Date'].dt.day  # Extract day
#     data['Hour'] = data['Date'].dt.hour  # Extract hour
#     data['Hour'] += 1
#     return data

# df = load_data()

# # Sidebar: adding filters for Genco Name and Date Range
# st.sidebar.header('Search')

# min_date, max_date = df['Date'].min(), df['Date'].max()

# start_date = st.sidebar.date_input("Start Date", min_value=min_date, max_value=max_date, value=min_date)
# end_date = st.sidebar.date_input("End Date", min_value=min_date, max_value=max_date, value=max_date)

# start_date = pd.to_datetime(start_date)
# end_date = pd.to_datetime(end_date)

# filtered_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]


# if 'Genco Name' in df.columns:
#     genco_options = ['All'] + list(df['Genco Name'].unique())
#     selected_gencos = st.sidebar.multiselect('Select Genco', options=genco_options, default='All')
#     if 'All' in selected_gencos:
#         selected_gencos = genco_options[1:]  # Include all Genco options
#     filtered_data = filtered_data[filtered_data['Genco Name'].isin(selected_gencos)]

# # Metric cards display
# total_gencos = filtered_data['Genco Name'].nunique()  # Count unique Gencos
# average_power_generated = round(filtered_data['TotalGeneration'].mean(), 2)  # Calculate average TotalGeneration
# average_restoration_time = round(filtered_data['Restoration_time'].mean())  # Calculate average Restoration Time
# average_operational_hours = round(filtered_data['Operational Hours'].mean())  # Calculate average Operational Hours
# average_downtime = round(filtered_data['Downtime Count'].sum())  # Calculate average Downtime

# st.markdown(f"""
# <div class='metric-container'>
#     <div class='metric-card'>Total Gencos: {total_gencos}</div>
#     <div class='metric-card'>Average Power Generated: {average_power_generated:.2f} MW</div>
#     <div class='metric-card'>Average Restoration Time: {average_restoration_time} hours</div>
#     <div class='metric-card'>Average Operational Hours: {average_operational_hours} hours</div>
#     <div class='metric-card'>Total Downtime Count: {average_downtime} times</div>
# </div>
# <div class='divider'></div>
# """, unsafe_allow_html=True)

# Display charts
chart1_col, chart2_col = st.columns(2)
chart3_col, chart4_col = st.columns(2)
chart5_col = st.columns(1)


with chart1_col:
    # Generate chart for Total Power Generation Trends
    if filtered_data.empty:
        st.write("No data available for the selected date range.")
    else:
        if start_date == end_date:
            # Filter data for the selected day
            day_data = filtered_data[filtered_data['Date'].dt.date == start_date.date()]
            # Group by hour and sum the PowerGenerated for each hour
            hourly_data = day_data.groupby('Hour').agg(TotalPowerGenerated=('TotalGeneration', 'sum')).reset_index()
            # Create a chart for the hourly power generation
            chart = alt.Chart(hourly_data).mark_bar().encode(
                x=alt.X('Hour:O', title='Hour of the Day'),
                y=alt.Y('TotalPowerGenerated:Q', title='Power Generated (MW)'),
                tooltip=[alt.Tooltip('Hour:O', title='Hour'), alt.Tooltip('TotalPowerGenerated:Q', title='Power Generated (MW)')]
            ).properties(
                title='Hourly Power Generation for Selected Day',
                width=350
            )
            st.altair_chart(chart, use_container_width=True)
        elif start_date.year == end_date.year and start_date.month == end_date.month:
            # Aggregating data by day when the same month and year are selected
            data_to_plot = filtered_data.groupby(filtered_data['Date'].dt.day)['TotalGeneration'].sum().reset_index(name='TotalGeneration')
            chart = alt.Chart(data_to_plot).mark_bar().encode(
                x=alt.X('Date:O', title='Day of the Month'),
                y=alt.Y('TotalGeneration:Q', title='Total Power Generated (MW)'),
                tooltip=[alt.Tooltip('Date:O', title='Day'), alt.Tooltip('TotalGeneration:Q', title='Total Power Generated (MW)')]
            ).properties(
                title='Daily Power Generation Trends',
                width=350
            )
            st.altair_chart(chart, use_container_width=True)
        elif start_date.year == end_date.year:
            data_to_plot = filtered_data.groupby('Month')['TotalGeneration'].sum().reset_index()
            data_to_plot['Month'] = pd.to_datetime(data_to_plot['Month'])
            chart = alt.Chart(data_to_plot).mark_bar().encode(
                x=alt.X('month(Month):O', title='Month'),
                y=alt.Y('TotalGeneration:Q', title='Total Power Generated (MW)'),
                tooltip=[alt.Tooltip('month(Month):O', title='Month'), alt.Tooltip('TotalGeneration:Q', title='Total Power Generated (MW)')]
            ).properties(
                title='Monthly Power Generation Trends',
                width=350
            )
            st.altair_chart(chart, use_container_width=True)
        else:
            data_to_plot = filtered_data.groupby('Year')['TotalGeneration'].sum().reset_index()
            chart = alt.Chart(data_to_plot).mark_bar().encode(
                x=alt.X('Year:O', title='Year'),
                y=alt.Y('TotalGeneration:Q', title='Total Power Generated (MW)'),
                tooltip=[alt.Tooltip('Year:O', title='Year'), alt.Tooltip('TotalGeneration:Q', title='Total Power Generated (MW)')]
            ).properties(
                title='Yearly Power Generation Trends',
                width=350
            )
            st.altair_chart(chart, use_container_width=True)



with chart2_col:
    # Generate chart for Average Operational Hours
    if start_date == end_date:  # Display hourly data if only one day is selected
        hourly_data = filtered_data.groupby(['Hour'])['Operational Hours'].mean().reset_index()
        operational_hours_chart = alt.Chart(hourly_data).mark_line(point=True).encode(
            x=alt.X('Hour:O', title='Hour of the Day'),
            y=alt.Y('Operational Hours:Q', title='Average Operational Hours'),
            tooltip=['Hour:O', 'Operational Hours:Q']
        ).properties(
            title='Hourly Average Operational Hours',
            width=350
        )
    elif start_date.month == end_date.month:  # Display daily data if within the same month
        daily_data = filtered_data.groupby(filtered_data['Date'].dt.day)['Operational Hours'].mean().reset_index()
        operational_hours_chart = alt.Chart(daily_data).mark_line(point=True).encode(
            x=alt.X('Date:O', title='Day of the Month'),
            y=alt.Y('Operational Hours:Q', title='Average Operational Hours'),
            tooltip=['Date:O', 'Operational Hours:Q']
        ).properties(
            title='Daily Average Operational Hours',
            width=350
        )
    else:  # Year or default view
        if start_date.year == end_date.year:
            monthly_data = filtered_data.groupby('Month')['Operational Hours'].mean().reset_index()
            monthly_data['Month'] = pd.to_datetime(monthly_data['Month'])
            operational_hours_chart = alt.Chart(monthly_data).mark_line(point=True).encode(
                x=alt.X('month(Month):O', title='Month'),
                y=alt.Y('Operational Hours:Q', title='Average Operational Hours'),
                tooltip=['month(Month):O', 'Operational Hours:Q']
            ).properties(
                title='Monthly Average Operational Hours',
                width=350
            )
        else:
            yearly_data = filtered_data.groupby('Year')['Operational Hours'].mean().reset_index()
            operational_hours_chart = alt.Chart(yearly_data).mark_line(point=True).encode(
                x=alt.X('Year:O', title='Year'),
                y=alt.Y('Operational Hours:Q', title='Average Operational Hours'),
                tooltip=['Year:O', 'Operational Hours:Q']
            ).properties(
                title='Yearly Average Operational Hours',
                width=350
            )
    st.altair_chart(operational_hours_chart, use_container_width=True)

with chart3_col:
    # Generate chart for Total Downtime Count Trends
    if start_date == end_date:  # Display hourly data if only one day is selected
        hourly_downtime = filtered_data.groupby(['Hour'])['Downtime Count'].sum().reset_index()
        downtime_chart = alt.Chart(hourly_downtime).mark_bar().encode(
            y=alt.Y('Hour:O', title='Hour of the Day', axis=alt.Axis(ticks=True)),
            x=alt.X('Downtime Count:Q', title='Total Downtime Count'),
            tooltip=['Hour:O', 'Downtime Count:Q']
        ).properties(
            title='Hourly Downtime Count',
            width=350
        )
    elif start_date.month == end_date.month:  # Display daily data if within the same month
        daily_downtime = filtered_data.groupby(filtered_data['Date'].dt.day)['Downtime Count'].sum().reset_index()
        downtime_chart = alt.Chart(daily_downtime).mark_bar().encode(
            y=alt.Y('Date:O', title='Day of the Month', axis=alt.Axis(ticks=True)),
            x=alt.X('Downtime Count:Q', title='Total Downtime Count'),
            tooltip=['Date:O', 'Downtime Count:Q']
        ).properties(
            title='Daily Downtime Count',
            width=350
        )
    else:  # Year or default view
        if start_date.year == end_date.year:
            monthly_downtime = filtered_data.groupby('Month')['Downtime Count'].sum().reset_index()
            monthly_downtime['Month'] = pd.to_datetime(monthly_downtime['Month'])
            downtime_chart = alt.Chart(monthly_downtime).mark_bar().encode(
                y=alt.Y('month(Month):O', title='Month', axis=alt.Axis(ticks=True)),
                x=alt.X('Downtime Count:Q', title='Total Downtime Count'),
                tooltip=['month(Month):O', 'Downtime Count:Q']
            ).properties(
                title='Monthly Downtime Count',
                width=350
            )
        else:
            yearly_downtime = filtered_data.groupby('Year')['Downtime Count'].sum().reset_index()
            downtime_chart = alt.Chart(yearly_downtime).mark_bar().encode(
                y=alt.Y('Year:O', title='Year', axis=alt.Axis(ticks=True)),
                x=alt.X('Downtime Count:Q', title='Total Downtime Count'),
                tooltip=['Year:O', 'Downtime Count:Q']
            ).properties(
                title='Yearly Downtime Count',
                width=350
            )
    st.altair_chart(downtime_chart, use_container_width=True)

with chart4_col:
    # Generate chart for Restoration Duration Trends
    if start_date == end_date:  # Display hourly data if only one day is selected
        hourly_restoration = filtered_data.groupby(['Hour'])['Restoration_time'].mean().reset_index()
        restoration_chart = alt.Chart(hourly_restoration).mark_line(point=True).encode(
            x=alt.X('Hour:O', title='Hour of the Day'),
            y=alt.Y('Restoration_time:Q', title='Average Restoration Duration'),
            tooltip=['Hour:O', 'Restoration_time:Q']
        ).properties(
            title='Hourly Restoration Duration',
            width=350
        )
    elif start_date.month == end_date.month:  # Display daily data if within the same month
        daily_restoration = filtered_data.groupby(filtered_data['Date'].dt.day)['Restoration_time'].mean().reset_index()
        restoration_chart = alt.Chart(daily_restoration).mark_line(point=True).encode(
            x=alt.X('Date:O', title='Day of the Month'),
            y=alt.Y('Restoration_time:Q', title='Average Restoration Duration'),
            tooltip=['Date:O', 'Restoration_time:Q']
        ).properties(
            title='Daily Restoration Duration',
            width=350
        )
    else:  # Year or default view
        if start_date.year == end_date.year:
            monthly_restoration = filtered_data.groupby('Month')['Restoration_time'].mean().reset_index()
            monthly_restoration['Month'] = pd.to_datetime(monthly_restoration['Month'])
            restoration_chart = alt.Chart(monthly_restoration).mark_line(point=True).encode(
                x=alt.X('month(Month):O', title='Month'),
                y=alt.Y('Restoration_time:Q', title='Average Restoration Duration'),
                tooltip=['month(Month):O', 'Restoration_time:Q']
            ).properties(
                title='Monthly Restoration Duration',
                width=350
            )
        else:
            yearly_restoration = filtered_data.groupby('Year')['Restoration_time'].mean().reset_index()
            restoration_chart = alt.Chart(yearly_restoration).mark_line(point=True).encode(
                x=alt.X('Year:O', title='Year'),
                y=alt.Y('Restoration_time:Q', title='Average Restoration Duration'),
                tooltip=['Year:O', 'Restoration_time:Q']
            ).properties(
                title='Yearly Restoration Duration',
                width=350
            )
    st.altair_chart(restoration_chart, use_container_width=True)


# Generate chart for Max and Min Power Trends
# Generate chart for Max and Min Power Trends
power_data = filtered_data.groupby('Genco Name').agg(
    Max_Power=('Max Power', 'max'),
    Min_Power=('Min Power', 'min')
).reset_index()
melted_power_data = power_data.melt(
    id_vars=['Genco Name'],
    value_vars=['Max_Power', 'Min_Power'],
    var_name='Type',
    value_name='Power'
)
power_chart = alt.Chart(melted_power_data).mark_bar().encode(
    x=alt.X('Genco Name:N', axis=alt.Axis(title='Genco Name')),
    y=alt.Y('Power:Q', axis=alt.Axis(title='Power (MW)')),
    color='Type:N',
    column='Type:N'
).properties(
    title="Max and Min Power by Genco",
    width=350
)

st.altair_chart(power_chart, use_container_width=True)
