#!/usr/bin/env python
"""
Guillotine Style 2D Bin Algorithm

Solomon Bothwell
ssbothwell@gmail.com
"""
from functools import reduce
from collections import namedtuple
from item import Item


FreeRectangle = namedtuple('FreeRectangle', ['width', 'height', 'x', 'y'])


class Guillotine:
    def __init__(self, x: int = 8, y: int = 4) -> None:
        self.x = x
        self.y = y
        self.freerects = [FreeRectangle(self.x, self.y, 0, 0)] # type: List[tuple]
        self.items = [] # type: List[Item]


    def __repr__(self) -> None:
        return "Guillotine(%r)" % (self.items)


    def first_fit(self, item: Item) -> bool:
        fitted_rects = [rect for rect in self.freerects if rect.width >= item.x and rect.height >= item.y]
        for freerect in fitted_rects:
            item.CornerPoint = (freerect.x, freerect.y)
            self.items.append(item)
            self.freerects.remove(freerect)
            if item.x < freerect.width:
                # generate free rectangle for remaining width
                right_width = freerect.width - item.x
                right_height = item.y
                right_x = freerect.x + item.x
                right_y = freerect.y
                right_rect = FreeRectangle(right_width,
                                           right_height,
                                           right_x,
                                           right_y)
                self.freerects.append(right_rect)
            if item.y < freerect.height:
                top_width = freerect.width
                top_height = freerect.height - item.y
                top_x = freerect.x
                top_y = item.y
                top_rect = FreeRectangle(top_width,
                                         top_height,
                                         top_x,
                                         top_y)
                self.freerects.append(top_rect)
            return True
        return False


    def best_width_fit(self, item) -> bool:
        fitted_rects = [rect for rect in self.freerects if rect.width >= item.x and rect.height >= item.y]
        best = reduce(lambda a, b: a if (a.width < b.width) else b, fitted_rects)

        if best:
            item.CornerPoint = (best.x, best.y)
            self.items.append(item)
            self.freerects.remove(best)
            if item.x < best.width:
                # generate free rectangle for remaining width
                right_width = best.width - item.x
                right_height = item.y
                right_x = best.x + item.x
                right_y = best.y
                right_rect = FreeRectangle(right_width,
                                           right_height,
                                           right_x,
                                           right_y)
                self.freerects.append(right_rect)
            if item.y < best.height:
                top_width = best.width
                top_height = best.height - item.y
                top_x = best.x
                top_y = item.y
                top_rect = FreeRectangle(top_width,
                                         top_height,
                                         top_x,
                                         top_y)
                self.freerects.append(top_rect)
            return True
        return False


    def best_height_fit(self, item) -> bool:
        fitted_rects = [rect for rect in self.freerects if rect.width >= item.x and rect.height >= item.y]
        best = reduce(lambda a, b: a if (a.height < b.height) else b, fitted_rects)

        if best:
            item.CornerPoint = (freerect.x, freerect.y)
            self.items.append(item)
            self.freerects.remove(best)
            if item.x < best .width:
                # generate free rectangle for remaining width
                right_width = best .width - item.x
                right_height = item.y
                right_x = best .x + item.x
                right_y = best .y
                right_rect = FreeRectangle(right_width,
                                           right_height,
                                           right_x,
                                           right_y)
                self.freerects.append(right_rect)
            if item.y < best .height:
                top_width = best .width
                top_height = best .height - item.y
                top_x = best .x
                top_y = item.y
                top_rect = FreeRectangle(top_width,
                                         top_height,
                                         top_x,
                                         top_y)
                self.freerects.append(top_rect)
            return True
        return False


    def best_area_fit(self, item) -> bool:
        fitted_rects = [rect for rect in self.freerects if rect.width >= item.x and rect.height >= item.y]
        best = reduce(lambda a, b: a if ((a.width*a.height) < (b.width*b.height)) else b, fitted_rects)

        if best:
            item.CornerPoint = (best.x, best.y)
            self.items.append(item)
            self.freerects.remove(best)
            if item.x < best.width:
                # generate free rectangle for remaining width
                right_width = best.width - item.x
                right_height = item.y
                right_x = best.x + item.x
                right_y = best.y
                right_rect = FreeRectangle(right_width,
                                           right_height,
                                           right_x,
                                           right_y)
                self.freerects.append(right_rect)
            if item.y < best.height:
                top_width = best.width
                top_height = best.height - item.y
                top_x = best.x
                top_y = item.y
                top_rect = FreeRectangle(top_width,
                                         top_height,
                                         top_x,
                                         top_y)
                self.freerects.append(top_rect)
            return True
        return False


    def worst_width_fit(self, item) -> bool:
        fitted_rects = [rect for rect in self.freerects if rect.width >= item.x and rect.height >= item.y]
        best = reduce(lambda a, b: a if (a.width > b.width) else b, fitted_rects)

        if best:
            item.CornerPoint = (best.x, best.y)
            self.items.append(item)
            self.freerects.remove(best)
            if item.x < best.width:
                # generate free rectangle for remaining width
                right_width = best.width - item.x
                right_height = item.y
                right_x = best.x + item.x
                right_y = best.y
                right_rect = FreeRectangle(right_width,
                                           right_height,
                                           right_x,
                                           right_y)
                self.freerects.append(right_rect)
            if item.y < best.height:
                top_width = best.width
                top_height = best.height - item.y
                top_x = best.x
                top_y = item.y
                top_rect = FreeRectangle(top_width,
                                         top_height,
                                         top_x,
                                         top_y)
                self.freerects.append(top_rect)
            return True
        return False


    def worst_height_fit(self, item) -> bool:
        fitted_rects = [rect for rect in self.freerects if rect.width >= item.x and rect.height >= item.y]
        best = reduce(lambda a, b: a if (a.height > b.height) else b, fitted_rects)

        if best:
            item.CornerPoint = (best.x, best.y)
            self.items.append(item)
            self.freerects.remove(best)
            if item.x < best.width:
                # generate free rectangle for remaining width
                right_width = best.width - item.x
                right_height = item.y
                right_x = best.x + item.x
                right_y = best.y
                right_rect = FreeRectangle(right_width,
                                           right_height,
                                           right_x,
                                           right_y)
                self.freerects.append(right_rect)
            if item.y < best.height:
                top_width = best.width
                top_height = best.height - item.y
                top_x = best.x
                top_y = item.y
                top_rect = FreeRectangle(top_width,
                                         top_height,
                                         top_x,
                                         top_y)
                self.freerects.append(top_rect)
            return True
        return False


    def worst_area_fit(self, item) -> bool:
        fitted_rects = [rect for rect in self.freerects if rect.width >= item.x and rect.height >= item.y]
        best = reduce(lambda a, b: a if ((a.height*a.width) > (b.height*b.width)) else b, fitted_rects)

        if best:
            item.CornerPoint = (best.x, best.y)
            self.items.append(item)
            self.freerects.remove(best)
            if item.x < best.width:
                # generate free rectangle for remaining width
                right_width = best.width - item.x
                right_height = item.y
                right_x = best.x + item.x
                right_y = best.y
                right_rect = FreeRectangle(right_width,
                                           right_height,
                                           right_x,
                                           right_y)
                self.freerects.append(right_rect)
            if item.y < best.height:
                top_width = best.width
                top_height = best.height - item.y
                top_x = best.x
                top_y = item.y
                top_rect = FreeRectangle(top_width,
                                         top_height,
                                         top_x,
                                         top_y)
                self.freerects.append(top_rect)
            return True
        return False


    def insert(self, item: Item, heuristic: str = 'best_area_fit') -> bool:
        heuristics = {'first_fit': self.first_fit,
                      'best_width_fit': self.best_width_fit,
                      'best_height_fit': self.best_height_fit,
                      'best_area_fit': self.best_area_fit,
                      'worst_width_fit': self.worst_width_fit,
                      'worst_height_fit': self.worst_width_fit,
                      'worst_area_fit': self.worst_width_fit}

        if heuristic in heuristics:
            # Call Heuristic
            res = heuristics[heuristic](item)
            # If item inserted successfully
            if res:
                return True
        return False


    def bin_stats(self) -> dict:
        """
        Returns a dictionary with compiled stats on the bin tree
        """

        stats = {
            'width': self.x,
            'height': self.y,
            'area': self.x * self.y,
            'efficiency': 1-(sum([F.width*F.height for F in self.freerects])/(self.x*self.y)),
            'items': self.items,
            }

        return stats

if __name__ == '__main__':
    G = Guillotine(8, 4)
    I = Item(2,5)
    I2 = Item(2,4)
    I3 = Item(2,2)
    G.insert(I)
    G.insert(I2)
    G.insert(I3)
    print(G.items)
    print(G.freerects)
    print(G.bin_stats())
