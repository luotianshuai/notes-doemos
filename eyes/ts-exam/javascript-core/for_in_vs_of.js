// for xx in 循环获取一个对象所有可枚举的属性
// for xx of 获取可迭代对象的属性值
let list_a = ["a", "b", "c", "d", "e"];

for (let a in list_a){
    console.log(a)
}

for (let b of list_a){
    console.log(b)
}
