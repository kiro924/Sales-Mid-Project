
import plotly.graph_objects as go
import pandas as pd
import streamlit as st
import plotly.express as px

colors = px.colors.qualitative.Dark24
colors2 = px.colors.qualitative.Set2
colors3 = px.colors.qualitative.Dark2

df=pd.read_csv('New Data.csv')

st.set_page_config(layout='wide',
                  page_title='Dashboard',
                  page_icon='📊')

tab1, tab2, tab3, tab4=st.tabs(['Sales Analysis','Products Analysis','Regions Analysis','Returns Analysis'])

with tab1:    
    col1, col2, col3=st.columns([4,4,4])

    col1.markdown(f'''
    <div class="metric" style="background-color: white; border-radius: 10px; padding: 20px; text-align: center; color: red; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <h3>Profits</h3>
        <p style="font-size: 32px; font-family: 'Courier New', monospace; font-weight: bold;">
            {int(df['Profit'].sum()):,}
        </p>
    </div>
''', unsafe_allow_html=True)

    col2.markdown(f'''
    <div class="metric" style="background-color: white; border-radius: 10px; padding: 20px; text-align: center; color: red; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <h3>Sales</h3>
        <p style="font-size: 32px; font-family: 'Courier New', monospace; font-weight: bold;">
            {int(df['ProductPrice'].sum()):,}
        </p>
    </div>
''', unsafe_allow_html=True)

    total_profit = df['Profit'].sum()
    total_sales = df['ProductPrice'].sum()
    profit_margin = (total_profit / total_sales) * 100
    col3.markdown(f'''
    <div class="metric" style="background-color: white; border-radius: 10px; padding: 20px; text-align: center; color: red; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <h3>Profit Margin</h3>
        <p style="font-size: 32px; font-family: 'Courier New', monospace; font-weight: bold;">
            {profit_margin:.2f}%
        </p>
    </div>
''', unsafe_allow_html=True)

    
    top_months=df.groupby('Month Name')[['Profit']].sum().sort_values(ascending=False, by='Profit')
    fig1=go.Figure()
    fig1.add_trace(go.Bar(x=top_months.index,
                         y=top_months['Profit'],
                         text=top_months['Profit']))
    
    fig1.update_layout(
        title='Total Profit by Months',
        xaxis_title='Months',
        yaxis_title='Total Profit'
        )
    fig1.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15) 
    col1.plotly_chart(fig1)

    top_Week=df.groupby('Week')[['Profit']].sum().sort_values(ascending=False, by='Week').head(10)
    fig2=go.Figure()
    fig2.add_trace(go.Bar(x=top_Week.index,
                          y=top_Week['Profit'],
                          text=top_Week['Profit']))
    fig2.update_layout(
        title='Total Profit by Weeks',
        xaxis_title='Weeks',
        yaxis_title='Total Profit'
        )
    fig2.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15)
    col2.plotly_chart(fig2)


    top_Day=df.groupby('Day')[['Profit']].sum().sort_values(ascending=False, by='Profit').head(10)
    fig3=go.Figure()
    fig3.add_trace(go.Bar(x=top_Day.index,
                          y=top_Day['Profit'],
                          text=top_Day['Profit']))   
    fig3.update_layout(
        title='Total Profit by Days',
        xaxis_title='Days',
        yaxis_title='Total Profit',
        )
    fig3.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15) 
    col3.plotly_chart(fig3)

    top_months=df.groupby('Month Name')[['OrderQuantity']].sum().sort_values(ascending=False, by='OrderQuantity')
    fig4=go.Figure()
    fig4.add_trace(go.Bar(x=top_months.index,
                          y=top_months['OrderQuantity'],
                          text=top_months['OrderQuantity']))
    
    fig4.update_layout(
        title='Total Quantaties by Months',
        xaxis_title='Months',
        yaxis_title='Quantities'
        )
    fig4.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15)
    
    col1.plotly_chart(fig4)

    top_Week=df.groupby('Week')[['OrderQuantity']].sum().sort_values(ascending=False, by='OrderQuantity').head(10)
    fig5=go.Figure()
    fig5.add_trace(go.Bar(x=top_Week.index,
                          y=top_Week['OrderQuantity'],
                          text=top_Week['OrderQuantity']))
    fig5.update_layout(
        title='Total Quantaties by Weeks',
        xaxis_title='Weeks',
        yaxis_title='Quantities'
        )
    fig5.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15)

    col2.plotly_chart(fig5)

    top_Day=df.groupby('Day')[['OrderQuantity']].sum().sort_values(ascending=False, by='OrderQuantity').head(10)
    fig6=go.Figure()
    fig6.add_trace(go.Bar(x=top_Day.index,
                          y=top_Day['OrderQuantity'],
                          text=top_Day['OrderQuantity']))   
    fig6.update_layout(
        title='Total Quantities by Days',
        xaxis_title='Days',
        yaxis_title='Quantities',
        )
    fig6.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15)
    col3.plotly_chart(fig6)


