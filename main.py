import backtrader as bt
import yfinance as yf
import pandas as pd
from datetime import datetime
import sign_handler
from random import choice
from MONEY.stops_strategy import STOPS_STRATEGYY
from UTILS.indicatorss import calculate_atr

data_global = None
stop_strategy_global = None

class MyStrategy(bt.Strategy):
    global data_global
    global stop_strategy_global
    params = (
        ("stop_loss", 2),      # Уровень стоп-лосса в абсолютных единицах
        ("take_profit", 3),   # Уровень тейк-профита в абсолютных единицах
    )

    def __init__(self):

        self.start_index = 0  
        self.dataa = data_global
        self.signal = None
        self.last_position = None
        self.enter_price = None
        
        self.stop_strategyI = STOPS_STRATEGYY(stop_strategy_global)
       
        self.order_counter = 0
        self.stop_counter = 0
        self.close_counter = 0
        self.id_list = []
        self.last_id = None
        self.close_id_list = []
        self.pos = False
        self.atr = None

    def next(self):        
        next_data = self.dataa.iloc[self.start_index:self.start_index+50]     
        # print(next_data) 
        position_size = 10 
        
        if not next_data.empty:  
            if stop_strategy_global != 1:
                self.atr = calculate_atr(next_data)
            stop_defender = False          
            current_close = next_data['Close'].iloc[-1]
            # current_hight = next_data['High'].iloc[-1]
            # current_low = next_data['Low'].iloc[-1]
            self.signal = sign_handler.signal_gen(next_data, current_close)            
        
            if self.signal == "buy" and not self.pos:               
                self.buy(size=position_size)
                self.pos = True                
                self.last_position = "buy"
                self.enter_price = current_close
                self.order_counter +=1
                self.id_list.append(self.start_index)
                self.last_id = self.start_index

            elif self.signal == "sell" and not self.pos:               
                self.sell(size=position_size)
                self.pos = True                
                self.last_position = "sell"
                self.enter_price = current_close
                self.order_counter +=1
                self.id_list.append(self.start_index)
                self.last_id = self.start_index

            if self.pos:
                self.stop_counter += 1
                stop_defender = self.stop_strategyI.stop_logic(self.last_position, self.enter_price, current_close, self.atr)
                if stop_defender:
                    # print('hi')
                    self.close()  
                    self.pos = False
                    self.close_id_list.append(self.last_id)
                    self.close_counter +=1
            # n = len(self.id_list) - len(self.close_id_list)
            # if n > 1:
            #     for _ in range(n):
            #         self.close()  
            # if (n !=0) and (self.start_index == len(data_global)-1):
            #     for _ in range(n):
            #         self.close()             
        
        self.start_index += 1
        if self.start_index == len(data_global):
            print(f"order_counter:__ {self.order_counter}")
            # print(self.stop_counter)
            print(f"close_counter:__ {self.close_counter}")
            # print(f"id_list:__ {self.id_list}")
            # print(f"len_id_list:__ {len(self.id_list)}")
            # print(f"close_id_list:__ {self.close_id_list}")
            # print(f"len_close_id_list:__ {len(self.close_id_list)}")

def main():
    global data_global 
    global stop_strategy_global
    total_profit = 0

    range_profit_list = []
    symbol_list = ['BTC-USD', 'ETH-USD', 'XRP-USD', 'LTC-USD', 'BCH-USD', 'EOS-USD', 'XMR-USD', 'ADA-USD', 'IOTA-USD', 'NEO-USD']
    try:
        stop_strategy_global = int(input('Please, choice stop_strategy (1,2,3,4)',))
    except:
        stop_strategy_global = 3
    for i, symbol in enumerate(symbol_list):
        # symbol = symbol_list[int(input('Please, choice a ticker (1,2,3) ',))-1]
        # symbol = 'AAPL'
        # symbol = 'BTC'
        start_date = '2017-01-01'
        end_date = '2023-08-20'
        try:
            data_global = yf.download(symbol, start=start_date, end=end_date)
        except:
            continue

        cerebro = bt.Cerebro()
        cerebro.addstrategy(MyStrategy)

        fake_data = bt.feeds.PandasData(
            dataname=data_global,
            fromdate=datetime(2017, 1, 1),
            todate=datetime(2023, 8, 20),
        )

        cerebro.adddata(fake_data)

        # Начальный капитал портфеля
        cerebro.broker.set_cash(1000)

        # Добавляем схему комиссий (пример)
        cerebro.broker.setcommission(commission=0.001)

        print(f'Starting Portfolio Value: {cerebro.broker.getvalue():.2f}')
        cerebro.run()
        # print(f'Final Portfolio Value: {cerebro.broker.getvalue():.2f}')
        range_profit_list.append((i, symbol, cerebro.broker.getvalue()-1000))
        # Завершение программы
        cerebro.broker.stop()
    range_profit_list = sorted(range_profit_list, key= lambda x: x[2], reverse=True)
    total_profit = sum([x[2] for x in range_profit_list])
    print(range_profit_list)
    print(total_profit)

if __name__ == "__main__":
    main()


# [*********************100%%**********************]  1 of 1 completed
# Starting Portfolio Value: 1000.00
# order_counter:__ 74
# close_counter:__ 67
# id_list:__ [149, 172, 188, 194, 213, 319, 355, 393, 399, 407, 439, 570, 582, 603, 619, 695, 700, 975, 1036, 1040, 1043, 1053, 1066, 1071, 1171, 1199, 1209, 1234, 1237, 1266, 1287, 1304, 1323, 1334, 1578, 1597, 1629, 1641, 1674, 1705, 1798, 1804, 1871, 1873, 1919, 1942, 1967, 1980, 1986, 1992, 2086, 2162, 2168, 2242, 2313, 2382, 2434, 2491, 2525, 2560, 2656, 2661, 2748, 2749, 2750, 2768, 2789, 2811, 2826, 2861, 2863, 2870, 2885, 2894]
# len_id_list:__ 74
# close_id_list:__ [149, 172, 188, 194, 213, 319, 355, 393, 399, 407, 439, 570, 582, 603, 619, 695, 700, 975, 1036, 1040, 1043, 1053, 1066, 1071, 1171, 1199, 1209, 1234, 1237, 1266, 1287, 1304, 1323, 1334, 1578, 1597, 1629, 1641, 1674, 1705, 1798, 1804, 1871, 1873, 1919, 1942, 1967, 1980, 1986, 1992, 2086, 2162, 2168, 2242, 2382, 2434, 2491, 2525, 2560, 2656, 2661, 2789, 2811, 2826, 2863, 2885, 2894]
# len_close_id_list:__ 67
# Final Portfolio Value: 863.17