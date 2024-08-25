import copy
class Solution:
    min_len = float('inf')
    res_path = []
    cost = None

    def shortestSuperstring(self, words) -> str:
        #
        n = len(words)
        cost = [[len(words[i]) for i in range(n)] for _ in range(n)]

        # preprocess
        for i in range(n):
            for j in range(n):
                left_w = words[i]
                right_w = words[j]
                for k in range(1, len(right_w)):
                    if left_w[len(left_w) - k:] == right_w[:k]:
                        cost[i][j] = len(right_w) - k
        self.cost = cost

        # dfs
        cur_len = 0
        path = []
        uniq_path = set()
        self.dfs(words, path, uniq_path, 0)

        res = ""
        for i in range(n):
            if i == 0:
                res = res + words[self.res_path[i]]
                continue
            res = res + words[self.res_path[i]][len(words[self.res_path[i]]) - cost[self.res_path[i-1]][self.res_path[i]]:]
        return res

    def dfs(self, words, path, uniq_path, cur_len):
        if cur_len >= self.min_len:
            return

        path_words = []
        for i in range(len(path)):
            path_words.append(words[path[i]])
        print("path: " + "\t".join(path_words))
        if len(path) == len(words):

            print("path words: " + '\t'.join(path_words))
            print("min_len: " + str(self.min_len))
            print("cur_len: " + str(cur_len))
            if cur_len < self.min_len:
                print("min len update")
                self.min_len = cur_len
                self.res_path = copy.deepcopy(path)
            print("")


        else:
            for i in range(len(words)):
                if i in uniq_path:
                    continue
                cur_len = len(words[i]) if not path else cur_len + self.cost[path[-1]][i]
                uniq_path.add(i)
                path.append(i)
                self.dfs(words, path, uniq_path, cur_len)
                uniq_path.remove(i)
                path.pop()
                cur_len = cur_len - len(words[i]) if not path else cur_len - self.cost[path[-1]][i]


if __name__ == '__main__':
    so = Solution()
    # words = ["alex", "loves", "leetcode"]
    words = ["catg","ctaagt","gcta","ttca","atgcatc"]
    # words = ["bzzfferklujni","zpgtzolmocuzanqwr","ustfecrfuqvhpaznjaxt","cuzanqwrwdslbzzffe","ehorslkpzpavzpgtzolm","xtxcsozsmaohilo","xapyixboynrakicimqe","ohiloxapyixboynra","ozsmaohiloxapyixboy","fuqvhpaznjaxtxcs","mocuzanqwrwdslbzzf","paznjaxtxcsozsmaohil"]
    # 25
    # "gctaagttcatgcatc"
    #  gctaagttcatgcatc
    # path: gcta	ctaagt	ttca
    # path: gcta	ctaagt	ttca	catg
    # path: gcta	ctaagt	ttca	catg	atgcatc
    # path words: gcta	ctaagt	ttca	catg	atgcatc
    #               2      1      3       0       4
    # 4+3+3+2+4
    # min_len: 23
    # cur_len: 24
    res = so.shortestSuperstring(words)
    print(res)