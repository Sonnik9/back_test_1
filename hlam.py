# from UTILS import indicatorss

# def bunch_handler_func(next_data, close_price, b_bband_q, s_bband_q, b_rsi_lev, s_rsi_lev, b_macd__q, s_macd_q, b_stoch_q, s_stoch_q, current_bunch):

#     signals_sum = []
#     buy_signals_counter = 0
#     sell_signals_counter = 0
#     buy_total_signal, sell_total_signal = False, False

#     if 'bband_flag' in current_bunch:
#         next_data = indicatorss.calculate_bollinger_bands(next_data)
#         upper, lower = next_data['Upper'][-1], next_data['Lower'][-1]
#         buy_bband_signal = close_price >= lower * b_bband_q
#         sell_bband_signal = close_price <= upper * s_bband_q
#         signals_sum.append((buy_bband_signal, sell_bband_signal))

#     if 'macd_strong_flag' in current_bunch:
#         next_data = indicatorss.calculate_macd(next_data)
#         macd, signal = next_data['MACD'][-1], next_data['Signal'][-1]
#         buy_strong_macd_signal = (macd > signal * b_macd__q) & (macd < 0)
#         sell_strong_macd_signal = (macd < signal * s_macd_q) & (macd > 0)
#         signals_sum.append((buy_strong_macd_signal, sell_strong_macd_signal))

#     if 'macd_lite_flag' in current_bunch:
#         next_data = indicatorss.calculate_macd(next_data)
#         macd, signal = next_data['MACD'][-1], next_data['Signal'][-1]
#         buy_lite_macd_signal = macd > signal * b_macd__q
#         sell_lite_macd_signal = macd < signal * s_macd_q
#         signals_sum.append((buy_lite_macd_signal, sell_lite_macd_signal))

#     if 'rsi_flag' in current_bunch:
#         next_data = indicatorss.calculate_rsi(next_data)
#         rsi = next_data['RSI'][-1]
#         buy_rsi_signal = rsi <= b_rsi_lev
#         sell_rsi_signal = rsi >= s_rsi_lev
#         signals_sum.append((buy_rsi_signal, sell_rsi_signal))

#     if 'stoch_flag' in current_bunch:
#         next_data = indicatorss.calculate_stochastic_oscillator(next_data)
#         fastk, slowk = next_data['SlowK'][-1], next_data['SlowD'][-1]
#         buy_stoch_signal = (fastk > slowk) & (fastk < b_stoch_q)
#         sell_stoch_signal = (fastk < slowk) & (fastk > s_stoch_q)
#         signals_sum.append((buy_stoch_signal, sell_stoch_signal))

#     if 'engulfing_flag' in current_bunch:
#         next_data = indicatorss.calculate_engulfing_patterns(next_data)
#         engulfing = next_data['Engulfing'][-1]
#         buy_engulfing_signal = engulfing > 0
#         sell_engulfing_signal = engulfing < 0
#         signals_sum.append((buy_engulfing_signal, sell_engulfing_signal))

#     if 'doji_flag' in current_bunch:
#         next_data = indicatorss.calculate_doji(next_data)
#         doji = next_data['Doji'][-1]
#         buy_doji_signal = doji != 0
#         sell_doji_signal = doji != 0
#         signals_sum.append((buy_doji_signal, sell_doji_signal))

#     for buy_signal, sell_signal in signals_sum:
#         if buy_signal:
#             buy_signals_counter += 1
#         if sell_signal:
#             sell_signals_counter += 1

#     if 'U' in current_bunch:
#         if buy_signals_counter == len(signals_sum):
#             buy_total_signal = True 
#     if 'D':
#         if sell_signals_counter == len(signals_sum):
#             sell_total_signal = True
#     if 'F' in current_bunch:
#         if buy_signals_counter == len(signals_sum):
#             buy_total_signal = True 
#         if sell_signals_counter == len(signals_sum):
#             sell_total_signal = True

#     return buy_total_signal, sell_total_signal


# def trends_defender(next_data):

#     try:
#         next_data = indicatorss.calculate_adx(next_data)
#         next_data = indicatorss.calculate_sma(next_data)
#     except Exception as ex:
#         print(ex)

