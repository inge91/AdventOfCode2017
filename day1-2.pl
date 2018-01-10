
splitDIY(X, 0, [], X).

splitDIY([H|X], Counter, [H|R1], R2):-
	MinCounter is Counter - 1,
	splitDIY(X, MinCounter, R1, R2).	

solve2([], [], Current, Current).

solve2([H|T1], [H|T2], Current, Result):-
	NewCurrent is Current + H * 2,
	solve2(T1, T2, NewCurrent, Result). 
 	
solve2([_|T1], [_|T2], Current, Result):-
	solve2(T1, T2, Current, Result). 
solve(X) :-
	parseInput(X, [], L1),
	length(L1, Len),
	Half is Len / 2,
	splitDIY(L1, Half, L2, L3),	
	solve2(L2, L3, 0, Result),
	print(Result).
	

parseInput(X, Y, Y):-
	X == 0.

parseInput(Number, X, Result) :-
	NewDigit is mod(Number, 10),
	NewNumber is div(Number, 10),
	parseInput(NewNumber, [NewDigit|X], Result).


