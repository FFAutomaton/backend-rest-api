import pandas as pd
from dtos.exchange_input_dto import CandleStickGraph

def dto_to_df(canldestickgraph):
    temp = CandleStickGraph.to_dict(canldestickgraph)
    df = pd.DataFrame()
    df = df.append(temp, ignore_index=True)

    return df
