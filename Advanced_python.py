def Foo():
	print "Hello - Foo"

def func(arg1, arg2 = Foo()):
	print "Entering func1"
	def inner_func(arg3=arg2):
		print "entering inner_func"
		return arg1, arg3 

	arg1 = arg2 = None
	return inner_func

func(10,Foo())