def write_to_excel(writer, sheet, df):
    df.to_excel(writer, sheet_name=sheet, index=False)