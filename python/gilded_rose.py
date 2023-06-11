# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def change_quality_counter(self, item, amount):
        item.quality += amount
        item.quality = max(0, min(50, item.quality))

    def update_aged_brie(self, item):
        self.change_quality_counter(item, 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            self.change_quality_counter(item, 1)

    def update_backstage_passes(self, item):
        self.change_quality_counter(item, 1)
        if item.sell_in < 11:
            self.change_quality_counter(item, 1)
        if item.sell_in < 6:
            self.change_quality_counter(item, 1)

        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0

    def update_sulfuras(self, item):
        self.change_quality_counter(item, -1)
        item.sell_in -= 1
        if item.sell_in < 0:
            self.change_quality_counter(item, -1)

    def update_quality(self):
        for item in self.items:
            self.update_item_quality(item)

    def update_item_quality(self, item):
        if item.name == "Aged Brie":
            self.update_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_passes(item)
        elif item.name != "Sulfuras, Hand of Ragnaros":
            self.update_sulfuras(item)



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