with tab2:
    col1, col2, col3=st.columns([3,3,3])
    
    top_category = df.groupby('CategoryName')[['Profit']].sum().sort_values(ascending=False, by='Profit').reset_index()
    top_category_name = top_category.loc[0, 'CategoryName']
    col1.markdown(f'''
    <div class="metric" style="background-color: white; border-radius: 10px; padding: 20px; text-align: center; color: red; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <h3>Top Category</h3>
        <p style="font-size: 32px; font-family: 'Courier New', monospace; font-weight: bold;">
            {top_category_name}
        </p>
    </div>
''', unsafe_allow_html=True)
    
    top_SubcategoryName=df.groupby('SubcategoryName')[['Profit']].sum().sort_values(ascending=False, by='Profit').head(10)
    top_subcategory_name = top_SubcategoryName.index[0]
    col2.markdown(f'''
    <div class="metric" style="background-color: white; border-radius: 10px; padding: 20px; text-align: center; color: red; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <h3>Top Sub Category</h3>
        <p style="font-size: 32px; font-family: 'Courier New', monospace; font-weight: bold;">
            {top_subcategory_name}
        </p>
    </div>
''', unsafe_allow_html=True)
    
    top_productname=df.groupby('ProductName')[['Profit']].sum().sort_values(ascending=False, by='Profit').head(10)
    top_product_name = top_productname.index[0]
    col3.markdown(f'''
    <div class="metric" style="background-color: white; border-radius: 10px; padding: 20px; text-align: center; color: red; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <h3>Top Product</h3>
        <p style="font-size: 32px; font-family: 'Courier New', monospace; font-weight: bold;">
            {top_product_name}
        </p>
    </div>
''', unsafe_allow_html=True)

    top_category = df.groupby('CategoryName')[['Profit']].sum().sort_values(ascending=False, by='Profit').reset_index()
    fig1 = px.pie(top_category, names='CategoryName', values='Profit', title='Profit for Each Category',hole=0.4) 
    fig1.update_traces(
        textposition='outside',
        texttemplate='%{label}: %{value:,.0f}',
        textfont_size=15)
    fig1.update_layout(
        showlegend=True,
        width=600,
        height=600)
    fig1.update_layout(
        yaxis_title="Profit",
        xaxis_title="Category",
       uniformtext_minsize=13,
    ) 
    col1.plotly_chart(fig1)


    top_SubcategoryName=df.groupby('SubcategoryName')[['Profit']].sum().sort_values(ascending=False, by='Profit').head(10)
    fig2=go.Figure()
    fig2.add_trace(go.Bar(x=top_SubcategoryName.index,
                           y=top_SubcategoryName['Profit'],
                           text=top_SubcategoryName['Profit']))
    fig2.update_layout(
    title=' Profits Over Top 10 Subcategory',
    xaxis_title='Subcategory',
    yaxis_title='Profit',
    )
    fig2.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15)
    col2.plotly_chart(fig2)

    top_productname=df.groupby('ProductName')[['Profit']].sum().sort_values(ascending=False, by='Profit').head(10)
    fig3=go.Figure()
    fig3.add_trace(go.Bar(x=top_productname.index,
                          y=top_productname['Profit'],
                          text=top_productname['Profit'])) 
    fig3.update_layout(
        title='Top 10 Profits Over Product Name',
        xaxis_title='Product',
        yaxis_title='Profit',
        )
    fig3.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15)
    col3.plotly_chart(fig3)

    top_ModelName=df.groupby('ModelName')[['Profit']].sum().sort_values(ascending=False, by='Profit').head(10)
    fig4=go.Figure()
    fig4.add_trace(go.Bar(x=top_ModelName.index,
                          y=top_ModelName['Profit'],
                          text=top_ModelName['Profit']))
    fig4.update_layout(
        title='Top 10 Profits Over Model Name',
        xaxis_title='Model',
        yaxis_title='Profit',
        )
    fig4.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15)
    col1.plotly_chart(fig4)

    

    top_category=df.groupby('CategoryName')[['OrderQuantity']].sum().sort_values(ascending=False, by='OrderQuantity').reset_index()
    fig5 = px.pie(top_category, names='CategoryName', values='OrderQuantity', title='Quantities for Each Category',hole=0.4) 
    fig5.update_traces(
    texttemplate='%{label}: %{value:,}',  # Display value with commas
    textposition='inside',
    textfont_size=17,
    insidetextorientation='radial'
    )
    
    fig5.update_layout(
    width=700,   # Adjust width here
    height=600,  # Adjust height here
    margin=dict(t=50, b=50, l=50, r=50),
    title_font_size=20
    )
    fig5.update_layout(
    xaxis_title='Category',
    yaxis_title='Quantities',
    )
    col2.plotly_chart(fig5)

    top_productname=df.groupby('ProductName')[['OrderQuantity']].sum().sort_values(ascending=False, by='OrderQuantity').head(10)
    fig6=go.Figure()
    fig6.add_trace(go.Bar(x=top_productname.index,
                          y=top_productname['OrderQuantity'],
                          text=top_productname['OrderQuantity']
                        )) 
    fig6.update_layout(
        title='Top 10 Quantities Over Product',
        xaxis_title='Product',
        yaxis_title='Quantities',
        )
    fig6.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15)
    col3.plotly_chart(fig6)


    top_ModelName=df.groupby('ModelName')[['Profit']].sum().sort_values(ascending=False, by='Profit').head(10)
    fig7=go.Figure()
    fig7.add_trace(go.Bar(x=top_ModelName.index,
                          y=top_ModelName['Profit'],
                          text=top_ModelName['Profit']
                        ))
    fig7.update_layout(
        title='Profits Over Top 10 Model',
        xaxis_title='Model',
        yaxis_title='Profit')
    fig7.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15)
    col1.plotly_chart(fig7)


