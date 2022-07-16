var datas:[Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
var nodes:[[Int]] = [[Int]](repeating: [Int](repeating: 0, count: 0), count: datas[0] + 1)

for _ in 0..<datas[1]{
	let node = readLine()!.split(separator: " ").map { Int(String($0))! }
	nodes[node[0]].append(node[1])
    nodes[node[1]].append(node[0])
}

var visited = [Int](repeating: 0, count: datas[0] + 1)
var current = 1

nodes = nodes.map { $0.sorted(by: { $0 < $1 })}

func dfs(R:Int){
	visited[R] = current
	for x in nodes[R] {
		if visited[x] == 0{
			current += 1
			dfs(R:x)
		}
	}
}

dfs(R:datas[2])

for i in 1..<visited.count{
	print(visited[i])
}

