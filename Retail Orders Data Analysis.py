import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px




mydb = mysql.connector.connect(
    host="localhost", user="root", password="Jsa.5378724253@", auth_plugin="mysql_"
)
arun = mydb.cursor()

st.logo(r"C:\Users\firea\OneDrive\Desktop\logo.jpeg")
st.title(":blue[RETAIL ORDER DATA ANALYSIS]")
a = "View BarChart"
z = "View Query"
c = "View BarChart and View Query"
arun.execute("use retail_orders")


sdb = st.sidebar.radio(
    "Queries",
    [
        "Select a Query",
        "Query1",
        "Query2",
        "Query3",
        "Query4",
        "Query5",
        "Query6",
        "Query7",
        "Query8",
        "Query9",
        "Query10",
    ],
)
# 1


if sdb == "Query1":
    arun.execute(
        """select product_id as product_id,  sum(sale_price) as revenue from table_0 
group by product_id 
order by revenue desc
limit 10;
"""
    )

    st.subheader("Top 10 highest revenue generating products")
    st.table(arun)
    arun.execute(
        """select product_id as product_id,  sum(sale_price) as revenue from table_0 
group by product_id 
order by revenue desc
limit 10;
"""
    )
    st.write(":grey[Revenue]")
    a = pd.DataFrame(arun)
    a1 = px.pie(a, values=1, names=0)
    st.plotly_chart(a1)

    with st.expander("View Query"):
        st.code(
            """SELECT product_id
	,sum(sale_price) AS revenue
FROM table_0
GROUP BY product_id
ORDER BY revenue DESC limit 10;"""
        )
# 2
if sdb == "Query2":
    arun.execute(
        """
select city, (sum(profit)/sum(quantity))*100 as profit_margin from table_0
group by city 
order by profit_margin desc
limit 5;
"""
    )
    st.subheader("Cities with highest profit margins")
    st.table(arun)
    arun.execute(
        """
        select city, (sum(profit)/sum(quantity))*100 as profit_margin from table_0
group by city 
order by profit_margin desc
limit 5;
"""
    )
    st.write(":grey[Profit Margins]")
    b = pd.DataFrame(arun)
    b1 = px.pie(b, values=1, names=1)
    st.plotly_chart(b1)

    with st.expander(z):
        st.code(
            """
SELECT city
	,(sum(profit) / sum(quantity)) * 100 AS profit_margin
FROM table_0
GROUP BY city
ORDER BY profit_margin DESC limit 5;
"""
        )
# 3
if sdb == "Query3":
    arun.execute(
        """
      select category , sum(discount) as total_discount from table_0
group by category 
order by total_discount ;            
                  """
    )
    st.subheader("Discount given for each category")
    st.table(arun)
    arun.execute(
        """
      select category , sum(discount) as total_discount from table_0
group by category 
order by total_discount ;            
                  """
    )
    st.write(":grey[Total Discount]")
    c = pd.DataFrame(arun)
    c1 = px.pie(c, values=1, names=0)
    st.plotly_chart(c1)
    with st.expander(z):
        st.code(
            """SELECT category,sum(discount) AS total_discount
FROM table_0
GROUP BY category
ORDER BY total_discount;
             """
        )
# 4
if sdb == "Query4":
    arun.execute(
        """
                  select category , avg(sale_price) as average_sale_price from table_0
group by category 
order by average_sale_price;

                  """
    )
    st.subheader("Average Sale Price per Product Category ")
    st.table(arun)
    arun.execute(
        """
                  select category , avg(sale_price) as average_sale_price from table_0
group by category 
order by average_sale_price;

                  """
    )
    st.write(":grey[Average Sale Price]")
    d = pd.DataFrame(arun)
    d1 = px.pie(d, values=1, names=0)
    st.plotly_chart(d1)
    with st.expander(z):
        st.code(
            """
             SELECT category,avg(sale_price) AS average_sale_price
FROM table_0
GROUP BY category
ORDER BY average_sale_price;

             """
        )
# 5
if sdb == "Query5":
    arun.execute(
        """select region, avg(sale_price) average_sale_price from table_0
group by region
order by average_sale_price desc
limit 1;"""
    )
    st.subheader("Region with Highest Average Sale Price")
    st.table(arun)
    arun.execute(
        """select region, avg(sale_price) average_sale_price from table_0
group by region
order by average_sale_price desc
limit 1;"""
    )
    st.bar_chart(arun)
    with st.expander(z):
        st.code(
            """SELECT region,avg(sale_price) average_sale_price
FROM table_0
GROUP BY region
ORDER BY average_sale_price DESC limit 1;"""
        )