#     if next_data['Close'][-1] > next_data['SMA'][-1] and next_data['ADX'][-1] > 25:
#         return "U"
#     elif next_data['Close'][-1] < next_data['SMA'][-1] and next_data['ADX'][-1] > 25:
#         return "D"
#     else:
#         return "F"

# def signal_gen(next_data, strategy_name, bunch_variant, l_s_strtg, close_price, b_bband_q, s_bband_q, b_rsi_lev, s_rsi_lev, b_macd__q, s_macd_q, b_stoch_q, s_stoch_q):
        
#         buy_signal, sell_signal = False, False 

#         if strategy_name == 'advanced_static':
#             trende_sign = trends_defender(next_data)
                     
#             if trende_sign == 'U':
#                 current_bunch = ['bband_flag', 'macd_lite_flag', 'engulfing_flag', 'U']
#             if trende_sign == 'D':
#                 current_bunch = ['bband_flag', 'macd_lite_flag', 'engulfing_flag', 'D']
                
#             if trende_sign == 'F':
#                 if bunch_variant == 1:            
#                     current_bunch = ['bband_flag', 'macd_lite_flag', 'doji_flag', 'F']
#                 if bunch_variant == 2:
#                     current_bunch = ['macd_lite_flag', 'stoch_flag', 'F']

#         # if strategy_name == 'advanced_dinamic':
#         #     current_bunch = best_advanced_bunch[bunch_variant-1]

#         buy_signal, sell_signal = bunch_handler_func(next_data, close_price, b_bband_q, s_bband_q, b_rsi_lev, s_rsi_lev, b_macd__q, s_macd_q, b_stoch_q, s_stoch_q, current_bunch)
 
#         # if l_s_strtg == 'long_short':
#         #     pass
#         # elif l_s_strtg == 'long':
#         #     sell_signal = False
#         # elif l_s_strtg == 'short':
#         #     buy_signal = False
#         # print(buy_signal, sell_signal)     
#         return buy_signal, sell_signal




        # self.sma = bt.talib.SMA(self.data, period=20)
        # print(self.sma)

        # # Создаем индикаторы Bollinger Bands
        # self.bollinger = bt.indicators.BollingerBands(
        #     self.data.close, period=self.boll_params[0][1], devfactor=self.boll_params[1][1]
        # )
        # me1 = EMA(self.data, period=12)
        # print(me1)
        # me2 = EMA(self.data, period=26)
        # self.l.macd = me1 - me2
        # self.l.signal = EMA(self.l.macd, period=9)

    # params_stopps = (
    #     ("take_profit_percent", 0.03),  # Уровень тейк-профита в процентах
    #     ("stop_loss_percent", 0.02),    # Уровень стоп-лосса в процентах
    # )
    # lines = ('macd', 'signal')
    # params = (('period_me1', 12), ('period_me2', 26), ('period_signal', 9),)
    # boll_params = (("bollinger_period", 20), ("bollinger_devfactor", 2.0),)




# from __future__ import (absolute_import, division, print_function,
#                         unicode_literals)

# import argparse
# import datetime

# import backtrader as bt


# class TALibStrategy(bt.Strategy):
#     params = (('ind', 'sma'), ('doji', True),)

#     INDS = ['sma', 'ema', 'stoc', 'rsi', 'macd', 'bollinger', 'aroon',
#             'ultimate', 'trix', 'kama', 'adxr', 'dema', 'ppo', 'tema',
#             'roc', 'williamsr']

#     def __init__(self):
#         if self.p.doji:
#             bt.talib.CDLDOJI(self.data.open, self.data.high,
#                              self.data.low, self.data.close)

#         if self.p.ind == 'sma':
#             bt.talib.SMA(self.data.close, timeperiod=25, plotname='TA_SMA')
#             bt.indicators.SMA(self.data, period=25)
#         elif self.p.ind == 'ema':
#             bt.talib.EMA(timeperiod=25, plotname='TA_SMA')
#             bt.indicators.EMA(period=25)
#         elif self.p.ind == 'stoc':
#             bt.talib.STOCH(self.data.high, self.data.low, self.data.close,
#                            fastk_period=14, slowk_period=3, slowd_period=3,
#                            plotname='TA_STOCH')

#             bt.indicators.Stochastic(self.data)

