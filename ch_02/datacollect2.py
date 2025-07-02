from pathlib import Path
import pandas as pd
from folder import in_dir,out_dir

out_2_2=out_dir/f"{Path(__file__).stem}.xlsx"

if __name__ =="__main__":
    result=[]
    for xlsx_path in Path(in_dir).glob("2024년*월.xlsx"):
        df_raw=pd.read_excel(xlsx_path,sheet_name="Sheet1",usecols="B:E",skiprows=2)
        result.append(df_raw)

    df_concat=pd.concat(result)
    df_concat.to_excel(out_2_2,index=False)