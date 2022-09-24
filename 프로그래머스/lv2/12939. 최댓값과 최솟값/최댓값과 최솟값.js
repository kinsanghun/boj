const max = (list) => {
    var m = list[0];
    list.map( d => d > m ? m = d : m )
    return m;
}
const min = (list) => {
    var m = list[0];
    list.map( d => d < m ? m = d : m )
    return m;
}

function solution(s) {
    let list = s.split(" ").map(Number)
    
    return `${min(list)} ${max(list)}`;
}