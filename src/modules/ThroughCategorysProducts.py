from src.modules.Category import Category


class ThroughCategorysProducts:
    def __init__(self, category: Category):
        self.products = category.get_products()
        self.stop = len(self.products)

    def __iter__(self):
        self.curr_val = -1
        return self

    def __next__(self):
        if self.curr_val + 1 < self.stop:
            self.curr_val += 1
            return self.products[self.curr_val]
        else:
            raise StopIteration
