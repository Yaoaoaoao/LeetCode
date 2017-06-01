class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # fastest
        common = set(list1).intersection(set(list2))
        if len(common) == 1:
            return list(common)
        common_index_sum, common_restaurant = 1e9, []
        for c in common:
            ai, bi = list1.index(c), list2.index(c)
            sumi = ai + bi
            if common_index_sum == sumi:
                common_restaurant.append(c)
            elif sumi < common_index_sum:
                common_index_sum = sumi
                common_restaurant = [c]
        return common_restaurant
        
        # O(a) + O(b)
        common_index_sum, common_restaurant = 1e9, []
        # No duplicates in both lists.
        aIndex = {a: i for i, a in enumerate(list1)} 
        for bi, b in enumerate(list2):
            if b in list1:
                ai = aIndex[b]  # O(1)
                sumi = ai + bi
                if common_index_sum == sumi:
                    common_restaurant.append(b)
                elif sumi < common_index_sum:
                    common_index_sum = sumi
                    common_restaurant = [b]
        return common_restaurant
        
        # O(a*b)
        common_index_sum, common_restaurant = 1e9, []
        for bi, b in enumerate(list2):
            if b in list1:
                ai = list1.index(b)  # O(n)
                sumi = ai + bi
                if common_index_sum == sumi:
                    common_restaurant.append(b)
                elif sumi < common_index_sum:
                    common_index_sum = sumi
                    common_restaurant = [b]
        return common_restaurant


print Solution().findRestaurant(
    ["Shogun", "Tapioca Express", "Burger King", "KFC"],
    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse",
     "Shogun"])

print Solution().findRestaurant(["k","KFC"], ["k","KFC"])
