import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 1141722952 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    stat, pval = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='larger')
    alpha = 0.07
    if (pval<alpha): 
        return True 
    else: 
        return False
