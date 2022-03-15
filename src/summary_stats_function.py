import pandas as pd
import numpy as np


#' Calculate summary statistics
#'
#' Creates a new data frame with with the same columns as input and 4 rows, 
#' listing the mean for each column present in the input data frame,
#' the standard deviation,
#' the minimum value for each column
#' and the maximum value for each column.
#'
#' @param data_frame A data frame with number values
#'
#' @return A data frame with four rows. 
#'   The first row (named mean) lists the mean of each column from the input data frame.
#'   The second row (named std) lists the standard deviation of each column from the input data frame.
#'   It will have the same number of columns as the columns present in input data frame.
#'
#' @export
#'
#' @examples
#' get_summary_stats(train_df)

def get_summary_stats(df):
    # returns a data frame with with the same columns as input,
    # and 4 rows: mean, std, min and max


    try:
        if not isinstance(df, pd.DataFrame):
            raise AttributeError("Invalid input: Not a DataFrame")
    except Exception as err:
        print("Something has gone wrong", err)
        return err
    
    if df.empty:
        print('DataFrame is empty!')
        return pd.DataFrame()

    new_df = pd.DataFrame(index=['mean','std','min','max'])

    for column in data_frame:
        new_df[column] = pd.Series([data_frame[column].mean(),data_frame[column].std(),data_frame[column].min(),data_frame[column].max()])

    return new_df