from dataclasses import dataclass
from dacite import from_dict
from typing import Optional
import yfinance as yf

@dataclass
class StockData:
    symbol: str
    longName: str
    sector: str
    dividendYield: Optional[float]
    dividendRate:  Optional[float]
    currentPrice: float
    fiftyTwoWeekLow: float
    marketCap: float
    payoutRatio: Optional[float]
    beta: Optional[float]

class Stock:
    def __init__(self, symbol):
        self._symbol=symbol

    def load(self):
        print(f'{self._symbol} loading')
        info = yf.Ticker(self._symbol).info
        print(f'{self._symbol} loaded')
        self._stockData = from_dict(data_class=StockData, data=info)

    def getStockData(self):
        return self._stockData




