products = {
    "リンゴ":19,
    "バナナ":18,
    "オレンジ":45,
    "トマト":20,
    "マンゴ":50,
    "さくらんぼ":100,
    "水":5,
    "ソーセージ":24,
    "ドラゴンフルーツ":35
}

products_index = [
    "リンゴ",
    "バナナ",
    "オレンジ",
    "トマト",
    "マンゴ",
    "さくらんぼ",
    "水",
    "ソーセージ",
    "ドラゴンフルーツ",
]

cart = 0
cart_products = {}
print("業務スーパーへようこそ")
print("本日の商品")
for i in products:
    print(f"{i}:{products[i]}円 ")
print()

while True:
    print("\n1.商品選択　 2.お会計")
    try:
        menu = int(input("何番をしますか？: "))
    except ValueError:
        print("⚠ 数字を入力してください。")
        continue  # 再度ループへ戻る

    if menu == 1:
        print("お好きな商品の番号を選んでください")
        for count, item in enumerate(products_index, 1):
            print(f"{count}. {item}")

        try:
            index = int(input("商品の番号を入力してください: "))
            if not (1 <= index <= len(products_index)):
                print("⚠ 無効な番号です。1〜9の間で入力してください。")
                continue

            quantity = int(input("何個を買いますか？: "))
            if quantity <= 0:
                print("⚠ 1以上の数を入力してください。")
                continue

        except ValueError:
            print("⚠ 数字を入力してください。")
            continue

        # カートに商品を追加
        product_name = products_index[index - 1]
        if product_name in cart_products:
            cart_products[product_name] += quantity
        else:

            cart_products[product_name] = quantity

        cart += products[product_name] * quantity
        print(f"✅ {product_name}を{quantity}個カートに追加しました。")

    elif menu == 2:
        if not cart_products:
            print("🛒 カートが空です。商品を選択してください。")
            continue

        print(f"\nお会計は {cart} 円です")
        print("商品詳細：")
        for item in cart_products:
            total_price = products[item] * cart_products[item]
            print(f"{item} - 数量: {cart_products[item]}, 合計: {total_price}円")
        print("\n🧾 ご利用ありがとうございました！")
        break

    else:
        print("⚠ 1 または 2 を入力してください。")



    




    
