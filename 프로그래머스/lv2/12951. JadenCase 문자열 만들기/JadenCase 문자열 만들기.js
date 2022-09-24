function solution(s) {
    var answer = "";
    var slice = s.split(" ")
    slice.map(d => {
        string = d.toLowerCase();
        answer += " " + string.charAt(0).toUpperCase() + string.slice(1);
    })
    return answer.slice(1);
}