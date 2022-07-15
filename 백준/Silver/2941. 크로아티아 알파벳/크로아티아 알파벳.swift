import Foundation

let croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
var input = readLine()!

for c in croatia {
    input = input.replacingOccurrences(of: c, with: "1")
}
print(input.count)