# 6
if sdb == "Query6":
    arun.execute(
        """
                  SELECT category,sum(profit) AS total_profit
FROM table_0
GROUP BY category
ORDER BY total_profit;
                  """
    )
    st.subheader("Total Profit Per Category")
    st.table(arun)
    arun.execute(
        """
                select category , sum(profit) as total_profit 
                from table_0
group by category 
order by total_profit;
                  """
    )
    st.write(":grey[Total Profit]")
    f = pd.DataFrame(arun)
    f1 = px.pie(f, values=1, names=0)
    st.plotly_chart(f1)
    with st.expander(z):
        st.code(
            """
            select category , sum(profit) as total_profit 
            from table_0
group by category 
order by total_profit; 
             """
        )

# 7
if sdb == "Query7":
    arun.execute(
        """
                  select segment, sum(quantity) as total_quantity 
                  from table_0
group by segment
order by total_quantity desc
limit 3;
                  """
    )
    st.subheader("Top 3 quantity per segment")
    st.table(arun)
    arun.execute(
        """
                  select segment, sum(quantity) as total_quantity 
                  from table_0
group by segment
order by total_quantity desc
limit 3;
                  """
    )
    st.write(":grey[Total Quantity]")
    g = pd.DataFrame(arun)
    g1 = px.pie(g, values=1, names=0)
    st.plotly_chart(g1)
    with st.expander(z):
        st.code(
            """
            select segment, sum(quantity) as total_quantity
            from table_0
group by segment
order by total_quantity desc
limit 3; 
             """
        )
# 8
if sdb == "Query8":
    arun.execute(
        """
                  select region , avg(discount) as average_discount from table_0
group by region 
order by average_discount ;
                  """
    )
    st.subheader("Average Discount Percentage per Region")
    st.table(arun)
    arun.execute(
        """
                  select region , avg(discount) as average_discount 
                  from table_0
group by region 
order by average_discount ;
                  """
    )
    st.write(":grey[Average Discount]")
    h = pd.DataFrame(arun)
    h1 = px.pie(h, values=1, names=0)
    st.plotly_chart(h1)
    with st.expander(z):
        st.code(
            """
            select region , avg(discount) as average_discount 
from table_0
group by region 
order by average_discount ;
             """
        )

# 9
if sdb == "Query9":
    arun.execute(
        """
                  select category, sum(profit) total_profit 
                  from table_0
group by category 
order by total_profit desc
limit 1;

                  """
    )
    st.subheader("Product Category With Highest Profit")
    st.table(arun)
    arun.execute(
        """
                  select category, sum(profit) total_profit 
                  from table_0
group by category 
order by total_profit desc
limit 1;

                  """
    )
    st.bar_chart(arun)
    with st.expander(z):
        st.code(
            """
            select category, sum(profit) total_profit
from table_0
group by category 
order by total_profit desc
limit 1;

             """
        )


# 10
if sdb == "Query10":
    arun.execute(
        """
     select year(order_date) as year_ ,sum(sale_price) as total_revenue 
     from table_0
group by year_
order by total_revenue;

               """
    )

    st.subheader("Product Category With Highest Profit")
    st.table(arun)
    arun.execute(
        """
     select year(order_date) as year_ ,sum(sale_price) as total_revenue 
     from table_0
group by year_
order by total_revenue;

               """
    )
    st.write(":grey[Total Revenue]")
    i = pd.DataFrame(arun)
    i1 = px.pie(i, names=0, values=1)
    st.plotly_chart(i1)
    with st.expander(z):
        st.code(
            """
     select year(order_date) as year_ ,sum(sale_price) as total_revenue 
from table_0
group by year_
order by total_revenue;

               """
        )

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Jsa.5378724253@", auth_plugin="mysql_"
)
arun = mydb.cursor()
arun.execute("Use retail_orders")

dbs = st.sidebar.radio(
    "Queries with Constraints",
    [
        "Select a Query",
        "Query11",
        "Query12",
        "Query13",
        "Query14",
        "Query15",
        "Query16",
        "Query17",
        "Query18",
        "Query19",
        "Query20",
    ],
)


# 11
if dbs == "Query11":
    arun.execute(
        """
select table_1.city , sum(table_2.profit) as total_profit 
from table_1
join table_2
on table_1.order_id=table_2.order_id
group by table_1.city
order by total_profit desc
limit 10;


                  """
    )
    st.subheader("Top 10 cities with Highest Profit")
    st.table(arun)
    arun.execute(
        """
select table_1.city , sum(table_2.profit) as total_profit
from table_1
join table_2
on table_1.order_id=table_2.order_id
group by table_1.city
order by total_profit desc
limit 10;


                  """
    )
    st.write(":grey[Total Profit]")
    j = pd.DataFrame(arun)
    j1 = px.pie(j, names=0, values=1)
    st.plotly_chart(j1)
    with st.expander(z):
        st.code(
            """
select table_1.city , sum(table_2.profit) as total_profit 
from table_1
join table_2
on table_1.order_id=table_2.order_id
group by table_1.city
order by total_profit desc
limit 10;


             """
        )

