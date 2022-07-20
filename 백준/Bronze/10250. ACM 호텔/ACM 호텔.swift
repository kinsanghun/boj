let cnt = Int(readLine()!)!

(0..<cnt).forEach { _ in
    let inputs = readLine()!.split(separator: " ").map { Int(String($0))! }
    let H = inputs[0]
    let _ = inputs[1]
    let n = inputs[2]
    let h = (n - 1) % H + 1
    let w = (n - 1) / H + 1
    let wString = w < 10 ? "0\(w)" : "\(w)"
    print("\(h)\(wString)")
}