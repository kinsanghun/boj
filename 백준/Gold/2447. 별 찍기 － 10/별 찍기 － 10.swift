var result = ""

func solution(_ n: Int, _ i: Int, _ j: Int) {
    if (i / n) % 3 == 1 && (j / n) % 3 == 1 {
        result += " "
    }else {
        if n / 3 == 0 {
            result += "*"
        }else {
            solution(n / 3, i, j)
        }
    }
}

let n = Int(readLine()!)!

for i in 0..<n {
    for j in 0..<n {
        solution(n,i,j)
    }
    result += "\n"
}
print(result)
