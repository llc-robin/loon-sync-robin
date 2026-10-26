
from pathlib import Path
import re
import sys

# 处理传入的 LCF 文件
file_path = Path(sys.argv[1])

plugins_to_add = [
    (
        "RealIP-Bypass-Domain.plugin",
        "https://raw.githubusercontent.com/llc-robin/loon-sync-robin/main/RealIP-Bypass-Domain.plugin",
    ),
    (
        "blockAds.plugin",
        "https://cdn.jsdelivr.net/gh/fmz200/wool_scripts@main/Loon/plugin/blockAds.plugin",
    ),
]

content = file_path.read_text(encoding="utf-8-sig")
lines = content.splitlines()

# 定位 [Plugin]
start = next(
    (i for i, line in enumerate(lines)
     if line.strip().lower() == "[plugin]"),
    None,
)

if start is None:
    raise RuntimeError("未找到 [Plugin]，停止修改，避免破坏配置")

# 定位下一个配置段
end = next(
    (i for i in range(start + 1, len(lines))
     if re.match(r"^\s*\[[^\]]+\]\s*$", lines[i])),
    len(lines),
)

section = lines[start + 1:end]
added = 0

for name, url in plugins_to_add:
    # 只在 [Plugin] 中检查，避免重复添加
    if any(name.lower() in line.lower() for line in section):
        print(f"已存在，跳过：{name}")
        continue

    section.append(f"{url}, enabled=true")
    added += 1
    print(f"新增：{name}")

lines[start + 1:end] = section

result = "\n".join(lines)
if content.endswith(("\n", "\r")):
    result += "\n"

file_path.write_text(result, encoding="utf-8")
print(f"处理完成，新增 {added} 条插件")
