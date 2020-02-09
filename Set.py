from random import random, uniform, sample

import textdistance


class Set:

    def __init__(self):
        self.set = []
        self.size = 0
       # self.tmpresult = {'index': 0, 'list': [], 'params': [], 'percentage': 0, 'similarity': 0, 'distance': 0,
        #                  'full_match': 0}
        self.listofResults = []

    def addToSet(self, l):
        self.set.append(l)

    def createSet(self, num, l):
        self.set.clear()
        self.size = num
        start = 0
        end = len(l)
        for a in range(self.size):
            print('=========================')
            tmp = int(uniform(start, end)) + 1
            tmp2 = sample(range(start, end), tmp)
            # tmp3 = l[tmp2]
            # tmp2.sort()
            tmplist = []
            for a in tmp2:
                tmplist.append(l[a])
            self.set.append(tmplist)
            print(a)

    def findParams(self, s):
        lenS = len(s)
        print("rozmiar wyszukiwanej listy: " + str(lenS))
        for index, a in enumerate(self.set):
            lenA = len(a)
            #    print("rozmiar przeszukiwanej listy: " + str(lenA)) 'params': [],
            tmpresult = {'index': 0, 'list': [], 'percentage': 0, 'similarity': 0, 'distance': 0,
                              'full_match': 0}
            i = 0  # index po s
            # j = 0 # index po a
            while i < lenA - lenS + 1:
                tmp = 0
                j = 0
                while j < lenS:
                    if (s[j] == a[i + j]):
                        tmp += 1
                    j += 1
                valuesa = ','.join(str(v) for v in a)
                valuess = ','.join(str(v) for v in s)
                similarity = textdistance.levenshtein.similarity(valuess, valuesa)
                distance = textdistance.levenshtein.distance(valuess, valuesa)
                if tmp != 0:

                    tmpresult['index'] = index
                    tmpresult['list'] = str(a)
                    #tmpresult['params'] = str(a[i:i + lenS])
                    tmpresult['percentage'] = float(tmp / lenS)
                    tmpresult['similarity'] = similarity
                    tmpresult['distance'] = distance

                    if (lenS == lenA == tmp):
                        tmpresult['full_match'] = 1

                    self.listofResults.append(tmpresult)
                    print(self.listofResults)
                i += 1
