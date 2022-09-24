function solution(s) {
    var now = s;
    var convert_count = 0;
    var zero_count = 0;
    while(now.length !== 1) {
        convert_count++;
        var arr = [...now].map(Number);
        let one = arr.filter(n => n === 1).length
        zero_count += arr.filter(n => n === 0).length
        now = one.toString(2)
        console.log(now)
    }
    var answer = [convert_count, zero_count];
    return answer;
}