with tab3:
    col1, col2, col3=st.columns([3,3,3])

    top_continent=df.groupby('Continent')[['Profit']].sum().sort_values(ascending=False, by='Profit')    
    topcontinent = top_continent.index[0]
    col1.markdown(f'''
    <div class="metric" style="background-color: white; border-radius: 10px; padding: 20px; text-align: center; color: red; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <h3>Top Category</h3>
        <p style="font-size: 32px; font-family: 'Courier New', monospace; font-weight: bold;">
            {topcontinent}
        </p>
    </div>
''', unsafe_allow_html=True)

    top_country=df.groupby('Country')[['Profit']].sum().sort_values(ascending=False, by='Profit')    
    topcountry = top_country.index[0]
    col2.markdown(f'''
    <div class="metric" style="background-color: white; border-radius: 10px; padding: 20px; text-align: center; color: red; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <h3>Top Country</h3>
        <p style="font-size: 32px; font-family: 'Courier New', monospace; font-weight: bold;">
            {topcountry}
        </p>
    </div>
''', unsafe_allow_html=True)

    top_regions=df.groupby('Region')[['Profit']].sum().sort_values(ascending=False, by='Profit')    
    topregions = top_regions.index[0]
    col3.markdown(f'''
    <div class="metric" style="background-color: white; border-radius: 10px; padding: 20px; text-align: center; color: red; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <h3>Top Region</h3>
        <p style="font-size: 32px; font-family: 'Courier New', monospace; font-weight: bold;">
            {topregions}
        </p>
    </div>
''', unsafe_allow_html=True)

    continent=df.groupby('Continent')[['Profit']].sum().sort_values(ascending=False, by='Profit').reset_index()
    fig1 = px.pie(continent, names='Continent', values='Profit', title='Profit In Each Continent',hole=0.4) 
    fig1.update_traces(
        textposition='inside',
        texttemplate='%{label}: %{value:,.0f}',
        textfont_size=15)
    fig1.update_layout(
        showlegend=True,
        width=600,
        height=600)
    fig1.update_layout(
        title='Profits  In Each Continent',
        xaxis_title='Continent',
        yaxis_title='Profit')
    col1.plotly_chart(fig1)

    top_country=df.groupby('Country')[['Profit']].sum().sort_values(ascending=False, by='Profit')
    fig2=go.Figure()
    fig2.add_trace(go.Bar(x=top_country.index,
                          y=top_country['Profit'],
                          text=top_country['Profit']
                        ))
    fig2.update_layout(
        title='Profits In Every Country',
        xaxis_title='Country',
        yaxis_title='Profit')
    fig2.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15)
    col2.plotly_chart(fig2)

    

    top_regions=df.groupby('Region')[['Profit']].sum().sort_values(ascending=False, by='Profit')
    fig3=go.Figure()
    fig3.add_trace(go.Bar(x=top_regions.index,
                          y=top_regions['Profit'],
                          text=top_regions['Profit']
                        ))
    fig3.update_layout(
        title='Profits In Every Region',
        xaxis_title='Regions',
        yaxis_title='Total Profit')
    fig3.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15)
    col3.plotly_chart(fig3)

    

    top_months= df.groupby(['Month Name', 'Continent'])[['Profit']].sum().sort_values(ascending=False, by='Profit').reset_index()    
    fig4 = px.bar(top_months, 
                 y='Month Name', 
                 x='Profit', 
                 color='Continent',  
                 title="profit in months and continent",
                 text='Profit'
                )
    fig4.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15)
    col1.plotly_chart(fig4)

    top_days= df.groupby(['Day', 'Continent'])[['Profit']].sum().sort_values(ascending=False, by='Profit').reset_index()    
    fig5 = px.bar(top_days, 
                 x='Day', 
                 y='Profit', 
                 color='Continent', 
                 title="profit from orders in days and continent",
                 text='Profit'
                )
    fig5.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15)
    col2.plotly_chart(fig5)


