class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}

        # strs = ["eat","tea","tan","ate","nat","bat"]

        for s in strs:
            # eat -> aet
            # tea -> aet
            # tan -> ant
            # ate -> aet
            # nat -> ant
            # bat -> abt
            sorted_string = "".join(sorted(s))

            if sorted_string in str_dict:
                # {aet: [eat, tea, ate]}
                str_dict[sorted_string].append(s)                
            else:
                str_dict[sorted_string] = [s]

        return list(str_dict.values())