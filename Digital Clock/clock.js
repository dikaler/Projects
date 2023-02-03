function EST() {

    // setting date to extract information from it
    // setting timezone to a city in EST
    var date = new Date(new Date().toLocaleString('en', {timeZone: 'America/New_York'}));

    // Get current month
    var month = date.getMonth() + 1;
    // Get current day
    var day = date.getDay() + 1;
    // Get current year
    var year = date.getFullYear();
    // Get day of week
    let weekday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][date.getDay()]
    // Get current hour
    var hour = date.getHours();
    // Get current minute
    var minute = date.getMinutes();
    // Get current second
    var second = date.getSeconds();


    // Variable to store whether its AM or PM
    var meridiem = "";

    // If day is less then 10, append 0 in front
    if (day < 10) {
        day = "0" + day;
    } else {
        day = day
    }


    // Assigning AM or PM according to the current hour
    if (hour >= 12) {
    meridiem = "PM";
    } else {
    meridiem = "AM";
    }

    // Converting the hour in 12-hour format
    if (hour == 0) {
    hour = 12;
    } else {
    if (hour > 12) {
    hour = hour - 12;
    }
    }

    // Update hour, minute, and second
    hour = update(hour);
    minute = update(minute);
    second = update(second);

    // Send date and time to respective id's
    document.getElementById("digital-date1").innerText = weekday + " " + month + "/" + day + "/" + year;
    document.getElementById("digital-clock1").innerText = hour + " : " + minute + " : " + second + " " + meridiem;
    

    // Set Timer to 1 sec
    setTimeout(EST, 1000);
    }

    // Append 0 before time elements if they are less than 10
    function update(t) {
    if (t < 10) {
    return "0" + t;
    }
    else {
    return t;
    }
};

// comments same as EST
function CST() {
    // setting timezone to a city in CST
    var date = new Date(new Date().toLocaleString('en', {timeZone: 'America/Los_Angeles'}));

    var month = date.getMonth() + 1;
    var day = date.getDay() + 1;
    var year = date.getFullYear();
    let weekday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][date.getDay()]
    var hour = date.getHours();
    var minute = date.getMinutes();
    var second = date.getSeconds();


    var meridiem = "";

    if (day < 10) {
        day = "0" + day;
    } else {
        day = day;
    }


    if (hour >= 12) {
    meridiem = "PM";
    } else {
    meridiem = "AM";
    }

    if (hour == 0) {
    hour = 12;
    } else {
    if (hour > 12) {
    hour = hour - 12;
    }
    }

    hour = update(hour);
    minute = update(minute);
    second = update(second);

    document.getElementById("digital-date2").innerText = weekday + " " + month + "/" + day + "/" + year;
    document.getElementById("digital-clock2").innerText = hour + " : " + minute + " : " + second + " " + meridiem;
    

    setTimeout(CST, 1000);
    }

    function update(t) {
    if (t < 10) {
    return "0" + t;
    }
    else {
    return t;
    }
};

// same comments as Local function
function PST() {
    // setting time zone to a city in PST
    var date = new Date(new Date().toLocaleString('en', {timeZone: 'America/Chicago'}));

    var month = date.getMonth() + 1;
    var day = date.getDay() + 1;
    var year = date.getFullYear();
    let weekday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][date.getDay()]
    var hour = date.getHours();
    var minute = date.getMinutes();
    var second = date.getSeconds();


    var meridiem = "";

    // Format Day
    if (day < 10) {
        day = "0" + day;
    } else {
        day = day;
    }


    if (hour >= 12) {
    meridiem = "PM";
    } else {
    meridiem = "AM";
    }

    if (hour == 0) {
    hour = 12;
    } else {
    if (hour > 12) {
    hour = hour - 12;
    }
    }

    hour = update(hour);
    minute = update(minute);
    second = update(second);

    document.getElementById("digital-date3").innerText = weekday + " " + month + "/" + day + "/" + year;
    document.getElementById("digital-clock3").innerText = hour + " : " + minute + " : " + second + " " + meridiem;
    

    setTimeout(PST, 1000);
    }

    function update(t) {
    if (t < 10) {
    return "0" + t;
    }
    else {
    return t;
    }
};

//comments are the same for each of the respective hide functions (except the timezones)
//will toggle the display from each digital clock
function hide1() {
    // set x = the time for EST
    var x = document.getElementById("digital-clock1");
    // set y = the h1 for EST
    var y = document.getElementById("h1id1");
    // set z = the date for EST
    var z = document.getElementById("digital-date1");
    //toggle each upon the click of the button
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    };

    if (y.style.display === "none") {
        y.style.display = "block";
    } else {
        y.style.display = "none";
    };

    if (z.style.display === "none") {
        z.style.display = "block";
    } else {
        z.style.display = "none";
    };
};

function hide2() {
    var x = document.getElementById("digital-clock2");
    var y = document.getElementById("h1id2");
    var z = document.getElementById("digital-date2");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    };

    if (y.style.display === "none") {
        y.style.display = "block";
    } else {
        y.style.display = "none";
    };

    if (z.style.display === "none") {
        z.style.display = "block";
    } else {
        z.style.display = "none";
    };
};

function hide3() {
    var x = document.getElementById("digital-clock3");
    var y = document.getElementById("h1id3");
    var z = document.getElementById("digital-date3");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    };

    if (y.style.display === "none") {
        y.style.display = "block";
    } else {
        y.style.display = "none";
    };

    if (z.style.display === "none") {
        z.style.display = "block";
    } else {
        z.style.display = "none";
    };
};