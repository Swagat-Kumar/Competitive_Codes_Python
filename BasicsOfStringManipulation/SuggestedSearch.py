class Solution:
    def suggestedProducts(self, products, searchWord: str):
        products.sort()
        aux = list(products)
        ans = []
        for i in range(len(searchWord)):
            temp = []
            for a in aux:
                if len(a) <= i:
                    continue
                if a[i] == searchWord[i]:
                    temp.append(a)
            ans.append(temp[:3])
            aux = temp
        return ans
