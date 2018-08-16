from typing import List, Union

l1 = ['Iraq', 'Japan', 'Australia', 'Egypt', 'Turkey']
l2 = ['Sydney', 'Istanbul', 'Tokyo', 'Baghdad', 'Cairo']
final =[]
L1 = 0
L2= 0
while L1 in l1 and L2 in l2 :
      if L1 == 'Iraq' and L2 == 'Baghdad':
        final.append([l1, l2])
      elif L1 == 'Japan' and L2 == 'Tokyo':
        final.append([l1, l2])
      elif L1 == 'Australia' and L2 == 'Sydney':
        final.append([l1, l2])
      elif L1 == 'Egypt' and L2 == 'Cairo':
        final.append([L1, L2])
      elif L1 == 'Turkey' and L2 == 'Istanbul':
        final.append([L1, L2])
        print(final)
        L1 += 1
        L2 += 1






