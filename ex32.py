the_count=[1,2,3,4,5]
fruit=['apple','orange','pears','apricots']
change=[1,'pennies',2,'dimes',3,'quaters']

#this first kind of for-;oop goes through a list
for number in the_count:
    print "This is count%d"%number

#same as above
    print "A fruit of type:%s"%fruit

#also we can go through mixed lists too
#notice we have to use%r sincde we don't know what's in it
for i in change:
    print "I got %r"%i

#we can also build lists, firs start with an empty one
elements=[]

#then use the rage function to do 0 to 5 counts
for i in range(0,6):
    print "Adding %d to the list."%i
    #append is a function that lists Understand
    elements.append(i)

#now we can print them out too
for i in elements:
    print "Elemnet was: %d"%i
