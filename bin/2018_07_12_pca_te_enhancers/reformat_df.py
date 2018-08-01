# Name: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Functions used to reformat pandas dataframes.

def normalize(df, lengths_col, normalize_cols):
    """
    Normalize all counts within columns normalize_cols of dataframe df by the
    lengths of strings within column lengths_col. All numbers are converted
    to floating point.

    Keyword Arguments:
        df: Pandas data frame to normalize

        lengths_col: Integer column number within the features matrix containing
            strings whose length serve as the divisors for other columns.
            Strings of length 0 will cause that column to contain inf values.

        normalize_cols: List of integers containing column numbers of columns
            whose values are the dividends to be divided by the lengths in
            lengths_col. Any NaNs divided with remain NaN.
    """
    # Create column to store all the lengths in the lengths column
    df["lengths"] = df.iloc[:, lengths_col].str.len()

    # Normalize counts by dividing by length of elements in
    df.iloc[:, normalize_cols] = (df.iloc[:, normalize_cols].div(
                                    df.loc[:, "lengths"], axis="index")
                                    .astype(float))

    # Drop the created column
    df.drop(["lengths"], axis="columns", inplace=True)