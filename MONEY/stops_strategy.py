
class STOPS_STRATEGYY():
    def __init__(self, strategy_number) -> None:
        self.strategy_number = strategy_number  
        self.t_p = None
        self.s_l = None
        self.tralling_s_l = None
        self.counter = 1
        self.tralling_flag = False
        self.checkpoint = False

    def stop_logic(self, last_position, enter_price, current_close, atr):
        self.t_p = 0.0015
        self.s_l = 0.001
        # self.t_p = 0.015
        # self.s_l = 0.007
        if self.strategy_number == 1:
            if last_position == "buy":                
                if current_close >= enter_price + enter_price*self.t_p:
                    return True
                if current_close <= enter_price - enter_price*self.s_l:
                    return True
            if last_position == "sell":                
                if current_close <= enter_price - enter_price*self.t_p:
                    return True
                if current_close >= enter_price + enter_price*self.s_l:
                    return True

            return False       
        
        elif self.strategy_number == 2:   
            # print('jdjdjh')   

            # self.s_l = 0.01  
            self.s_l = 0.001                 
            if last_position == "buy": 
                self.checkpoint = enter_price*(1 + self.counter/100)
                self.tralling_s_l = enter_price + ((self.checkpoint - enter_price)/2)
                if current_close > enter_price:
                    if current_close >= self.checkpoint:
                        self.tralling_flag = True
                        self.counter += 1
                        if self.counter == 2:
                            self.counter = 0
                            # print('realy i am here')
                            self.tralling_flag = False
                            return True                    
                    if (current_close <= self.tralling_s_l) and self.tralling_flag:
                        self.counter = 0
                        # print('hi2')
                        self.tralling_flag = False
                        return True
                    # if current_close < self.checkpoint:
                    #     self.counter = 0
                    #     self.tralling_flag = False
                    #     return True
                # elif current_close < enter_price and self.tralling_flag:
                #     self.counter = 0
                #     self.tralling_flag = False
                #     return True
                elif current_close < enter_price:
                    if current_close <= enter_price - atr*self.s_l:
                        # print('hi3')
                        self.counter = 0
                        self.tralling_flag = False
                        return True
            if last_position == "sell": 
                self.checkpoint = enter_price*(1 - self.counter/100)
                self.tralling_s_l = enter_price - ((enter_price - self.checkpoint)/2)
                if current_close < enter_price:
                    if current_close <= self.checkpoint:
                        self.tralling_flag = True
                        self.counter += 1
                        if self.counter == 2:
                            self.counter = 0
                            # print('realy i am here')
                            self.tralling_flag = False
                            return True                    
                    if (current_close >= self.tralling_s_l) and self.tralling_flag:
                        self.counter = 0
                        self.tralling_flag = False
                        return True
                    # if current_close > self.checkpoint:
                    #     self.counter = 0
                    #     self.tralling_flag = False
                    #     return True

                elif current_close > enter_price:                        
                    if current_close >= enter_price + atr*self.s_l:
                        # print('hi3')
                        self.counter = 0
                        self.tralling_flag = False
                        return True
            return False
        elif self.strategy_number == 3:
            self.t_p = 0.015
            self.s_l = 0.007
            self.t_p = 0.0015
            self.s_l = 0.001
            # print(current_close, enter_price, atr, enter_price + atr*self.t_p, enter_price + atr*(1+ self.t_p))

            if last_position == "buy":                
                if current_close >= enter_price + atr*self.t_p:
               
                    # print('sdhfb')
                    return True
                if current_close <= enter_price - atr*self.s_l:
               
                    # print('sdhfb')
                    return True
            if last_position == "sell":                
                if current_close <= enter_price - atr*self.t_p:
               
                    # print('sdhfb')
                    return True
                if current_close >= enter_price + atr*self.s_l:
               
                
                    # print('sdhfb')
                    return True

            return False  
