from dataclasses import dataclass
from dacite import from_dict
from typing import Optional
import yfinance as yf
from dataclass_csv import DataclassWriter

@dataclass
class Stock:
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


def getStockData(s: str):
    print(f'{s} loading')
    t = yf.Ticker(s).info
    print(f'{s} loaded')
    return from_dict(data_class=Stock, data=t)

tickers="ABX.TO AEM.TO AQN.TO ATD.TO BAM-A.TO BCE.TO BHC.TO BIP-UN.TO BMO.TO BNS.TO CAE.TO CAR-UN.TO CCL-B.TO CCO.TO CM.TO CNQ.TO CNR.TO CP.TO CSU.TO CTC-A.TO CVE.TO DOL.TO EMA.TO ENB.TO FM.TO FNV.TO FSV.TO FTS.TO GIB-A.TO GIL.TO H.TO IFC.TO IMO.TO K.TO L.TO MFC.TO MG.TO MRU.TO NA.TO NTR.TO OTEX.TO POW.TO PPL.TO QSR.TO RCI-B.TO RY.TO SAP.TO SHOP.TO SJR-B.TO SLF.TO SNC.TO SU.TO T.TO TD.TO TECK-B.TO TRI.TO TRP.TO WCN.TO WN.TO WPM.TO".split()
#tickers="ABX.TO AEM.TO".split()
#print(yf.Ticker("ABX.TO").info)
data = []
for t in tickers:
    d = getStockData(t)
    data.append(d)

print(data)
with open("stockdata.csv", "w", newline='') as f:
   w = DataclassWriter(f, data, Stock)
   w.write()

#a = [(k,v) for k, v in d.items() if k in['symbol', 'longName','dividendYield','dividendRate','currentPrice','fiftyTwoWeekLow','marketCap']]
#print (a)
#symbols = tickers = yf.Ticker("ABX.TO AEM.TO AQN.TO ATD.TO BAM-A.TO BCE.TO BHC.TO BIP-UN.TO BMO.TO BNS.TO CAE.TO CAR-UN.TO CCL-B.TO CCO.TO CM.TO CNQ.TO CNR.TO CP.TO CSU.TO CTC-A.TO CVE.TO DOL.TO EMA.TO ENB.TO FM.TO FNV.TO FSV.TO FTS.TO GIB-A.TO GIL.TO H.TO IFC.TO IMO.TO K.TO L.TO MFC.TO MG.TO MRU.TO NA.TO NTR.TO OTEX.TO POW.TO PPL.TO QSR.TO RCI-B.TO RY.TO SAP.TO SHOP.TO SJR-B.TO SLF.TO SNC.TO SU.TO T.TO TD.TO TECK-B.TO TRI.TO TRP.TO WCN.TO WN.TO WPM.TO", session=session)



