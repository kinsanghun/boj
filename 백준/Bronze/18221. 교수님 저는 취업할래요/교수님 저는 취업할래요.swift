import Foundation

let n = Int(readLine()!)!

var tables = [[Int]]()
var teacher = (0,0)
var run = (0,0)

func getRact() -> [(Int,Int)] {
    var row = (0,0)
    var col = (0,0)
    
    row.0 = min(teacher.0,run.0)
    row.1 = max(teacher.0,run.0)
	
    col.0 = min(teacher.1,run.1)
    col.1 = max(teacher.1, run.1)
    
    return [row,col]
}

func compareDist() -> Bool  { return Int(sqrt(Double(pow(Double(abs(teacher.0 - run.0)),Double(2))+pow(Double(abs(teacher.1 - run.1)),Double(2))))) >= 5 }



for i in 0..<n
{
    let list = readLine()!.split(separator : " " ).map{Int(String($0))!}
    for j in 0..<list.count
	{
        let tmp = list[j]
        if tmp == 5 { teacher = (i,j) }
		else if tmp == 2 { run = (i,j) }
    }
    tables.append(list)
}

if compareDist() 
{
    let rect = getRact()
    var cnt = 0
    quit : for i in rect[0].0...rect[0].1 
	{
        for j in rect[1].0...rect[1].1 
		{
            if tables[i][j] == 1 { cnt += 1 }
            if cnt >= 3 { break quit }
        }
    }
    if cnt >= 3 { print(1) }
	else { print(0) }
}
else { print(0) }

