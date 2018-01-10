% Removes the first max value from a list,
% returns the new list, the max value, and the
% index where it was removed from.
remove_max([], [], 0, 0).

remove_max([H|T], [0|T], H, 0):-
	max_list([H|T], H),!.

remove_max([H|T], [H|X], Max, NewCount):-
	remove_max(T, X, Max, Count),
	NewCount is Count + 1.

% Increments the value by one of the list elemented
% with index.
incrementAtIndex([H|T], 0, [IncrementedH|T]):-
	IncrementedH is H + 1.

incrementAtIndex([H|T], Index, [H|Q]):-
	NewIndex is Index - 1,
	incrementAtIndex(T, NewIndex, Q).	


% Distributes the values ToDistribute over all of the elements in the list,
% starting at the specified index Index.
distribute(Result, Result, 0, _).
distribute(Begin, NewResult, ToDistribute, Index):-
	incrementAtIndex(Begin, Index, IncrementOnce),
	NewToDistribute is ToDistribute - 1,
	length(Begin, L),
	NewIndex is mod((Index + 1), L), 
	distribute(IncrementOnce, NewResult, NewToDistribute, NewIndex). 


matchingIndex([H|_], Y, 1):-
	compare(=, H, Y).

matchingIndex([_|T], H, NewCount):-
	matchingIndex(T, H, Count),
	NewCount is Count + 1.

solve2(History, Banks, 0):-
	member(Banks, History),
	%day 6, part 2.
	matchingIndex(History, Banks, C),
	print(C).

solve2(History, Banks, IncrementedSteps):-
	remove_max(Banks, NewBanks, MaxValue, Index),
	length(Banks, L),
	NewIndex is mod((Index + 1), L), 
	distribute(NewBanks, Redistributed, MaxValue, NewIndex),
	solve2([Banks|History], Redistributed, Steps),
	IncrementedSteps is Steps + 1.
	

solve(Banks, Steps):-
	solve2(Banks, Banks, Steps).

printList([]).

printList([H|T]):-
	print(H),
	print(' '),
	printList(T).
