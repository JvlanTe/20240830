import sqlite3

conn = sqlite3.connect("pokemon.db")

c = conn.cursor()

type1_input = input("検索したタイプ1を入力してください:")
type2_input = input("検索したいタイプ2を入力してください:")

# 最後のかっこのなかのカンマが大事らしい（変数が1個だった場合)
c.execute("SELECT name, hp FROM pokemon WHERE type1 = ? AND type2 = ?", (type1_input, type2_input))

# 全データをrowsに入れてる（？）
rows = c.fetchall()

if rows:
    for row in rows:
        print(f"名前:{row[0]},HP:{row[1]}")

else:
    print(f"タイプ1が{type1_input}、タイプ2が{type2_input}のポケモンは見つかりませんでした。")

conn.close()
