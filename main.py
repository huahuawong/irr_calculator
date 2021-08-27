import pandas as pd
import streamlit as st
import sklearn
from scipy.stats import pearsonr
import time
import numpy as np


st.title("Inter-rater Reliability Calculator")
st.text("Measuring inter-rater reliability")
st.sidebar.header("About")
st.sidebar.text("""The IRR calculator uses scikit-learn 
and scipy module to implement 
different methods to calculate 
IRR. This tool can calculate 
IRR using Cohen's Kappa, Percent 
Agreement and Pearson's correlation. 
To get your IRR score, upload 
a csv file with columns and 
specify your raters in 
the fields below.
""")


df = st.file_uploader("Choose a file")
# df = pd.read_csv("test.csv")


def highlight_max(s, props=''):
    return np.where(s == np.nanmax(s.values), props, '')


if df:
    df = pd.read_csv(df)

    col1, col2 = st.columns(2)

    with col1:
        st.dataframe(df.style.apply(highlight_max, props='color:white;background-color:darkblue', axis=0))
        # st.dataframe(df.style.highlight_max(color= '',axis=0))  # Same as st.write(df)

    with col2:
        st.line_chart(df)
        person1 = st.sidebar.text_input("Enter column name for person 1")
        person2 = st.sidebar.text_input("Enter column name for person 2")

        if st.sidebar.button("Calculate Cohen's Kappa"):
            with st.spinner('Wait for it...'):
                time.sleep(0.1)
            st.success('Done!')

            y1 = df[person1]
            y2 = df[person2]
            kap = sklearn.metrics.cohen_kappa_score(y1, y2, labels=None, weights=None, sample_weight=None)
            st.sidebar.write('Result: %s' % round(kap, 3))

        if st.sidebar.button("Calculate Percent Agreement"):
            with st.spinner('Wait for it...'):
                time.sleep(0.1)
            st.success('Done!')
            y1 = df[person1]
            y2 = df[person2]

            total = len(y1)
            count_match = 0
            for i in range(0, len(y1)):
                if y1[i] == y2[i]:
                    count_match += 1
            if count_match == 0:
                agreement = 0
            else:
                agreement = round(count_match / total, 3)
            st.sidebar.write('Result: %s' % agreement)

        if st.sidebar.button("Calculate Pearson's Correlation"):
            with st.spinner('Wait for it...'):
                time.sleep(0.1)
            st.success('Done!')

            y1 = df[person1]
            y2 = df[person2]

            corr, _ = pearsonr(y1, y2)
            corr = round(corr, 3)
            st.sidebar.write('Result: %s' % corr)
