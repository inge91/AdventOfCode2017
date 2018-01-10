
maxDiff(L, MaxDiff) :-
	min_list(L, Min),
	max_list(L, Max),
	MaxDiff is Max - Min.


solve2([], 0).

solve2([H|T], Result):-
	maxDiff(H, Y),
	solve2(T, X),
	Result is X + Y.

solve(I, S):-
	solve2(I, S). 

	
