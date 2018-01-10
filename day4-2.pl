
anagram2([], _, true).

anagram2([H|_], Y, false):-
	\+member(H, Y).

anagram2([H|T], Y, X):-
	member(H, Y),
	anagram2(T, Y, X).

anagram(X, Y, Return):-
	atom_chars(X, CX), 
	atom_chars(Y, CY), 
	length(CX, LX),
	length(CY, LY),
	LX == LY,
	anagram2(CX,CY, Return),!.

anagram(_, _, false).


anagramsInList([], false).

anagramsInList([X|T], Out):-
	findall(Y, (member(Y, T), anagram(X, Y, true)), Y),
	length(Y, 0),
	anagramsInList(T, Out).

anagramsInList(_, true).

solve([], 0).

solve([H|T], Result):-
	anagramsInList(H, R),
	R == false,
	print(H),
	solve(T, X),
	Result is X + 1.

solve([_|T], X):-
	solve(T, X).

