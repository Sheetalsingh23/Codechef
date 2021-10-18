import numpy
import itertools
for _ in range(int(input())):
      n = int(input())
      a = list(map(int, input().split()))
      mini = min(a)-1
      maxi = max(a)+1
      l = []
      for i in range(mini, maxi+1):
            l.append(i)
      # print(l)
      def find(l,n):
            return len([list(i) for i in itertools.combinations(l,n) if numpy.prod(i)%2==0])
      print(find(l,n))
