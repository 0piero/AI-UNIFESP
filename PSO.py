def func(x):
	return 1+2*x-x**2
def PSO(w, c1, c2, r1, r2, v, x, lbp, gbp, f, iter):
	for it in range(iter):
		l1 = list(map(lambda x,w: x*w, v, [w for _ in range(len(x))]))
		l2 = list(map(lambda x,c1,r1: x*c1*r1, [p-x_i for p, x_i in zip(lbp, x)], [c1 for _ in range(len(x))], [r1 for _ in range(len(x))]))
		l3 = list(map(lambda x,c2,r2: x*c2*r2, [gbp - x_i for x_i in x], [c2 for _ in range(len(x))], [r2 for _ in range(len(x))]))
		v = list(map(lambda a, b, c: a+b+c, l1, l2, l3))
		x = [x_i + v_i for x_i,v_i in zip(x,v)]
		f_ = [func(x_i) for x_i in x]
		for i, (f_i, f_j) in enumerate(zip(f_, f)):
			if f_i>f_j:
				f[i] = f_i
				lbp = x
			if f_i>func(gbp):
				gbp = x[i]
		print("iteração:",it)
		print("X:",x)
		print("V:",v)
		print("G:",gbp)
		print("P:",lbp)
	return x


if __name__ == '__main__':
	X_inicial = [-0.343, 3.956, -1.123, -0.098, 0.039]
	V_inicial = [0.0319, 0.3185, 0.3331, 0.2677, -0.3292]
	#F_inicial = [0.1976, -6.7368, -2.5061, 0.7942, 1.0755]
	F = [func(x) for x in X_inicial]
	#gbp = 0.039
	c1=0.2
	c2 = 0.6
	r1 = 0.4657
	r2 = 0.5319
	w = 0.7
	xi = PSO(w, c1, c2, r1, r2, V_inicial, X_inicial, X_inicial, X_inicial[F.index(max(F))], F, 2)
	print("Final:",xi)




	