# 12
if dbs == "Query12":
    arun.execute(
        """
select table_1.state , sum(table_2.sale_price) as revenue
from table_1
join table_2 
on table_1.order_id=table_2.order_id
group by table_1.state
order by  revenue desc
limit 3;


                  """
    )
    st.subheader("Top 3 Highest Generating  States")
    st.table(arun)
    arun.execute(
        """
select table_1.state , sum(table_2.sale_price) as revenue 
from table_1
join table_2 
on table_1.order_id=table_2.order_id
group by table_1.state
order by  revenue desc
limit 3;


                  """
    )
    st.write(":grey[Revenue]")
    k = pd.DataFrame(arun)
    k1 = px.pie(k, names=0, values=1)
    st.plotly_chart(k1)
    with st.expander(z):

        st.code(
            """
select table_1.state , sum(table_2.sale_price) as revenue 
from table_1
join table_2 
on table_1.order_id=table_2.order_id
group by table_1.state
order by  revenue desc
limit 3;

             """
        )
# 13
if dbs == "Query13":
    arun.execute(
        """
select a.state, a.city, b.sub_category as Furniture from  table_1 as a
join table_2 as b
on a.order_id=b.order_id
where b.category='Furniture'
limit 50;

                  """
    )
    st.subheader("Cities and States Where the Furniture Sold")
    st.table(arun)
    arun.execute(
        """
select a.state, a.city, b.sub_category 
from  table_1 as a
join table_2 as b
on a.order_id=b.order_id
where b.category='Furniture'
limit 50;

                  """
    )

    with st.expander("view Barchart"):
        st.bar_chart(arun)
    with st.expander(z):
        st.code(
            """
select a.state, a.city, b.sub_category from  table_1 as a
join table_2 as b
on a.order_id=b.order_id
where b.category='Furniture'
limit 50;

             """
        )

# 14
if dbs == "Query14":
    arun.execute(
        """
select a.region, sum(b.sale_price)as Revenue 
from table_1 as a
join table_2 as b
on a.order_id=b.order_id
group by a.region
order by a.region ;

                  """
    )
    st.subheader("Find the Revenues From all the Region")
    st.table(arun)
    arun.execute(
        """
select a.region, sum(b.sale_price)as Revenue from table_1 as a
join table_2 as b
on a.order_id=b.order_id
group by a.region
order by a.region ;

                  """
    )
    st.write(":grey[Revenue]")
    l = pd.DataFrame(arun)
    l1 = px.pie(l, names=0, values=1)
    st.plotly_chart(l1)
    with st.expander(z):
        st.code(
            """
select a.region, sum(b.sale_price) from table_1 as a
join table_2 as b
on a.order_id=b.order_id
group by a.region
order by a.region ;
             """
        )

# 15
if dbs == "Query15":
    arun.execute(
        """
select a.city  , sum(b.profit) as total_profit 
from table_1 as a
join table_2 as b
on a.order_id=b.order_id
group by a.city
having total_profit >1000
order by a.city; 

                  """
    )
    st.subheader("Find the profit of the city having more than $1000")
    st.table(arun)
    arun.execute(
        """
select a.city  , sum(b.profit) as total_profit 
from table_1 as a
join table_2 as b
on a.order_id=b.order_id
group by a.city
having total_profit >1000
order by a.city; 

                  """
    )
    st.write(":grey[Total Profit]")
    m = pd.DataFrame(arun)
    m1 = px.pie(m, names=0, values=1)
    st.plotly_chart(m1)
    with st.expander(z):
        st.code(
            """
select a.city  , sum(b.profit) as total_profit 
from table_1 as a
join table_2 as b
on a.order_id=b.order_id
group by a.city
having total_profit >1000 
order by a.city; 
             """
        )
# 16
if dbs == "Query16":
    arun.execute(
        """
select a.postal_code, sum(b.discount) as total_discount 
from table_1 as a
join table_2 as b
on a.order_id=b.order_id
group by a.postal_code
order by total_discount desc
limit 10;

                  """
    )
    st.subheader("Top 10 Postal code has given the highest Discount")
    st.table(arun)
    arun.execute(
        """
select a.postal_code, sum(b.discount) as total_discount from table_1 as a
join table_2 as b
on a.order_id=b.order_id
group by a.postal_code
order by total_discount desc
limit 10;

                  """
    )
    st.write(":grey[Total Discount]")
    n = pd.DataFrame(arun)
    n1 = px.pie(n, names=0, values=1)
    st.plotly_chart(n1)
    with st.expander(z):
        st.code(
            """
select a.postal_code, sum(b.discount) as total_discount 
from table_1 as a
join table_2 as b
on a.order_id=b.order_id
group by a.postal_code
order by total_discount desc
limit 10;
             """
        )
