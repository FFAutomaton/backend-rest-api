from pydantic import BaseModel
import datetime
from dataclasses import dataclass, asdict
from typing import List, Optional, Set


@dataclass
class CandleStickDto:
    open_time: datetime.date = None
    open: float = None
    high: float = None
    low: float = None
    close: float = None
    volume: float = None

    def __init__(self, temp_data):
        self.open_time = datetime.datetime.utcfromtimestamp(temp_data[0] / 1000)
        self.open = temp_data[1]
        self.high = temp_data[2]
        self.low = temp_data[3]
        self.close = temp_data[4]
        self.volume = temp_data[5]

@dataclass
class CandleStickGraph:
    candlesticks: Optional[List[CandleStickDto]]

    def __init__(self, data):
        i = 0
        temp_list = []
        while i < len(data):
            temp_list.append(CandleStickDto(data[i]))
            i = i + 1
        self.candlesticks = temp_list
