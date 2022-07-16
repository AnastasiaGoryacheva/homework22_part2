Я изучила работу https://github.com/Novvval/HW_21.3/blob/master/app.py
Я обнаружила следующие запахи плохого кода:

app.py строчки 40 и 66
повторяющиеся функции
было:
@property
    def items(self):
        return self._items

@property
    def get_items(self):
        return self._items

исправлено: (требуется удалить первую функцию def items)
@property
def get_items(self):
    return self._items


app.py строчка 96
непонятное название функции, что она делает
было: def main()
исправила: def goods_delivery()


app.py строчка 147
непонятное название функции, что она делает
было: def display_contents()
исправила: def get_stored_goods()


app.py строчка 74
магическое число 5 в классе Shop никак не обозначено
было:
class Shop(Store):
    def __init__(self):
        super().__init__()
        self._capacity = 20

исправлено: (добавлена функиция с пояснением числа 5)
def add(self, product, amount):
        if (self.get_free_space - amount) >= 0 and self.get_unique_items_count < 5:
            self.capacity -= amount
            if product in self.items:
                self.get_items[product] += amount
            else:
                self.get_items[product] = amount
        else:
            print(f"Не хватает места! Попробуй еще раз!")


app.py строчка 164
вылетает ошибка из за русского языка, если ставить место откуда забирают товар,
то по условиям кода надо писать "из магазин", вместо "из магазина" (ошибка русского языка)
два варианта пути: исправить "магазин" на "магазина", либо в условии поставить пункт прибытия товара
было:
def determine_places(request):
    # переопределение названий в запросе на объекты
    if request.from_ == "склад":
        request.from_ = store
        request.to = shop
    elif request.from_ == "магазин":
        request.from_ = shop
        request.to = store
    return request.to, request.from_
исправлено:
def determine_places(request):
    # переопределение названий в запросе на объекты
    if request.to == "склад":
        request.to = store
        request.from = shop
    elif request.to == "магазин":
        request.to = shop
        request.from = store
    return request.to, request.from


app.py
не работает вариант доставки товара из магазина на склад
было:
отсутствие словаря с товаарами в магазина в размере не более 20 штук
исправлено:
(добавлена таблица продуктов в магазин в ограниченным количеством до 20 штук)
shop.items = {
    "огурцы": 2,
    "помидоры": 4,
    "бананы": 6,
    "вода": 3
}
