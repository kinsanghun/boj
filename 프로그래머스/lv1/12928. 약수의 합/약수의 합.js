function solution(n) {
    let answer = 0;
    
    for(var i = 0; i <= parseInt(n / 2); i++ ){
        if(n % i == 0) {
            answer += i;
        }
    }
    return answer + n;
}