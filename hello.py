"""第一个 Python 脚本：门店欢迎板。

运行方式：python hello.py
"""

from datetime import date

BRANDS = {
    "姜胖胖自助烤肉": 2,
    "霸王茶姬": 5,
    "塔斯汀": 3,
}


def main() -> None:
    today = date.today().strftime("%Y年%m月%d日")
    total = sum(BRANDS.values())

    print("=" * 38)
    print(f"  {today}  门店早报")
    print("=" * 38)
    for brand, count in BRANDS.items():
        print(f"  {brand:<12} {count} 家")
    print("-" * 38)
    print(f"  合计 {total} 家门店，开工！")
    print("=" * 38)


if __name__ == "__main__":
    main()
