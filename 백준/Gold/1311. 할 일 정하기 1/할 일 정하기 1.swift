let n = Int(readLine()!)!
var work:[[Int]] = Array(repeating:Array(repeating: -1, count: (1 << 21)), count: 20)
var d:[[Int]] = []
for _ in 1...n {
	d.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}

func solution(x: Int, v: Int) -> Int 
{
	if x == n 
  {
		return 0
	}
	else if work[x][v] != -1 
  {
		return work[x][v]
	}
	else {
		work[x][v] = 1_000_000
		for i in 0..<n 
    {
			if (v & (1 << i)) == 0 
      {
				work[x][v] = min(work[x][v], solution(x : x+1, v : v|(1 << i)) + d[x][i])
			}
		}
		return work[x][v]
	}
}
print(solution(x:0, v:0))