#         elif self.p.ind == 'macd':
#             bt.talib.MACD(self.data, plotname='TA_MACD')
#             bt.indicators.MACD(self.data)
#             bt.indicators.MACDHisto(self.data)
#         elif self.p.ind == 'bollinger':
#             bt.talib.BBANDS(self.data, timeperiod=25,
#                             plotname='TA_BBANDS')
#             bt.indicators.BollingerBands(self.data, period=25)

#         elif self.p.ind == 'rsi':
#             bt.talib.RSI(self.data, plotname='TA_RSI')
#             bt.indicators.RSI(self.data)

#         elif self.p.ind == 'aroon':
#             bt.talib.AROON(self.data.high, self.data.low, plotname='TA_AROON')
#             bt.indicators.AroonIndicator(self.data)

#         elif self.p.ind == 'ultimate':
#             bt.talib.ULTOSC(self.data.high, self.data.low, self.data.close,
#                             plotname='TA_ULTOSC')
#             bt.indicators.UltimateOscillator(self.data)

#         elif self.p.ind == 'trix':
#             bt.talib.TRIX(self.data, timeperiod=25,  plotname='TA_TRIX')
#             bt.indicators.Trix(self.data, period=25)

#         elif self.p.ind == 'adxr':
#             bt.talib.ADXR(self.data.high, self.data.low, self.data.close,
#                           plotname='TA_ADXR')
#             bt.indicators.ADXR(self.data)

#         elif self.p.ind == 'kama':
#             bt.talib.KAMA(self.data, timeperiod=25, plotname='TA_KAMA')
#             bt.indicators.KAMA(self.data, period=25)

#         elif self.p.ind == 'dema':
#             bt.talib.DEMA(self.data, timeperiod=25, plotname='TA_DEMA')
#             bt.indicators.DEMA(self.data, period=25)

#         elif self.p.ind == 'ppo':
#             bt.talib.PPO(self.data, plotname='TA_PPO')
#             bt.indicators.PPO(self.data, _movav=bt.indicators.SMA)

#         elif self.p.ind == 'tema':
#             bt.talib.TEMA(self.data, timeperiod=25, plotname='TA_TEMA')
#             bt.indicators.TEMA(self.data, period=25)

#         elif self.p.ind == 'roc':
#             bt.talib.ROC(self.data, timeperiod=12, plotname='TA_ROC')
#             bt.talib.ROCP(self.data, timeperiod=12, plotname='TA_ROCP')
#             bt.talib.ROCR(self.data, timeperiod=12, plotname='TA_ROCR')
#             bt.talib.ROCR100(self.data, timeperiod=12, plotname='TA_ROCR100')
#             bt.indicators.ROC(self.data, period=12)
#             bt.indicators.Momentum(self.data, period=12)
#             bt.indicators.MomentumOscillator(self.data, period=12)

#         elif self.p.ind == 'williamsr':
#             bt.talib.WILLR(self.data.high, self.data.low, self.data.close,
#                            plotname='TA_WILLR')
#             bt.indicators.WilliamsR(self.data)


# def runstrat(args=None):
#     args = parse_args(args)

#     cerebro = bt.Cerebro()

#     dkwargs = dict()
#     if args.fromdate:
#         fromdate = datetime.datetime.strptime(args.fromdate, '%Y-%m-%d')
#         dkwargs['fromdate'] = fromdate

#     if args.todate:
#         todate = datetime.datetime.strptime(args.todate, '%Y-%m-%d')
#         dkwargs['todate'] = todate

#     data0 = bt.feeds.YahooFinanceCSVData(dataname=args.data0, **dkwargs)
#     cerebro.adddata(data0)

#     cerebro.addstrategy(TALibStrategy, ind=args.ind, doji=not args.no_doji)

#     cerebro.run(runcone=not args.use_next, stdstats=False)
#     if args.plot:
#         pkwargs = dict(style='candle')
#         if args.plot is not True:  # evals to True but is not True
#             npkwargs = eval('dict(' + args.plot + ')')  # args were passed
#             pkwargs.update(npkwargs)

#         cerebro.plot(**pkwargs)


# def parse_args(pargs=None):

#     parser = argparse.ArgumentParser(
#         formatter_class=argparse.ArgumentDefaultsHelpFormatter,
#         description='Sample for sizer')

