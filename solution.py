import pandas as pd
import numpy as np


chat_id = 391223586 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    p = (x_success + y_success) / (x_cnt + y_cnt)
    n1 = x_cnt
    n2 = y_cnt
    
    z = abs((p1 - p2) / math.sqrt(p * (1 - p) * (1/n1 + 1/n2)))
    
    return z > 2.58
