class ProductOfNumbers:
    # # ------------- Ituition O(K) ------------
    # def __init__(self):
    #     self.addList = []

    # def add(self, num: int) -> None:
    #     self.addList.append(num)

    # def getProduct(self, k: int) -> int:
    #     n = len(self.addList)
    #     k_numbers = self.addList[n - k :]
    #     res = 1
    #     for num in k_numbers:
    #         res *= num
    #     return res


    # --------------- Prefix O(1) --------------
    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        product = self.prefix[-1] // self.prefix[- k - 1]
        return product


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)