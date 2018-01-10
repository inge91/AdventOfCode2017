
uniqueWords([], true).

uniqueWords([H|T], false):-
	member(H, T),!. 

uniqueWords([_|T], X):-
	uniqueWords(T, X),!.

solve([], 0).

solve([H|T], Result):-
	uniqueWords(H, R),
	R == true,
	solve(T, X),
	Result is X + 1.

solve([_|T], X):-
	solve(T, X).

