function solution(s) {
    var answer = [0, 0];
    
    while(s.length !== 1) {
        var arr = [...s].map(Number);
        answer[0]++;
        answer[1] += arr.filter(n => n === 0).length;
        s = arr.filter(n => n === 1).length.toString(2);
    }
    return answer;
}