
solve2([H|[]], 0, H).

solve2([H, H|T], NewC, X):-
	solve2([H|T], C, X),
	NewC is C + H.
 	
solve2([_, I|T], Current, X):-
	solve2([I|T], Current, X). 

solve(X):-
	parseInput(X, [], [H|T]),
	solve2([H|T], Result, H),
	NewResult is Result + H,
	print(NewResult).

solve(X):-
	parseInput(X, [], [H|T]),!,
	solve2([H|T], Result, L),
	print(Result).
	

parseInput(X, Y, Y):-
	X == 0.

parseInput(Number, X, Result) :-
	NewDigit is mod(Number, 10),
	NewNumber is div(Number, 10),
	parseInput(NewNumber, [NewDigit|X], Result),!.

