from dataclass_csv import DataclassWriter
import threading
from stock import Stock, StockData

tickers="ABX.TO AEM.TO AQN.TO ATD.TO BAM-A.TO BCE.TO BHC.TO BIP-UN.TO BMO.TO BNS.TO CAE.TO CAR-UN.TO CCL-B.TO CCO.TO CM.TO CNQ.TO CNR.TO CP.TO CSU.TO CTC-A.TO CVE.TO DOL.TO EMA.TO ENB.TO FM.TO FNV.TO FSV.TO FTS.TO GIB-A.TO GIL.TO H.TO IFC.TO IMO.TO K.TO L.TO MFC.TO MG.TO MRU.TO NA.TO NTR.TO OTEX.TO POW.TO PPL.TO QSR.TO RCI-B.TO RY.TO SAP.TO SHOP.TO SJR-B.TO SLF.TO SNC.TO SU.TO T.TO TD.TO TECK-B.TO TRI.TO TRP.TO WCN.TO WN.TO WPM.TO".split()
#tickers="ABX.TO AEM.TO".split()
def refreshData():
    stocks = list(map(Stock, tickers))
    threads = []
    for s in stocks:
        t = threading.Thread(target=s.load)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    with open("stockdata.csv", "w", newline='') as f:
        data = list(map(lambda x: x.getStockData(), stocks))
        w = DataclassWriter(f, data, StockData)
        w.write()

if __name__ == '__main__':
    refreshData()

