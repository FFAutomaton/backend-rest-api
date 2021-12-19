from pydantic import BaseModel
import datetime
from dataclasses import dataclass, asdict
from typing import List, Optional, Set

#	thamin_schema = {
# 			"ds": '2021-12-16',
# 			"tahmin": 4678.76,
# 			"close": 3567
# 			}


@dataclass
class ProphetDataDto:
    ds: str = None
    tahmin: float = None
    close: float = None

    def __init__(self, response):
        self.ds = response['ds']
        self.tahmin = response['tahmin']
        self.close = response['close']