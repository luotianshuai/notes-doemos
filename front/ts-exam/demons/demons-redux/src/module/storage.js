// 浏览器的 localStorage 自定义模块
let storage = {
    set(key,value){
        localStorage.setItem(key,JSON.stringify(value))
    },
    get(key){
        return JSON.parse(localStorage.getItem(key));
    },
    del(key){
        localStorage.removeItem(key);
    },
};

export default storage;
