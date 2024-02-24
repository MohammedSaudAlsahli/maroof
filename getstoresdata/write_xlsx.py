import pandas as pd
from sotres import Store
from config import HEADERS, PARAMS, BASE_URL


def xlsx(end_count, start_count = 0) -> None:
    store_data = Store(url=BASE_URL, headers=HEADERS, params=PARAMS, end_count=end_count, start_count=start_count)
    data_dict_list = [data.model_dump() for data in store_data.store_data()]
    df = pd.DataFrame(data_dict_list)
    df.to_excel('output.xlsx', index=False)