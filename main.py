import backtrader as bt
import yfinance as yf
import pandas as pd
from datetime import datetime
import sign_handler

data_global = None

class MyStrategy(bt.Strategy):
    global data_global

    def __init__(self):

        self.start_index = 0  
        self.dataa = data_global
        self.signal = None
        self.last_position = None
        self.enter_price = None
        self.t_p = 0.03
        self.s_l = 0.02

    def stop_logic(self, last_position, enter_price, current_hight, current_low):
        stop_defender = False
        if last_position:
            if last_position == "buy":
                if enter_price + enter_price*self.t_p <= current_hight:
                    stop_defender = True
                elif enter_price - enter_price*self.s_l >= current_low:
                    stop_defender = True
            if last_position == "sell":
                if enter_price - enter_price*self.t_p >= current_low:
                    stop_defender = True
                elif enter_price + enter_price*self.s_l <= current_hight:
                    stop_defender = True

        return stop_defender

      


    def next(self):        
        next_data = self.dataa.iloc[:self.start_index+25]     
        # print(next_data)  
        
        if not next_data.empty:  
            stop_defender = False          
            current_close = next_data['Close'].iloc[-1]
            current_hight = next_data['High'].iloc[-1]
            current_low = next_data['Low'].iloc[-1]
            self.signal = sign_handler.signal_gen(next_data, current_close)
            
        
            if self.signal == "buy" and not self.position:
                
                position_size = 10
                self.buy(size=position_size)
                self.last_position = "buy"
                self.enter_price = current_close

            elif self.signal == "sell" and not self.position:
                
                position_size = 10
                self.sell(size=position_size)
                self.last_position = "sell"
                self.enter_price = current_close

            elif self.signal == "neutral" and self.position:
                stop_defender = self.stop_logic(self.last_position, self.enter_price, current_hight, current_low)
                if stop_defender:
                    # print('hi')
                    self.close()                
        
        self.start_index += 1

def main():
    global data_global 

    symbol = 'MSFT'
    # symbol = 'AAPL'
    symbol = 'BTC'
    start_date = '2010-01-01'
    end_date = '2023-08-31'
    data_global = yf.download(symbol, start=start_date, end=end_date)
    # print(data_global)
    # return

    cerebro = bt.Cerebro()
    cerebro.addstrategy(MyStrategy)

    fake_data = bt.feeds.PandasData(
        dataname=data_global,
        fromdate=datetime(2010, 1, 1),
        todate=datetime(2023, 8, 31),
    )

    cerebro.adddata(fake_data)

    # Начальный капитал портфеля
    cerebro.broker.set_cash(1000)

    # Добавляем схему комиссий (пример)
    cerebro.broker.setcommission(commission=0.001)

    print(f'Starting Portfolio Value: {cerebro.broker.getvalue():.2f}')
    cerebro.run()
    print(f'Final Portfolio Value: {cerebro.broker.getvalue():.2f}')
    # Завершение программы
    cerebro.broker.stop()

if __name__ == "__main__":
    main()
