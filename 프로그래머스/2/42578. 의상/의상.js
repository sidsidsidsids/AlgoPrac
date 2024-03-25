function solution(clothes) {
    var answer = 0;
    const items = new Map();
    clothes.forEach((item, _) => {
        const kind = item[1];
        if (!items.has(kind)) {
            items.set(kind, 1)
        }
        items.set(kind, items.get(kind) + 1)
    })
    let value = 1
    items.forEach((val, key) => {
        value *= val
    })
    value -= 1
    answer += value
    return answer;
}