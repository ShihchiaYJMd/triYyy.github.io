"""把中文字体裁剪成只含页面用到的汉字，输出 woff2 到 assets/fonts/。

页面文案改动后重新跑一遍：
    python3 tools/subset-fonts.py <字体目录>

字体目录里放原始 ttf（不入库），文件名对应关系见 FONTS。
跑完后把 styles.css 里字体 url 的 ?v= 和 html 里 styles.css?v= 一起加一，避免浏览器用旧缓存。
"""

import sys
from pathlib import Path

from fontTools import subset

ROOT = Path(__file__).resolve().parent.parent
PAGES = ["index.html", "404.html"]
OUT = ROOT / "assets" / "fonts"

# 原始文件名 -> 输出文件名
FONTS = {
    "LXGWWenKai-Regular.ttf": "wenkai-regular.woff2",  # 正文楷体（OFL）
    "LXGWWenKai-Medium.ttf": "wenkai-medium.woff2",
    "FZSuSXSJF.TTF": "sushi-xingshu.woff2",  # 方正苏轼行书：首屏台词、竖排题字
    "FZYanZQKSJF.TTF": "yan-kaishu.woff2",  # 方正颜真卿楷书：标题、印章
}

# 中文标点里落在拉丁区段的几个符号，也交给楷体
EXTRA = "·—‘’“”…"


def is_cjk(ch: str) -> bool:
    cp = ord(ch)
    return (
        0x2E80 <= cp <= 0x9FFF  # 部首、标点、假名、汉字
        or 0xF900 <= cp <= 0xFAFF  # 兼容汉字
        or 0xFF00 <= cp <= 0xFFEF  # 全角标点
    )


def collect_text() -> str:
    text = "".join((ROOT / p).read_text(encoding="utf-8") for p in PAGES)
    chars = {c for c in text if is_cjk(c)} | set(EXTRA)
    return "".join(sorted(chars))


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    src_dir = Path(sys.argv[1])
    text = collect_text()
    OUT.mkdir(parents=True, exist_ok=True)

    for src_name, out_name in FONTS.items():
        src = src_dir / src_name
        if not src.exists():
            print(f"跳过（未找到）：{src}")
            continue
        opts = subset.Options()
        opts.flavor = "woff2"
        opts.layout_features = ["*"]
        opts.name_IDs = ["*"]
        font = subset.load_font(str(src), opts)
        sub = subset.Subsetter(opts)
        sub.populate(text=text)
        sub.subset(font)
        subset.save_font(font, str(OUT / out_name), opts)
        size = (OUT / out_name).stat().st_size // 1024
        print(f"{out_name}: {len(text)} 字, {size} KB")


if __name__ == "__main__":
    main()
