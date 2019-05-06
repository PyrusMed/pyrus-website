const LATENCY_TEST_DURATION_MINUTES = 3

$(window).load(() => {
    $('.start').click(start)
})

function start() {
    // Hide the start button
    $('.start').hide()

    // Show the timer
    $('.timer').show()

    // Show the latency counter
    $('.latency').show()

    // Start the timer and call the end function
    // when the timer expires
    startTimer(end)
}

function startTimer(endCallback) {
    var startTime = new Date
    var endTime = new Date
    endTime.setMinutes(startTime.getMinutes() + LATENCY_TEST_DURATION_MINUTES)

    var cancelKey = setInterval(() => {
        var now = new Date

        // If time has expired stop the interval
        // and execute the callback
        if (now > endTime) {
            clearInterval(cancelKey);
            endCallback();
        }
        else {
            var timeLeftMilliseconds = endTime - now
            var milliseconds = timeLeftMilliseconds % 1000
            var s = (timeLeftMilliseconds - milliseconds) / 1000
            var seconds = s % 60
            s = (s - seconds) / 60
            var minutes = s % 60

            $('.timer').text(minutes + ':' + seconds)
        }
    }, 10);
}

function end() {
    // Hide the timer
    $('.timer').hide()

    // Show the thank you message
    $('.thankyou').show()
}