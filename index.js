// Function to get current time
function clock(){
    let now = new Date(), displayTime = "";
//Hours and Mins
    const time = [now.getHours(), now.getMinutes()];
    for (let i = 0; i < time.length; i++) {
        displayTime += updateTime(time[i]);
        if (i < time.length - 1) {
            displayTime += ":";
        }
    }
    document.getElementById("clock").innerText = displayTime;
}
// Function to add 0 for number less than 10
function updateTime(h) {
  if (h < 10) {
    return "0" + h;
  }
  else {
    return h;
  }
}
// With the help of Stack Overflow
clock();