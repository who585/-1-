# TODO Найдите количество книг, которое можно разместить на дискете
disk = 1.44 * 1024 * 1024
stranitsi = 100
stroki = 50
simvoli = 25
odin = 4
count = int(disk / (odin * simvoli * stroki * stranitsi))

print("Количество книг, помещающихся на дискету:", count)
