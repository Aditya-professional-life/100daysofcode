class Solution:

    def toh(self, N, fromm, to, aux):
        if N == 1:
            print("move disk 1 from rod {} to rod {}".format(fromm, to))
            return 1
        else:
            steps1 = self.toh(N - 1, fromm, aux, to)
            print("move disk {} from rod {} to rod {}".format(N, fromm, to))
            steps2 = self.toh(N - 1, aux, to, fromm)
            return 1 + steps1 + steps2