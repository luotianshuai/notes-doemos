let state = {
    count: 1
};

console.log(state.count);

state.count = 2;

console.log(state.count);

// 好了，现在我们实现了状态（计数）的修改和使用了
// 当然上面的有一个很明显的问题：修改 count 之后，使用 count 的地方不能收到通知。我们可以使用发布-订阅模式来解决这个问题

