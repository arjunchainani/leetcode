import heapq
import copy

class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        results = [0] * len(score)
        # save some runtime by storing all the indices in a hash map for constant lookup
        score_indices = {score[i]: i for i in range(len(score))}

        for i in range(len(score)):
            score[i] *= -1
        
        score_heap = copy.deepcopy(score)

        heapq.heapify(score_heap)
        curr_place = 1

        while len(score_heap) != 0:
            score_val = heapq.heappop(score_heap) * -1
            
            if curr_place == 1:
                results[score_indices[score_val]] = "Gold Medal"
            elif curr_place == 2:
                results[score_indices[score_val]] = "Silver Medal"
            elif curr_place == 3:
                results[score_indices[score_val]] = "Bronze Medal"
            else:
                results[score_indices[score_val]] = str(curr_place)

            curr_place += 1
        
        return results