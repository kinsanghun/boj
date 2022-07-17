import Foundation

let cnt:Int = Int(readLine()!)!
var total:Int = 0
var stack:[Int] = []
for _ in 0..<cnt{
	let n = Int(readLine()!)!
	
	if n == 0 {
		total -= stack.popLast()!
	} else {
		stack.append(n)
		total += n
	}
}
print(total)
