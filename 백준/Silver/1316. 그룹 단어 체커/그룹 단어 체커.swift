func check(word: String) -> Int {
    var group = [Character]()
    var f: Character = "_"
    
    for c in word {
        if group.contains(c) {
            return 0
        }
        
        if c != f {
            group.append(f)
            f = c
        }
    }
    return 1
}

let cnt = Int(readLine()!)!
var total:Int = 0

for _ in 0...cnt-1 {
	let str = readLine()!
	total += check(word:str)	
}
print(total)