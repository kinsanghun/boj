import Foundation
var input = readLine()!.split(separator: " ").map { Double(String($0))!}
input[2] -= input[0]

var sum = input[2] / (input[0] - input[1])
print(Int(ceil(sum)) + 1)