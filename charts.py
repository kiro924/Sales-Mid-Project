
import plotly.graph_objects as go
import pandas as pd
import streamlit as st
import plotly.express as px

colors = px.colors.qualitative.Dark24
colors2 = px.colors.qualitative.Set2
colors3 = px.colors.qualitative.Dark2

df=pd.read_csv('New Data')

st.set_page_config(layout='wide',
                  page_title='Dashboard',
                  page_icon='📊')

tab1, tab2, tab3, tab=st.tabs(['Univariate Analysis','Bivariate Analysis','Multivariate Analysis','Line Plot Analysis'])

with tab1:    
    col1, col2, col3=st.columns([4,4,4])
    top_10_order_dates = df['OrderDate'].value_counts().sort_values(ascending=False).head(10)
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        x=top_10_order_dates.index, 
        y=top_10_order_dates.values,  
        marker=dict(color=colors),
        
    ))
    fig1.update_layout(title="count of top 10 order dates".title())
    col1.plotly_chart(fig1)

    top_10_stock_dates=df['StockDate'].value_counts().sort_values(ascending=False).head(10)
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=top_10_stock_dates.index,    
        y=top_10_stock_dates.values,   
        marker=dict(color=colors2)      
    ))
    fig2.update_layout(title="count of top 10 stock dates".title())
    col2.plotly_chart(fig2)


    top_10_return_date=df['ReturnDate'].value_counts().sort_values(ascending=False).head(10)
    fig4=go.Figure()
    fig4.add_trace(go.Bar(x=top_10_return_date.index,
                       y=top_10_return_date.values,
                       marker=dict(color=colors)
                       ))
    fig4.update_layout(title="count of top 10 return dates".title())
    col1.plotly_chart(fig4)

    top_10_subcat_name=df['SubcategoryName'].value_counts().sort_values(ascending=False).head(10)
    fig5=go.Figure()
    fig5.add_trace(go.Bar(x=top_10_subcat_name.index,
                       y=top_10_subcat_name.values,
                       marker=dict(color=colors2)
                       ))
    fig5.update_layout(title="count of top 10 subcategory name".title())
    col2.plotly_chart(fig5)

    top_cat_name=df['CategoryName'].value_counts().sort_values(ascending=False)
    fig6=go.Figure()
    fig6.add_trace(go.Bar(x=top_cat_name.index,
                       y=top_cat_name.values,
                       marker=dict(color=colors3)
                       ))
    fig6.update_layout(title="count of top category name".title())
    col3.plotly_chart(fig6)


with tab2:
    col1, col2, col3=st.columns([3,3,3])

    top_months=df.groupby('Month Name')[['Profit']].sum().sort_values(ascending=False, by='Profit')
    fig1=go.Figure()
    fig1.add_trace(go.Bar(x=top_months.index,
                       y=top_months['Profit'],
                       marker=dict(color=colors)
                       ))

    fig1.update_layout(
        title='Total Profit In Each Month',
        xaxis_title='Months',
        yaxis_title='Total Profit',)

    col1.plotly_chart(fig1)

    top_Week=df.groupby('Week')[['Profit']].sum().sort_values(ascending=False, by='Week').head(10)
    fig2=go.Figure()
    fig2.add_trace(go.Bar(x=top_Week.index,
                       y=top_Week['Profit'],
                       marker=dict(color=colors2)
                       ))

    fig2.update_layout(
        title='Total Profit In Each Week',
        xaxis_title='Weeks',
        yaxis_title='Total Profit',)
    
    col2.plotly_chart(fig2)

    top_Day=df.groupby('Day')[['Profit']].sum().sort_values(ascending=False, by='Profit').head(10)
    fig3=go.Figure()
    fig3.add_trace(go.Bar(x=top_Day.index,
                       y=top_Day['Profit'],
                       marker=dict(color=colors3)
                       ))
    fig3.update_layout(
        title='Total Profit In Each Day',
        xaxis_title='Days',
        yaxis_title='Total Profit',)
    col3.plotly_chart(fig3)

    top_season=df.groupby('Order Season')[['Profit']].sum().sort_values(ascending=False, by='Profit')
    fig4=go.Figure()
    fig4.add_trace(go.Bar(x=top_season.index,
                       y=top_season['Profit'],
                       marker=dict(color=colors)
                        ))
    fig4.update_layout(
        title='Total Profit In Each Season',
        xaxis_title='Seasons',
        yaxis_title='Total Profit',
        )
    col1.plotly_chart(fig4)

    top_return_season=df.groupby('Return Season')[['Profit']].sum().sort_values(ascending=False, by='Profit')
    fig5=go.Figure()
    fig5.add_trace(go.Bar(x=top_return_season.index,
                       y=top_return_season['Profit'],
                       marker=dict(color=colors2)
                        ))
    fig5.update_layout(
        title='Total Amount of Returns In Each Season',
        xaxis_title='Return Seasons',
        yaxis_title='Total Amount',)
    col2.plotly_chart(fig5)

    top_productname=df.groupby('ProductName')[['Profit']].sum().sort_values(ascending=False, by='Profit').head(10)
    fig6=go.Figure()
    fig6.add_trace(go.Bar(x=top_productname.index,
                       y=top_productname['Profit'],
                       marker=dict(color=colors3)
                        ))
    fig6.update_layout(
        title='Profits Over Top 10 Products ',
        xaxis_title='Product Name',
        yaxis_title='Total Profit',)
    col3.plotly_chart(fig6)

    top_ModelName=df.groupby('ModelName')[['Profit']].sum().sort_values(ascending=False, by='Profit').head(10)
    fig7=go.Figure()
    fig7.add_trace(go.Bar(x=top_ModelName.index,
                       y=top_ModelName['Profit'],
                       marker=dict(color=colors)
                        ))
    fig7.update_layout(
        title='Profits Over Top 10 Model Name',
        xaxis_title='Model Name',
        yaxis_title='Total Profit')
    col1.plotly_chart(fig7)

    top_regions=df.groupby('Region')[['Profit']].sum().sort_values(ascending=False, by='Profit').head(7)
    fig8=go.Figure()
    fig8.add_trace(go.Bar(x=top_regions.index,
                       y=top_regions['Profit'],
                       marker=dict(color=colors2)
                        ))
    fig8.update_layout(
        title='Profits In Every Region',
        xaxis_title='Regions',
        yaxis_title='Total Profit')
    col2.plotly_chart(fig8)

    continent=df.groupby('Continent')[['Profit']].sum().sort_values(ascending=False, by='Profit')
    fig9=go.Figure()
    fig9.add_trace(go.Bar(x=continent.index,
                       y=continent['Profit'],
                       marker=dict(color=colors3)
                        ))
    fig9.update_layout(
        title='Profits  In Each Continent',
        xaxis_title='Continent',
        yaxis_title='Total Profit')
    col3.plotly_chart(fig9)


