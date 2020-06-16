# 937. Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def way_to_sort(log):
            id, after_id log.split(" ", max_split=1)
            if after_id[0].isalpha:
                return (0, after_id, id)
            else:
                return (1, )

    sorted_logs = sorted(logs, key = way_to_sort)
    return sorted_logs