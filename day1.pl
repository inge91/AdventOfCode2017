

solve2([H|[]], Current, Current, H).

solve2([H, H|T], Current, Result, X):-
	NewCurrent is Current + H,
	solve2([H|T], NewCurrent, Result, X). 
 	
solve2([_, I|T], Current, Result, X):-
	solve2([I|T], Current, Result, X). 
	
	
solve(X) :-
	parseInput(X, [], [H|T]),
	solve2([H|T], 0, Result, Last),
	(Last == H,
	NewResult is Result + Last,
	print(NewResult));
	print(Result).
	

parseInput(X, Y, Y):-
	X == 0.

parseInput(Number, X, Result) :- 
	NewDigit is mod(Number, 10),
	NewNumber is div(Number, 10),
	parseInput(NewNumber, [NewDigit|X], Result).


