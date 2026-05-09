let reservationList = [];
const NB_CALCULATIONS = parseInt(readline());
for (let i = 0; i < NB_CALCULATIONS; ++i) {
  let inputs = readline().split(' ');
  let startDay = parseInt(inputs[0]);
  let duration = parseInt(inputs[1]);
  let task = {
    "startDay": startDay,
    "endDay": startDay + duration - 1
  }
  reservationList.push(task);
}

reservationList.sort(function(task1, task2) {
  return task1.endDay - task2.endDay;
});

let nbTasksCompleted = 1;
let prevIndex = 0;
for (let i = 1; i < NB_CALCULATIONS; ++i) {
  let task = reservationList[i];
  let prevTask = reservationList[prevIndex];
  // check if task doesn't overlap
  if (task.startDay > prevTask.endDay) {
    ++nbTasksCompleted;
    prevIndex = i;
  }
}

print(nbTasksCompleted);
