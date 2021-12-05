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

    def __init__(self, tempdata):
        self.open_time = datetime.datetime.utcfromtimestamp(tempdata[0] / 1000)
        self.open = tempdata[1]
        self.high = tempdata[2]
        self.low = tempdata[3]
        self.close = tempdata[4]
        self.volume = tempdata[5]

@dataclass
class CandleStickGraph:
    candlesticks: Optional[List[CandleStickDto]]
    # def __init__(self, candlesticks):
    #     self.candlesticks = candlesticks