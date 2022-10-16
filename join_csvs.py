import pandas as pd
import warnings
warnings.filterwarnings("ignore")


def check_same_columns(files_name: list) -> None:

    list_columns = []

    for file in files_name:

        df = pd.read_csv(file, delimiter=';', encoding='latin-1', skiprows=[0])

        list_columns.append(df.columns.to_list())

    print("There are probably the same columns!") if pd.DataFrame(list_columns).duplicated().sum(
    ) + 1 == len(list_columns) else print("There's a problem here. Please check them one by one.")


def join_cvs(files_name: list) -> pd.DataFrame:

    df_general = pd.DataFrame()
    shapes = []

    for file in files_name:

        df = pd.read_csv(file, delimiter=';', encoding='latin-1', skiprows=[0])
        df['csv'] = file.split("_")[-1].replace(".csv", "")

        shapes.append(df.shape[0])
        df_general = df_general.append(df, ignore_index=True)

    return df_general if sum(shapes) == df_general.shape[0] else print("There's problem with csv join: the final df isn't same size as the originals.")


def main():

    files = ['./data/despesa_ceaps_2022.csv', './data/despesa_ceaps_2019.csv', './data/despesa_ceaps_2018.csv', './data/despesa_ceaps_2017.csv', './data/despesa_ceaps_2016.csv',
             './data/despesa_ceaps_2015.csv', './data/despesa_ceaps_2014.csv', './data/despesa_ceaps_2013.csv', './data/despesa_ceaps_2012.csv', './data/despesa_ceaps_2012.csv',
             './data/despesa_ceaps_2010.csv', './data/despesa_ceaps_2009.csv', './data/despesa_ceaps_2008.csv']

    check_same_columns(files)

    df = join_cvs(files)

    df.to_csv("./data/ceaps_2008_to_2022.csv", index=False)


if __name__ == "__main__":
    main()
