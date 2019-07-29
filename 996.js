myfun = function foo(arr, start) {
    if (start == arr.length - 1) {
        console.log(arr);
        return;
    }
    for (var i=start;i<arr.length;i++) {
        var tmp = arr[start];
        arr[start] = arr[i];
        arr[i] = tmp;
        // if (i>start){
        //     console.log({start:start, i:i});
        //     console.log(arr);
        //     return 
        // }
        foo(arr, start+1);
        tmp = arr[start];
        arr[start] = arr[i];
        arr[i] = tmp;
    }
}

myfun([1,2,3,4,],0);