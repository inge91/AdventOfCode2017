% For day7-1 no programming was necessary. I started at the first program in the list and used ctrl-f to see if it was supported by a different program.
% Then, I looked for that supporting program in the same way, until I found a program that was not supported by a different program: mkxke.


% Now, the second problem is more interesting. To more easily manipulate the list in Prolog, I did some preprocessing, so each entry had the following form:


% write some functions to construct a tree datastructure from the not so nice to process data list we created.

findNode([], _, []).

findNode([[[Child, W]|T]|_], Child, [[Child, W]|T]). 

findNode([_|Rest], Child, R):-
	findNode(Rest, Child, R). 

tree([], _, []).

tree([Parent|H], MessyTree, [[[Parent, Weight],[]]| NewH]):-
	findNode(MessyTree, Parent, [[Parent, Weight]|[]]),
	tree(H, MessyTree, NewH).

tree([Parent|T], MessyTree, [[[Parent, Weight]|ChildTree]|NewT]):-
	findNode(MessyTree, Parent, [[Parent, Weight]|ChildList]),
	tree(ChildList, MessyTree, ChildTree),
	tree(T, MessyTree, NewT).

% This will succeed when Parent matches as a child for any other node.
findRoot([[[Parent, _]|_]|T], Root):-
	member([[_,_]|P], T),
	member(Parent, P),
	findRoot(T, Root).

branchSum([], 0).
branchSum([[[_, W]|Children]|T], NewW):-
	branchSum(T, RestW),
	NewW is W + RestW.

notAllEqual([], false).

notAllEqual([H|T], true):-
	\+ member(H, T).

notAllEqual([H|T], X):-
	notAllEqual(T, X).	

findWrongWeight([], 0).

findWrongWeight([[[_|[Children]]|T], Result):-
	findall(Sum, (member(Y, Children), branchSum(Y, Sum), Sum),
	notAllEqual(Sum, true),

	
	
	
	

solve(MessyTree, Weight):-
	tree([tknk], MessyTree, CleanTree),!,
	print(CleanTree),
	branchSum(MessyTree, Weight),
	findWrongWeight(CleanTree).
	
 
