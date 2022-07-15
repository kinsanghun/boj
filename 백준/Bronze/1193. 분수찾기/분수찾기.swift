var n = Int(readLine()!)!
var count = 1

while true {
    n -= count
    if n <= 0 {
        break
    }
    count += 1
}
if count % 2 == 1 {
    print("\(-n+1)/\(n+count)")
} else {
    print("\(n+count)/\(-n+1)")
}