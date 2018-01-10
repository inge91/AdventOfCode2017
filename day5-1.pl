
append(X, [], [X]).

append(X, [H|T], [H|Q]):-
	append(X, T, Q).

popLastElement([X], [], X).
popLastElement([H|T], [H|Q], X):-
	popLastElement(T, Q, X).

moveForward(B, C, [], B, C , [], Count, Count).

moveForward(B, C, A, B, C, A, 0, 0).

moveForward(Before, Current, [After|T], X, Y, Z, Count, C):-
	NewCount is Count - 1,
	append(Current, Before, NewBefore),
	moveForward(NewBefore, After, T, X, Y, Z, NewCount, C).
	

moveBackward([], C, A, [], C , A, Count, Count).

moveBackward(B, C, A, B, C, A, 0, 0).

moveBackward(Before, Current, After, X, Y, Z, Count, C):-
	NewCount is Count - 1,
	popLastElement(Before, NewBefore, NewCurrent),
	moveForward(NewBefore, NewCurrent, [Current|After], X, Y, Z, NewCount, C).	



printList([]).

printList([H|T]):-
	print(H),
	print(' '),
	printList(T).

printList(X):-
	print("["),
	print(X),
	print("]").

printDividedList(H, C, T):-
	printList(H),
	print(' '),
	printList(C),
	print(' '),
	printList(T),
	nl.

move(A, X, [], 0):-
	X > 0,
	printList(A).
		
	
move(A, X, _, 0):-
	X < 0,
	printList(A).

move(Before, Current, After, NewCounter):-
	C is Current + 1,
	Current < 0,
	abs(Current, CurrentAbs),
	moveBackward(Before, C, After, NewBefore, NewCurrent, NewAfter, CurrentAbs, Steps),
	move(NewBefore, NewCurrent, NewAfter, Counter),	 
	printDividedList(Before,Current, After),
	NewCounter is Counter + 1.

move(Before, Current, After, NewCounter):-
	C is Current + 1,
	Current > 0,
	abs(Current, CurrentAbs),
	moveForward(Before, C, After, NewBefore, NewCurrent, NewAfter, CurrentAbs, Steps),
	move(NewBefore, NewCurrent, NewAfter, Counter),	
	printDividedList(Before,Current, After),
	NewCounter is Counter + 1.

move(Before, C, After, NewCounter):-
	move(Before, Current, After, NewCounter),
	C is Current + 1.
		

solve([H|T], Y):-
	move([], H, T, Y).



