from collections import deque

n, m = map(int, input().split())

adj = [[] for _ in range(n)]
for _ in range(m):
	a, b = map(int, input().split())
	adj[a - 1].append(b - 1)
	adj[b - 1].append(a - 1)

assigned = [0 for _ in range(n)]
valid = True
for i in range(n):
	if assigned[i] != 0:
		continue

	assigned[i] = 1
	todo = deque([i])
	while todo:
		curr = todo.popleft()
		n_color = 2 if assigned[curr] == 1 else 1
		for next_ in adj[curr]:
			if assigned[next_] != 0:
				if assigned[next_] != n_color:
					valid = False
					break
			else:
				assigned[next_] = n_color
				todo.append(next_)

		if not valid:
			break

	if not valid:
		break

if valid:
	print(" ".join(str(i) for i in assigned))
else:
	print("IMPOSSIBLE")
