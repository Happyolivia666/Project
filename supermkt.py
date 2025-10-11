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
    print("1.商品選択　 ２.お会計")
    menu = int(input("何番をしますか？"))
    if menu == 1:
        print ("お好きな商品の番号を選びでください")
        count = 1
        for i in products:
            
            print(f"{count}.{i}",end="")
            count += 1
        print()
        index = int(input("商品の番号を入力しで下さい"))
        sum = int(input("何個を買いますか？"))
        cart_products[products_index[index-1]] = sum
        cart += products[products_index[index-1]]*sum


    else:
        print(f"お会計は{cart}円")
        print("商品詳細：  ")
        for item  in cart_products:
            print (f"{item},{cart_products[item]}, {products[item]*cart_products[item]}")

        break


    




    
