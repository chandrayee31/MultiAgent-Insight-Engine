import pandas as pd
def analysis_agent(df:pd.DataFrame)->dict:
    monthly_sales=df.groupby('month')['sales'].sum()
    category_sales=df.groupby('category')['sales'].sum()
    lowest_sales_month=monthly_sales.idxmin()
    highest_sales_month=monthly_sales.idxmax(

    )
    return {
        "monthly_sales": monthly_sales.to_dict(),
        "category_sales": category_sales.to_dict(),
        "lowest_sales_month": lowest_sales_month,
        "highest_sales_month": highest_sales_month
    }