import pickle
import streamlit as st
import pandas as pd
import numpy as np
import math
from sklearn.preprocessing     import StandardScaler, RobustScaler, MinMaxScaler
from lightgbm import LGBMClassifier

#load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# defining the prediction function
def predict(ReleaseYear, CastNum, DurMin, DurHour, WeekYe, WeekYeSin, WeekYeCos, MonYe, MonYeSin, 
            MonYeCos, DayWeek, DayWeekSin, DayWeekCos, AddedYe, CateNum, CountriesNum, 
            DayMon, DayMonSin, DayMonCos, DiffYe):
    
    # -------------------------------------MAKING PREDICTION----------------------------------
    
    # making the prediction
    yhat = model.predict([[ReleaseYear, CastNum, DurMin, DurHour, WeekYe, WeekYeSin, WeekYeCos, MonYe, MonYeSin, 
            MonYeCos, DayWeek, DayWeekSin, DayWeekCos, AddedYe, CateNum, CountriesNum, 
            DayMon, DayMonSin, DayMonCos, DiffYe]])
    
    # giving the answer
    prediction = (yhat)
    
    return prediction
    
def main():
    st.header('Multiclass Classification - Notas de Shows da Netflix')
    st.text("Autor: Valcilio Eugenio - Data Scientist")
    
    # ReleaseYear
    ReleaseYear = st.number_input('Digite o ano de lançamento:', value=0)
    
    # CastNum
    CastNum = st.number_input('Digite o número de pessoas no elenco:', value=0)
    
    # DurMin
    DurMin = st.number_input('Duração do show em minutos (considere 1 season igual a 600 minutos):', value=0)
    
    # DurHour
    if DurMin != 0:
        DurHour = DurMin/60 
    else:
        DurHour = 0
    
    # WeelYe
    WeekYe = st.number_input('Digite qual o número da semana no ano que o show foi adicionado  a Netflix:', value=0)
    
    # MonYe
    MonYe = st.number_input('Digite o mês do ano em numeral que o show foi adicionado a Netflix (1 = Janeiro e assim por diante):', value=0)
    
    # DayWeek
    DayWeek = st.number_input('Digite o número do dia da semana que o show foi adicionado a Netflix (0 = Segunda, ..., 6 = Domingo):', value=0)
    
    # AddedYe
    AddedYe = st.number_input('Digite o ano em que o show foi adicionado a Netflix:', value=0)
    
    # DiffYe
    if AddedYe != 0:
    	DiffYe = ReleaseYear - AddedYe
    else:
    	DiffYe = 0
    
    # CatNum
    CateNum = st.number_input('Digite o número de categorias:', value=0)
    
    # CountriesNum
    CountriesNum = st.number_input('Digite o número de países lançado (considere 1, caso não saiba):', value=0)
    
    # DayMon
    DayMon = st.number_input('Digite o dia do mês (de 1 a 30, considere 30 se for 31):', value=0)
    
    # preparing the dataset
    if DayMon != 0:
    
        # # -------------------------------------RESCALING----------------------------------

        # -------------------------------------STANDARDSCALER----------------------------------

        #ReleaseYear
        ss = pickle.load(open('scalers/release_year_scaler.pkl', 'rb'))
        RY = (ss.transform([[ReleaseYear]]))[0]
        ReleaseYear = RY[0]

        # day_of_month
        ss = pickle.load(open('scalers/day_of_month_scaler.pkl', 'rb'))
        DM = (ss.transform([[DayMon]]))[0]
        DM = DM[0]

        # day_of_week
        ss = pickle.load(open('scalers/day_of_week_scaler.pkl', 'rb'))
        DW = (ss.transform([[DayWeek]]))[0]
        DayWeek = DW[0]

        # added_year
        ss = pickle.load(open('scalers/added_year_scaler.pkl', 'rb'))
        AY = (ss.transform([[AddedYe]]))[0]
        AddedYe = AY[0]

        # month_of_year
        ss = pickle.load(open('scalers/month_of_year_scaler.pkl', 'rb'))
        MY = (ss.transform([[MonYe]]))[0]
        MonYe = MY[0]

        # week_of_year
        ss = pickle.load(open('scalers/week_of_year_scaler.pkl', 'rb'))
        WY = (ss.transform([[WeekYe]]))[0]
        WeekYe = WY[0]

        # -------------------------------------ROBUSTSCALER----------------------------------

        # duration_min
        rs = pickle.load(open('scalers/duration_min_scaler.pkl', 'rb'))
        DM = (rs.transform([[DurMin]]))[0]
        DurMin = DM[0]

        # duration_hour
        rs = pickle.load(open('scalers/duration_hour_scaler.pkl', 'rb'))
        DH = (rs.transform([[DurHour]]))[0]
        DurHour = DH[0]

        # -------------------------------------MINMAXSCALER----------------------------------

        # num_of_cast
        mms = pickle.load(open('scalers/num_of_cast_scaler.pkl', 'rb'))
        CN = (mms.transform([[CastNum]]))[0]
        CastNum = CN[0]

        # num_of_countries
        mms = pickle.load(open('scalers/num_of_countries_scaler.pkl', 'rb'))
        CON = (mms.transform([[CountriesNum]]))[0]
        CountriesNum = CON[0]

        # num_of_categories
        mms = pickle.load(open('scalers/num_of_categories_scaler.pkl', 'rb'))
        CAN = (mms.transform([[CateNum]]))[0]
        CateNum = CAN[0]
        
        # diff_bet_years
        mms = pickle.load(open('scalers/diff_bet_years_scaler.pkl', 'rb'))
        DY = (mms.transform([[DiffYe]]))[0]
        DiffYe = DY[0]

        # -------------------------------------TRANSFORMATION----------------------------------

        # ----------------------------------NATURE TRANSFORMATION----------------------------------

        # day_of_week
        DayWeekSin = np.sin(DayWeek*(2.*np.pi/7))
        DayWeekCos = np.cos(DayWeek*(2.*np.pi/7))

        # day_of_month
        DayMonSin = np.sin(DayMon*(2.*np.pi/30))
        DayMonCos = np.cos(DayMon*(2.*np.pi/30))

        # month_of_year
        MonYeSin = np.sin(MonYe*(2.*np.pi/12))
        MonYeCos = np.cos(MonYe*(2.*np.pi/12))

        # week_of_year
        WeekYeSin = np.sin(WeekYe*(2.*np.pi/52))
        WeekYeCos = np.cos(WeekYe*(2.*np.pi/52))
    
    if st.button('Prediction'):
        
        # fazendo a predição
        result = predict(ReleaseYear, CastNum, DurMin, DurHour, WeekYe, WeekYeSin, WeekYeCos, MonYe, MonYeSin, 
            MonYeCos, DayWeek, DayWeekSin, DayWeekCos, AddedYe, CateNum, CountriesNum, 
            DayMon, DayMonSin, DayMonCos, DiffYe)
        
        # informando os resultados
        st.success('A nota do seu show indicado será {:.0f}.'.format(result[0]))
        
if __name__ == '__main__':
    main()
