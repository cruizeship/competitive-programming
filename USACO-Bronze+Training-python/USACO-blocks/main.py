'''
ID: an.cruz1
LANG: PYTHON3
TASK: blocks
'''

#http://usaco.org/index.php?page=viewproblem2&cpid=664 

""" inPut --> form N lists
calculate --> compare word1 in a list to word2 in a list
              find all of the letters that are needed - copies of the same letter with the same quantity
output --> create list of the occurences of each letter

compare each set to each other
"""

def inPut():
  f = open('blocks.in', 'r')
  N = int(f.readline().strip())
  lstOfLsts = []
  for i in range(N):
    lst = []
    var = f.readline().strip().split()
    var1 = var[0]
    var2 = var[1]
    lst.append(var1)
    lst.append(var2)
    lstOfLsts.append(lst)
  return lstOfLsts
  #inPut creates N lists inside of lstOfLsts. 
  #each list contains two words (representative of both sides of a card)

def calculate(lstOfLsts):
  finalDict = {}
  alphabetLst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #alphabetLst used to reference items in alphabetDict
  for i in range(len(lstOfLsts)):
    alphabetDict1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0} #letter count for word one
    alphabetDict2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0} #letter count for word two
    alphabetDict3 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0} #total letter count for both words
    for l in lstOfLsts[i][0]:
      alphabetDict1[str(l)] += 1 
    for m in lstOfLsts[i][1]:
      alphabetDict2[str(m)] += 1
    #looks back at lstOfLsts and adds the correct amount of letters in each word to their respective alphabetDict
    for n in range(26):
      if alphabetDict1[alphabetLst[n]] == 0 and alphabetDict2[alphabetLst[n]] == 0: 
        pass #if none of the words have a certain letter, nothing is added to alphabetDict3
      if alphabetDict1[alphabetLst[n]] == alphabetDict2[alphabetLst[n]]:
        alphabetDict3[alphabetLst[n]] = alphabetDict1[alphabetLst[n]] #if both words contain an equal amount of a certain letter, the quantity from alphabetDict1 is added to alphabetDict3
      if alphabetDict1[alphabetLst[n]] > alphabetDict2[alphabetLst[n]]:
        alphabetDict3[alphabetLst[n]] = alphabetDict1[alphabetLst[n]]
        #if alphabetDict1 contains more of a certain letter than alphabetDict2, the quantity from alphabetDict1 is added to alphabetDict3
      if alphabetDict1[alphabetLst[n]] < alphabetDict2[alphabetLst[n]]:
        alphabetDict3[alphabetLst[n]] = alphabetDict2[alphabetLst[n]]
        #if alphabetDict2 contains more of a certain letter than alphabetDict1, the quantity from alphabetDict2 is added to alphabetDict3
      else:
        pass  
    if len(finalDict) == 0:
      finalDict = alphabetDict3
    #on the first list of letters, finalDict will be made equal to alphabetDict3
    else:
      for o in finalDict: 
        finalDict[o] = finalDict[o] + alphabetDict3[o] 
        #on every other list of letters, the values in finalDict are added to the values in alphabetDict3
  return finalDict

def output(finalDict):
  alphabetLst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #alphabetLst used to reference items in alphabetDict
  out = open('blocks.out', 'w')
  for i in range(len(finalDict)):
    out.write(str(finalDict[alphabetLst[i]]) + '\n')
  out.close()

output(calculate(inPut()))