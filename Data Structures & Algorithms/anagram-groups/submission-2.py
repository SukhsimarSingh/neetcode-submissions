from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                # ord function gives ASCII value for a character, eg ord(a) - 97, so for character b it would be 98, and for c 99 and so on
                # Hence, if we subtract any character by the a's ASCII value we would get a value from 0 to 25 which is exactly the numbers in count
                # therefore we would update the index using this for the count list which is having 26 placeholder values basically add 1 over there
                # and increase the count everytime we get the same value, thus creating a unique key for each word
                index_sub = ord(c) - ord('a')
                count[index_sub] +=1

                # Avoiding this code entirely using default_dict
                # if tuple(count) in str_dict:
                #     str_dict[tuple(count)].append(s)
                # else:
                #     str_dict[tuple(count)] = s
                
            key = tuple(count)
            str_dict[key].append(s)

        return list(str_dict.values())