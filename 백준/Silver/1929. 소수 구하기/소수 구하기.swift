let input:[Int] = readLine()!.split(separator: " ").map{Int(String($0))!}

var n = input[0]
let m = input[1]

var list:[Int] = [Int](0...m)
if n == 1 {
	n = 2
}


for i in 2...m {
	if list[i] == 0 {
		continue
	}
	for j in stride(from:i+i, through: m, by: i) {
		list[j] = 0
	}
}
for l in n...m{
	if list[l] > 0 {
		print(list[l])
	}
}