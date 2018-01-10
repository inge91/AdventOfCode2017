
uniqueElements([], []).

uniqueElements([H|T], [H|Result]):-
	\+member(H, T),
	uniqueElements(T, Result).

uniqueElements([_|T], Result):-
	uniqueElements(T, Result).

solve(Instructions, Out):-
	findall([X,0], (member(Z, Instructions), Z = [X, _, _, _, _ , _ , _]), R),
	uniqueElements(R, Result),
	performInstructions(Instructions, Result, NewResult),
	findall(Val, (member(Y, NewResult), Y = [_, Val]), Vals),	
	max_list(Vals, Out).

performInstructions([], L, L).

performInstructions([[Var, Op, Val, If, Var2, Eq, Val2]|T], L, NewL2):-
	performInstruction(Var, Op, Val, If, Var2, Eq, Val2, L, NewL),
	performInstructions(T, NewL, NewL2).


getVal([[Var, Val]|_], Var, [Var, Val]).

getVal([_|T], Var, X):-
	getVal(T, Var, X).

performInstruction([], [], []).

performInstruction(Var, Op, Val, _, Var2, Eq, Val2, L, NewL) :-
	getVal(L, Var2, VarAndVal),	
	(conditionMet([Var2, Eq, Val2], VarAndVal, true),
	 changeValue([Var, Op, Val], L, NewL));
	NewL = L. 

changeValue([H, inc, X], [[H, V]|T], [[H, NewV]|T]):-
	NewV is V + X.

changeValue([H, dec, X], [[H, V]|T], [[H, NewV]|T]):-
	NewV is V - X.

changeValue([Var, Mod, Val], [H|T], [H|X]):-
	changeValue([Var, Mod, Val], T, X).

conditionMet([Var, >, Val], [Var, V], true):- 
	V > Val.

conditionMet([Var, <, Val], [Var, V], true):- 
	V < Val.

conditionMet([Var, ==, Val], [Var, V], true):- 
	V == Val.

conditionMet([Var, \=, Val], [Var, V], true):- 
	V \= Val.

conditionMet([Var, <=, Val], [Var, V], true):- 
	V =< Val.

conditionMet([Var, >=, Val], [Var, V], true):- 
	V >= Val.

conditionMet(_, _, false).