#     parser.add_argument('--data0', required=False,
#                         default='../../datas/yhoo-1996-2015.txt',
#                         help='Data to be read in')

#     parser.add_argument('--fromdate', required=False,
#                         default='2005-01-01',
#                         help='Starting date in YYYY-MM-DD format')

#     parser.add_argument('--todate', required=False,
#                         default='2006-12-31',
#                         help='Ending date in YYYY-MM-DD format')

#     parser.add_argument('--ind', required=False, action='store',
#                         default=TALibStrategy.INDS[0],
#                         choices=TALibStrategy.INDS,
#                         help=('Which indicator pair to show together'))

#     parser.add_argument('--no-doji', required=False, action='store_true',
#                         help=('Remove Doji CandleStick pattern checker'))

#     parser.add_argument('--use-next', required=False, action='store_true',
#                         help=('Use next (step by step) '
#                               'instead of once (batch)'))

#     # Plot options
#     parser.add_argument('--plot', '-p', nargs='?', required=False,
#                         metavar='kwargs', const=True,
#                         help=('Plot the read data applying any kwargs passed\n'
#                               '\n'
#                               'For example (escape the quotes if needed):\n'
#                               '\n'
#                               '  --plot style="candle" (to plot candles)\n'))

#     if pargs is not None:
#         return parser.parse_args(pargs)

#     return parser.parse_args()


# if __name__ == '__main__':
#     runstrat()


# import talib
# # import talib.abstract as ta

# def calculate_bollinger_bands(data, period=20, num_std=2):
#     # middle_band = talib.SMA(data['Close'], timeperiod=period)
#     data['Upper'], _, data['Lower'] = talib.BBANDS(data['Close'], timeperiod=period, nbdevup=num_std, nbdevdn=num_std)    
#     # next_data['SMA'] = next_data.Close.rolling(window=period).mean()
#     # next_data['stddev'] = next_data.Close.rolling(window=period).std()
#     # next_data['Upper'] = next_data.SMA + 2* next_data.stddev
#     # next_data['Lower'] = next_data.SMA - 2* next_data.stddev
#     return data

# def calculate_sma(data, period=20):
#     print(data)
#     num_std = 2
#     try:
#     #    data['SMA'] = data.Close.rolling(window=period).mean()
#         # data['SMA'] = talib.SMA(data['Close'], timeperiod=period)
#         _, data['SMA'], _ = talib.BBANDS(data['Close'], timeperiod=period, nbdevup=num_std, nbdevdn=num_std) 
#     except Exception as ex:
#         print(ex)
#     return data

# def calculate_rsi(data, period=14):
#     # data['RSI'] = talib.RSI(data['Close'], timeperiod=period)
#     # data['RSI'].fillna(data['RSI'].mean(), inplace=True)
#     data['RSI'] = talib.RSI(data['Close'], timeperiod=period)
#     data['RSI'].interpolate(method='linear', inplace=True)
#     return data

# def calculate_macd(data, fast_period=12, slow_period=26, signal_period=9):
#     data['MACD'], data['Signal'], _ = talib.MACD(data['Close'], fastperiod=fast_period, slowperiod=slow_period, signalperiod=signal_period)
#     return data

# def calculate_atr(data, period=14):
#     data['ATR'] = talib.ATR(data['High'], data['Low'], data['Close'], timeperiod=period)    
#     return data

# def calculate_adx(data, period=14):
#     print(data)
#     data.loc[:, 'ADX'] = talib.ADX(data['High'], data['Low'], data['Close'], timeperiod=period)

#     return data

# def calculate_engulfing_patterns(data):
#     data['Engulfing'] = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])
#     return data

# def calculate_doji(data):
#     data['Doji'] = talib.CDLDOJI(data['Open'], data['High'], data['Low'], data['Close'])
#     return data 

# def calculate_stochastic_oscillator(data, k_period=14, d_period=3):
#     data['SlowK'], data['SlowD'] = talib.STOCH(data['High'], data['Low'], data['Close'], fastk_period=k_period, slowk_period=k_period, slowd_period=d_period)
#     # data['SlowK'], data['SlowD'] = talib.STOCH(data['High'], data['Low'], data['Close'], 5, 3, 3, 0, 0)
#     return data

