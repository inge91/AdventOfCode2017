
complement(X, [X|L], L).

complement(X, [H|T], [H|L]):-
	complement(X, T, L).


maxDiff([], 0).

maxDiff([Diff| T], Diff):-
	maxDiff(T, Diff2),
	Diff >= Diff2.

maxDiff([Diff| T], Diff2):-
	maxDiff(T, Diff2),
	Diff < Diff2.


divisionTuples(L, Result) :-
	member(X, L), 
	complement(X, L, C),	
	member(Y, C),
	Result is X / Y,
	integer(Result).

solve2([], 0).

solve2([H|T], Result):-
	findall(X, divisionTuples(H, X ), Z),
	print(Z),
	maxDiff(Z, R),
	print(R),
	solve2(T, X),
	Result is X + R.

solve(I, S):-
	solve2(I, S). 

	
