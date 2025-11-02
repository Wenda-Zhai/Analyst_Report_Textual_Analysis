import os
from pathlib import Path

path = Path(__file__).parent
os.chdir(path)
input_file = "report_conclusions_raw.csv"   # 你的原始文件
lines_per_file = None

# 先统计总行数
with open(input_file, "r", encoding="utf-8") as f:
    header = next(f)  # 读取表头
    total_lines = sum(1 for _ in f)

# 平均分配到 5 个文件
n=6
lines_per_file = total_lines // n

with open(input_file, "r", encoding="utf-8") as f:
    header = next(f)  # 重新读表头
    file_idx = 1
    out_file = open(f"part_{file_idx}.csv", "w", encoding="utf-8")
    out_file.write(header)

    for i, line in enumerate(f, start=1):
        out_file.write(line)
        if i % lines_per_file == 0 and file_idx < n:
            out_file.close()
            file_idx += 1
            out_file = open(f"part_{file_idx}.csv", "w", encoding="utf-8")
            out_file.write(header)

    out_file.close()
