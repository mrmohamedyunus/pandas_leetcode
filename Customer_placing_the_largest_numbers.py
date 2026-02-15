import pandas as pd
def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    result=(
        orders.groupby('customer_number').size().reset_index(name='order_count')
    )
    max_orders=result['order_count'].max()
    return result[result['order_count']==max_orders][['customer_number']]
    