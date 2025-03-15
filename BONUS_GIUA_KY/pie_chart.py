import pandas as pd
import plotly.express as px

# Đọc file Excel
file_path = "dataset-406H.xlsx"
xls = pd.ExcelFile(file_path)
df = pd.read_excel(xls, sheet_name="Sheet1")

df.columns = df.columns.str.strip()
df_cleaned = df.dropna(subset=["Mã HP"])
df_cleaned["Học Kỳ Gốc"] = df_cleaned["Học Kỳ"]
total_credits_per_semester = df_cleaned.groupby("Học Kỳ Gốc")["Số Tín Chỉ"].sum().reset_index()
df_cleaned = df_cleaned.merge(total_credits_per_semester, on="Học Kỳ Gốc", suffixes=("", "_tổng"))
df_cleaned["Học Kỳ"] = "Học kỳ " + df_cleaned["Học Kỳ Gốc"].astype(str) + " (" + df_cleaned["Số Tín Chỉ_tổng"].astype(str) + " tín chỉ)"


fig = px.sunburst(df_cleaned,
                  path=["Học Kỳ", "Loại môn học", "Tên học phần"],
                  values="Số Tín Chỉ",
                  title="Phân bổ chương trình đào tạo của 406H")

output_html_path = "pie_chart_406H.html"
fig.write_html(output_html_path)

