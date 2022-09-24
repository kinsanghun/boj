function solution(s) {
    var answer = "";
    s.split(" ").map(d => answer += " " + d.charAt(0).toUpperCase() + d.slice(1).toLowerCase() )
    
    return answer.slice(1);
}