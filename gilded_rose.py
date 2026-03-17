# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_price(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.price > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.price = item.price - 1
            else:
                if item.price < 50:
                    item.price = item.price + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.price < 50:
                                item.price = item.price + 1
                        if item.sell_in < 6:
                            if item.price < 50:
                                item.price = item.price + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.price > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.price = item.price - 1
                    else:
                        item.price = item.price - item.price
                else:
                    if item.price < 50:
                        item.price = item.price + 1


class Item:
    def __init__(self, name, sell_in, price):
        self.name = name
        self.sell_in = sell_in
        self.price = price

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.price)
