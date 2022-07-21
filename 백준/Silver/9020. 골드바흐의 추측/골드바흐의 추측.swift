let n = Int(readLine()!)!
let m = 10000

var list:[Int] = [Int](0...m)

for i in 2...m {
	if list[i] == 0 {
		continue
	}
	for j in stride(from:i+i, through: m, by: i) {
		list[j] = 0
	}
}
for _ in 1...n {
	let input = Int(readLine()!)!
	var prime1 = input / 2
	var prime2 = input / 2
	while true {
		if list[prime1] + list[prime2] == input {
			print(prime1, prime2)
			break
		}
		else {
			prime1 -= 1
			prime2 += 1
		}
	}
}