import sys

import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.errors import UndefinedVariableError

from main.data_mining.a_return_csv_data import return_pd_df_from_all_files, TimeFrameAndModelEnum
from main.model.all_moto_atv_models import reduced_moto_atv_brand_model_dict

sns.set_theme(style='darkgrid')
sns.set(rc={'axes.facecolor': 'cornflowerblue'})

all_moto_list = return_pd_df_from_all_files(TimeFrameAndModelEnum.TODAY)


def show_plot(x_prec_int, y_prec_int, title):
    ax = plt.gca()
    ax.set_title(title)
    ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(int(f'{x_prec_int}')))
    ax.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(int(f'{y_prec_int}')))
    plt.ginput(20)
    plt.show()


def show_most_popular():
    moto_count = all_moto_list.groupby(['Model', 'Year', 'Price']).size().reset_index(name="Location")
    model_count = moto_count.Model.value_counts().iloc[:20]

    print(f'model count= \n {model_count}')
    sns.countplot(
        data=moto_count,
        y='Model',
        hue='Model',
        palette='Greens_d',
        order=moto_count.Model.value_counts().iloc[:20].index
    )
    plt.show()


def show_most_popular_by_year():
    moto_count = all_moto_list.groupby(['Year', 'Price', 'Model'])
    print(moto_count.size())

    sns.catplot(
        data=all_moto_list
        .sort_values('Model')
        .groupby("Model").filter(lambda x: len(x) > 30),
        x='Year',
        y='Model',
        kind='box'
    )
    plt.show()


def show_most_popular_by_price():
    sns.catplot(
        data=all_moto_list
        .sort_values('Model')
        .groupby("Model")
        .filter(lambda x: len(x) > 30),
        x='Model',
        y='Price',
        kind='boxen'
    )
    plt.show()


def show_most_popular_by_price_and_year():
    sns.relplot(
        data=all_moto_list
        .sort_values('Model')
        .groupby('Model')
        .filter(lambda x: len(x) > 30),
        x='Price',
        y='Year',
        col='Model',
        col_wrap=5,
        dashes=False,
        markers=True
    )
    plt.show()


def show_price_estimation(query_model):
    pd.set_option('display.max_rows', None)
    try:
        # moto_count = all_moto_list.groupby(['Model', 'Year', 'Price']).size().reset_index(name="Location")
        # model_count = moto_count.Model.value_counts().iloc[:20]

        printing = all_moto_list \
            .query(f'Model =="{query_model}"') \
            .groupby(['Price', 'Year', 'Location', 'Link']) \
            .size()

        print(printing)
        # print(type(printing))
        if len(printing) > 0:
            sns.lmplot(
                data=all_moto_list.query(f'Model == "{query_model}"'),
                x='Price',
                y='Year',
                x_estimator=np.mean,
                ci=None,
                lowess=False,
                scatter_kws={'s': 80}
            )

            show_plot(x_prec_int=500, y_prec_int=1, title=query_model)
    except (UndefinedVariableError, ValueError):
        tb = sys.exc_info()[0]
        print(f"Show price estimation TraceBack {tb}")


if __name__ == '__main__':
    for brand in reduced_moto_atv_brand_model_dict:
        for model in reduced_moto_atv_brand_model_dict.get(brand):
            print(f'Model: {model}')
            show_price_estimation(model)

        # show_most_popular()
        # show_most_popular_by_year()
        # show_most_popular_by_price()
        # show_most_popular_by_price_and_year()
        # show_price_estimation('crf')
