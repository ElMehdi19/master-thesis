import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


class TriLinearRegression:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe
        self.newtonian_reg = LinearRegression(fit_intercept=False)
        self.bingham_reg = LinearRegression()
        self.casson_reg = LinearRegression()
    
    def fit_newtonian(self):
        self.newtonian_reg.fit(self.df[['ShearRate']], self.df.Stress)
    
    def fit_bingham(self):
        self.bingham_rg.fit(self.df[['ShearRate']], self.df.Stress)

    def fit_casson(self):
        self.casson_reg.fit(self.df[['ShearRate']] ** 0.5, self.df.Stress ** 0.5)
    
    def fit_models(self):
        self.fit_newtonian()
        self.fit_bingham()
        self.fit_casson()
    
    def get_regression_params(self):
        newtonian = { 'a': self.newtonian_reg.coef_[0], 'b': self.newtonian_reg.intercept_ }
        bingham = { 'a': self.bingham_reg.coef_[0], 'b': self.bingham_reg.intercept_ }
        casson = { 'a': self.casson_reg.coef_[0], 'b': self.casson_reg.intercept_ }
        return { 'newtonian': newtonian, 'bingham': bingham, 'casson': casson }

    def print_regression_params(self):
        for (model, params) in self.get_regression_params().items():
            print(f'{model}: a={params.get("a")} | b={params.get("b")}')

if __name__ == '__main__':
    df = pd.read_csv('dataset.csv')
    tri_lin_reg = TriLinearRegression(df.head(13))
    tri_lin_reg.fit_models()
    tri_lin_reg.print_regression_params()
