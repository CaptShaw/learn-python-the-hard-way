print 1, (True and True) == 1
print 2, (False and True) == 0
print 3, (1 == 1 and 2 == 1) == 0
print 4, ("test" == "test") == 1
print 5, (1 == 1 or 2 != 1) == 1
print 6, (True and 1 == 1) == 1
print 7, (False and 0 != 0) == 0
print 8, (True or 1 == 1) == 1
print 9, ("test" == "testing") == 0
print 10, (1 != 0 and 2 == 1) == 0
print 11, ("test" != "testing") == 1
print 12, ("test" == 1) == 0
print 13, (not (True and False)) == 1
print 14, (not (1 == 1 and 0 != 1)) == 0 
print 15, (not (10 == 1 or 1000 == 1000)) == 0
print 16, (not (1 != 10 or 3 == 4)) == 0
print 17, (not ("testing" == "testing" and "Zed" == "Cool Guy")) == 1
print 18, (1 == 1 and not ("testing" == 1 or 1 == 0)) == 1
print 19, ("chunky" == "bacon" and not (3 == 4 or 3 == 3)) == 0
print 20, (3 == 3 and not ("testing" == "testing" or "Python" == "Fun")) == 0