with tab3:
    col1, col2, col3=st.columns([3,3,3])

    top_products = df.groupby(['ProductName', 'Order Season'])[['Profit']].sum().sort_values(ascending=False, by='Profit').reset_index().head(28)    
    fig1 = px.bar(top_products, 
                 x='ProductName', 
                 y='Profit', 
                 color='Order Season', 
                 title="Top 10 Products by Profit and Order Season",
                 color_discrete_sequence=colors  
                )
    col1.plotly_chart(fig1)

    top_products= df.groupby(['ProductName', 'Return Season'])[['Profit']].sum().sort_values(ascending=False, by='Profit').reset_index().head(30)    
    fig2 = px.bar(top_products, 
                 x='ProductName', 
                 y='Profit', 
                 color='Return Season',  
                 title="Top 10 Product Name By Return Season",
                 labels={'ProductName': 'Product Name', 'Profit': 'Profit'},  
                 color_discrete_sequence=colors2  
                )
    
    fig2.update_layout(
        yaxis_title="Total Amount",
    )
    
    col2.plotly_chart(fig2)

    top_model_name= df.groupby(['ModelName', 'Return Season'])[['Profit']].sum().sort_values(ascending=False, by='Profit').reset_index().head(31)
    fig3 = px.bar(top_model_name, 
                 x='ModelName', 
                 y='Profit', 
                 color='Return Season',  
                 title="Top 10 Amount Of Model Name by Return Season",
                 color_discrete_sequence=colors3  
                )
    fig3.update_layout(
        yaxis_title="Total Amount",
     )
    col3.plotly_chart(fig3)

    top_months= df.groupby(['Month Name', 'Continent'])[['Profit']].sum().sort_values(ascending=False, by='Profit').reset_index().head(31)    
    fig4 = px.bar(top_months, 
                 x='Month Name', 
                 y='Profit', 
                 color='Continent',  
                 title="profit in months and continent", 
                 color_discrete_sequence=colors
                )
    col1.plotly_chart(fig4)

    top_days= df.groupby(['Day', 'Continent'])[['Profit']].sum().sort_values(ascending=False, by='Profit').reset_index().head(31)    
    fig5 = px.bar(top_days, 
                 x='Day', 
                 y='Profit', 
                 color='Continent', 
                 title="profit from orders in days and continent",
                 color_discrete_sequence=colors2  
                )
    col2.plotly_chart(fig5)

    top_Return_Month= df.groupby(['Return_Month Name', 'Continent'])[['Profit']].sum().sort_values(ascending=False, by='Profit').reset_index()    
    fig6 = px.bar(top_Return_Month, 
                 x='Return_Month Name', 
                 y='Profit', 
                 color='Continent',  
                 title="total amount from returns in months and continent",
                 color_discrete_sequence=colors
                )
    fig6.update_layout(      
        yaxis_title="Total Amount",
    )
    col3.plotly_chart(fig6)

    top_Return_Day= df.groupby(['Return_Day', 'Continent'])[['Profit']].sum().sort_values(ascending=False, by='Profit').reset_index()    
    fig7 = px.bar(top_Return_Day, 
                 x='Return_Day', 
                 y='Profit', 
                 color='Continent',  
                 title="total amount from returns in days and continent",
                 color_discrete_sequence=colors2 
                )
    fig7.update_layout(     
        yaxis_title="Total Amount",
    )
    col2.plotly_chart(fig7)


with tab4:
    top_months=df.groupby('Month Name')[['Profit']].sum().sort_values(ascending=False, by='Profit')

    