with tab4:
    returns=pd.read_csv('Returns.csv')
    col1, col2, col3 = st.columns([5,5,5]) 

    gross_profit_loss = int(returns['GrossProfitLoss'].sum())
    col1.markdown(f'''
        <div class="metric" style="background-color: white; border-radius: 10px; padding: 20px; text-align: center; color:red; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
            <h3>Returns</h3>
            <p style="font-size: 36px; font-family: 'Courier New', monospace; font-weight: bold;">
                ${gross_profit_loss:,.0f}
            </p>
        </div>
    ''', unsafe_allow_html=True)
    
    season_return = returns.groupby('Season')[['GrossProfitLoss']].sum().sort_values(ascending=False, by='GrossProfitLoss').reset_index()
    seasonreturn=season_return.loc[0, 'Season']
    col2.markdown(f'''
    <div class="metric" style="background-color: white; border-radius: 10px; padding: 20px; text-align: center; color: red; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <h3>Top Season</h3>
        <p style="font-size: 32px; font-family: 'Courier New', monospace; font-weight: bold;">
            {seasonreturn}
        </p>
    </div>
''', unsafe_allow_html=True)

    day_return=returns.groupby('Day')[['GrossProfitLoss']].sum().sort_values(ascending=False, by='GrossProfitLoss').reset_index()
    dayreturn=day_return.loc[0, 'Day']
    col3.markdown(f'''
    <div class="metric" style="background-color: white; border-radius: 10px; padding: 20px; text-align: center; color: red; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <h3>Top Day</h3>
        <p style="font-size: 32px; font-family: 'Courier New', monospace; font-weight: bold;">
            {dayreturn}
        </p>
    </div>
''', unsafe_allow_html=True)

    season_return = returns.groupby('Season')[['GrossProfitLoss']].sum().astype(int).sort_values(ascending=False, by='GrossProfitLoss').reset_index()
    fig7 = px.pie(season_return, names='Season', values='GrossProfitLoss', title='Return in Each Season', hole=0.4) 
    fig7.update_traces(
        textinfo='value+label',
        textfont_size=15
    ) 
    col1.plotly_chart(fig7)


    month_return=returns.groupby('Month')[['GrossProfitLoss']].sum().sort_values(ascending=False, by='GrossProfitLoss').reset_index()
    fig1=px.bar(month_return, x='Month', y='GrossProfitLoss', title='return in each month'.title(), text='GrossProfitLoss')
    fig1.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15
    )
    col1.plotly_chart(fig1)

    week_return=returns.groupby('Week')[['GrossProfitLoss']].sum().sort_values(ascending=False, by='GrossProfitLoss').reset_index()
    fig2=px.bar(week_return, x='Week', y='GrossProfitLoss', title='return in each month'.title(), text='GrossProfitLoss')
    fig2.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15
    )
    col2.plotly_chart(fig2)

    day_return=returns.groupby('Day')[['GrossProfitLoss']].sum().astype(int).reset_index()
    fig3 = px.line(day_return, x='Day', y='GrossProfitLoss', title='Return on Each Day', text='GrossProfitLoss')
    fig3.update_traces(
    texttemplate='%{text:.2f}',  
    textposition='top right',
    textfont_size=15
    )
    col3.plotly_chart(fig3)


    continent_return=returns.groupby('Continent')[['GrossProfitLoss']].sum().astype(int).sort_values(ascending=False, by='GrossProfitLoss').reset_index()
    fig4 = px.pie(continent_return, names='Continent', values='GrossProfitLoss', title='Return in Each Continent', hole=0.4) 
    fig4.update_traces(
        textinfo='value+label',
        textfont_size=15
    ) 
    col1.plotly_chart(fig4)

    country_return=returns.groupby('Country')[['GrossProfitLoss']].sum().sort_values(ascending=False, by='GrossProfitLoss').reset_index()
    fig5=px.bar(country_return, x='Country', y='GrossProfitLoss', title='return in each country'.title(), text='GrossProfitLoss')
    fig5.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15
    )
    col2.plotly_chart(fig5)

    region_return=returns.groupby('Region')[['GrossProfitLoss']].sum().sort_values(ascending=False, by='GrossProfitLoss').reset_index()
    fig6=px.bar(region_return, x='Region', y='GrossProfitLoss', title='return in each region'.title(), text='GrossProfitLoss')
    fig6.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15
    )
    col3.plotly_chart(fig6)

    
    category_return=returns.groupby('CategoryName')[['GrossProfitLoss']].sum().sort_values(ascending=False, by='GrossProfitLoss').reset_index().head(10)
    fig8 = px.pie(category_return, names='CategoryName', values='GrossProfitLoss', title='Return for Each Category',hole=0.4) 
    fig8.update_traces(
        textposition='outside',
        texttemplate='%{label}: %{value:,.0f}',
        textfont_size=15)
    fig8.update_layout(
        showlegend=True,
        width=600,
        height=600)

    
    col3.plotly_chart(fig8)
    

    subcategory_return=returns.groupby('SubcategoryName')[['GrossProfitLoss']].sum().sort_values(ascending=False, by='GrossProfitLoss').reset_index().head(10)
    fig9=px.bar(subcategory_return, x='SubcategoryName', y='GrossProfitLoss', title='return for each subcategory'.title(), text='GrossProfitLoss')
    fig9.update_traces(
        texttemplate='%{text:.2s}', 
        textposition='outside',
        textfont_size=15
    )
    col2.plotly_chart(fig9)