# 17
if dbs == "Query17":
    arun.execute(
        """
select a.city ,sum( b. quantity) as Total_sold 
from table_1 as a
join table_2 as b
on a.order_id=b.order_id
group by a.city
order by Total_sold desc 
limit 5;

                  """
    )
    st.subheader("Top 5 Quantity Sold per City")
    st.table(arun)
    arun.execute(
        """
select a.city ,sum( b. quantity) as Total_sold from table_1 as a
join table_2 as b
on a.order_id=b.order_id
group by a.city
order by Total_sold desc 
limit 5;

                  """
    )
    st.write(":grey[Total Sold]")
    o = pd.DataFrame(arun)
    o1 = px.pie(o, names=0, values=1)
    st.plotly_chart(o1)
    with st.expander(z):
        st.code(
            """
select a.city ,sum( b. quantity) as Total_sold 
from table_1 as a
join table_2 as b
on a.order_id=b.order_id
group by a.city
order by Total_sold desc 
limit 5;
             """
        )

# 18
if dbs == "Query18":
    arun.execute(
        """
select a.country, count(b.sub_category) as HouseHold_Items 
from table_1 as a
join table_2 as b
on a.order_id = b.order_id
group by a.country
order by HouseHold_Items desc
limit 10;
                  """
    )
    st.subheader("Country Having the most Household Items")
    st.table(arun)
    arun.execute(
        """
select a.country, count(b.sub_category) as HouseHold_Items from table_1 as a
join table_2 as b
on a.order_id = b.order_id
group by a.country
order by Household_Items desc
limit 10;
                  """
    )
    with st.expander("View BarChart"):
        st.bar_chart(arun)
    with st.expander(z):
        st.code(
            """
select a.country, count(b.sub_category) as sub_category 
from table_1 as a
join table_2 as b
on a.order_id = b.order_id
group by a.country
order by sub_category desc
limit 10;
             """
        )

# 19
if dbs == "Query19":
    arun.execute(
        """
select a.city,b.sub_category as Furniture
from table_1 as a
join table_2 as b
on a.order_id=b.order_id
where a.city='los Angeles'
            limit 50;
                  """
    )
    st.subheader("Furniture Sold in the Los Angeles City")
    st.table(arun)
    arun.execute(
        """
select a.city,b.sub_category as Furniture from table_1 as a
join table_2 as b
on a.order_id=b.order_id
where a.city='los Angeles'
            limit 50;
                  """
    )
    with st.expander("View BarChart"):
        st.bar_chart(arun)
    with st.expander(z):
        st.code(
            """
select a.city,b.sub_category 
from table_1 as a
join table_2 as b
on a.order_id=b.order_id
where a.city='los Angeles'
limit 50;
             """
        )

# 20
if dbs == "Query20":
    arun.execute(
        """
SELECT 
    a.city, 
    b.sale_price AS SP,
    CASE
        WHEN b.sale_price > 300 THEN 'high'
        WHEN b.sale_price < 300 THEN 'low'
        ELSE 'NAN'
    END AS Sale_Category
FROM table_1 AS a
JOIN table_2 AS b
ON a.order_id= b.order_id
limit 50; 
                  """
    )
    st.subheader("Rate the sale price as Low and High with City.")
    st.table(arun)
    arun.execute(
        """
SELECT 
    a.city, 
    b.sale_price AS SP,
    CASE
        WHEN b.sale_price > 300 THEN 'high'
        WHEN b.sale_price < 300 THEN 'low'
        ELSE 'NAN'
    END AS Sale_Category
FROM 
    table_1 AS a
JOIN 
    table_2 AS b
ON 
    a.order_id= b.order_id
                limit 50; 
                  """
    )
    st.write("Sale Price")
    q = pd.DataFrame(arun)
    q1 = px.pie(q, names=0, values=1)
    st.plotly_chart(q1)
    with st.expander(z):
        st.code(
            """
SELECT a.city, b.sale_price AS SP,
    CASE
        WHEN b.sale_price > 300 THEN 'high'
        WHEN b.sale_price < 300 THEN 'low'
        ELSE 'NAN'
    END AS Sale_Category
FROM table_1 AS a
JOIN table_2 AS b
ON  a.order_id= b.order_id
             limit 50; 
             """
        )
