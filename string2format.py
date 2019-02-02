string2format="""1407
1428
1449
1470
1491
1512
1533
1554
1575
1596
1617
1638
1659
1680
1701
1722
1743
1764
1785
1806
1827
1848
1869
1890
1911
1932
1953
1974
1995"""

liste = string2format.splitlines()
newstr = ""
for i in range(0,len(liste),5):
    newstr = newstr + ",".join(liste[i:i+5])+"\n"
print(newstr)