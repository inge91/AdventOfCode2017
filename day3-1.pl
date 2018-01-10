actualDistance(_, _, _, Number, Number, D, D).

actualDistance(MaxDistance, MD, _, Number, Value, MaxDistance, D):-
	NewIncr is -1,
	NewNumber is Number - 1,
	NewDistance is MaxDistance + NewIncr,
	actualDistance(MaxDistance, MD, NewIncr, NewNumber, Value, NewDistance, D).

actualDistance(MD, MinDistance, _, Number, Value, MinDistance, D):-
	NewIncr is 1,
	NewNumber is Number - 1,
	NewDistance is MinDistance + NewIncr,
	actualDistance(MD, MinDistance, NewIncr, NewNumber, Value, NewDistance, D).

actualDistance(MD1, MD2, Incr, Number, Value, Distance, D):-
	NewNumber is Number - 1,
	NewDistance is Distance + Incr,
	actualDistance(MD1, MD2, Incr, NewNumber, Value, NewDistance, D).

ceilToUneven(X, Y):-
	ceiling(X, Y),
	N is mod(Y, 2),
	N == 1.

ceilToUneven(X, Y):-
	ceiling(X, L),
	N is mod(L, 2),
	Y is L + 1,
	N == 0.

solve(Number) :-
	sqrt(Number, Y),
	ceilToUneven(Y, NextSqrt),
	floor(NextSqrt / 2, MinDistance), 
	MaxDistance is MinDistance * 2,
	pow(NextSqrt, 2, MaxValue),
	actualDistance(MaxDistance, MinDistance, 1, MaxValue, Number, MaxDistance, Distance),
	print(Distance).







