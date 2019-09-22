function solution(n) {
    // n+1 이라고 해준 이유는 사람이 사고하는 것처럼 2번째 방이 2가 되기 위해서 한칸 더 늘려서 표현함
    var boolArray = new Array();
    for(var i=0 ; i<n+1;i++){
        boolArray.push(true)
    }
    boolArray[0] = false; // 0은 소수가 아니니 false
    boolArray[1] = false; // 1이라고 생각하고 1은 소수가 아니니 false
    for(var i=2;i*i<n+1;i++){
        if (boolArray[i]==true){
            for(var j = i+i; j < n+1; j += i){
                boolArray[j] = false;
            }
        }
    }
    var count = 0;
    for(var i=0;i<n+1;i++){
        if(boolArray[i]==true){
            count += 1;
        }
    }
    return count;
}

console.log(solution(10))