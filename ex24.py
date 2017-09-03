print "Let's practice everything."

print "You\'d need to know \'bout escapes with \\ that do \nnewlines and \t tabs."

poem="""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""                        #\'== 'v \\=\ \t =tab \n=return key

print "----------"
print poems
print "----------"

five=10-2+3-6
print "This should be five: %s"%five

def secret_formula(started): #define secret_formula(started)=j*500,j/1000,c/100
    jelly_beans=started*500
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars,crates

start_point=10000
beans,jars,crates=secret_formula(start_point)#j*500*10000,j/1000*10000,c/100*10000

print "With a starting pointof:%d"%start_point
print "We'd have %d beans,%d jars, and %d crates."%secret_formula(start_point)

start_point=start_point/10

print "We can also do that this way:"
print "We'd have %d beans,%d jars,and %d crates."%secret_formula(start_point)
